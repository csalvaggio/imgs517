N = 1000


"""
PURE PYTHON APPROACH
"""
import math

def is_prime(value: int) -> bool:
    """
    Determine whether an integer is a prime number.

    A prime number is an integer greater than 1 that has no positive divisors
    other than 1 and itself.

    Parameters
    ----------
    value : int
        The integer to test for primality.

    Returns
    -------
    bool
        True if the value is prime, False otherwise.
    """
    if value < 2:
        return False

    if value == 2:
        return True

    if value % 2 == 0:
        return False

    limit: int = int(math.isqrt(value)) + 1
    for divisor in range(3, limit, 2):
        if value % divisor == 0:
            return False

    return True

def nth_prime(n: int) -> int:
    """
    Compute the n-th prime number (1-indexed).

    Parameters
    ----------
    n : int
        The index of the prime number to compute. Must be >= 1.

    Returns
    -------
    int
        The n-th prime number.

    Raises
    ------
    ValueError
        If n is less than 1.
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    if n == 1:
        return 2

    count: int = 1  # We already counted the prime number 2
    candidate: int = 1

    while count < n:
        candidate += 2  # Only test odd numbers
        if is_prime(candidate):
            count += 1

    return candidate

import time

t0 = time.perf_counter()
print(nth_prime(N))
t1 = time.perf_counter()
ePython = t1 - t0
print("Time: {0:.7f} [s]".format(ePython))


"""
PYTHON BOUND C++ APPROACH
"""
import primes

t0 = time.perf_counter()
print(primes.nth_prime(N))
t1 = time.perf_counter()
eCpp = t1 - t0
print("Time: {0:.7f} [s]".format(eCpp))


"""
PERFORMANCE DIFFERENCE
"""
print("Factor: {0:.2f}x".format(ePython / eCpp))
