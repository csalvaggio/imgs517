#include <pybind11/pybind11.h>

#include "primes.h"

namespace py = pybind11;

PYBIND11_MODULE(_primes, m) {
  m.doc() = "Prime utilities (C++/pybind11)";

  m.def("is_prime", &is_prime, py::arg("value"),
        "Return True if value is prime, else False.");

  m.def("nth_prime", &nth_prime, py::arg("N"),
        "Return the Nth prime (1 -> 2). Raises ValueError if N < 1.");
}
