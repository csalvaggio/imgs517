N = 1000


"""
PURE PYTHON APPROACH
"""
import math
import primes
import time

def is_prime(value):
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False

    limit = int(math.sqrt(value) + 1)
    for divisor in range(3, limit):
        if value % divisor == 0:
            return False
    return True

def nth_prime(N):
    if N <= 0:
        raise ValueError("N must be >= 1")
    if N == 1:
        return 2

    count = 1
    candidate = 1

    while count < N:
        candidate += 2
        if is_prime(candidate):
            count += 1
    return candidate

t0 = time.perf_counter()
print(nth_prime(N))
t1 = time.perf_counter()
ePython = t1 - t0
print("Time: {0:.7f} [s]".format(ePython))


"""
PYTHON BOUND C++ APPROACH
"""
t0 = time.perf_counter()
print(primes.nth_prime(N))
t1 = time.perf_counter()
eCpp = t1 - t0
print("Time: {0:.7f} [s]".format(eCpp))


"""
PERFORMANCE DIFFERENCE
"""
print("Factor: {0:.2f}x".format(ePython / eCpp))
