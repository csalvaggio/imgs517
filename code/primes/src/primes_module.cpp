#include <pybind11/pybind11.h>

#include <cmath>
#include <stdexcept>

namespace py = pybind11;

bool is_prime(int value) {
  if (value < 2) return false;
  if (value == 2) return true;
  if (value % 2 == 0) return false;

  int limit = static_cast<int>(std::sqrt(value));
  for (int divisor = 3; divisor <= limit; divisor += 2) {
    if (value % divisor == 0) return false;
  }
  return true;
}

int nth_prime(int N) {
  if (N <= 0) throw std::invalid_argument("N must be >= 1");
  if (N == 1) return 2;

  int count = 1;
  int candidate = 1;

  while (count < N) {
    candidate += 2;
    if (is_prime(candidate)) {
      count++;
    }
  }
  return candidate;
}

PYBIND11_MODULE(_primes, m) {
  m.doc() = "Prime utilities (C++/pybind11)";

  m.def("is_prime", &is_prime, py::arg("value"),
        "Return True if value is prime, else False.");

  m.def("nth_prime", &nth_prime, py::arg("N"),
        "Return the Nth prime (1 -> 2). Raises ValueError if N < 1.");
}
