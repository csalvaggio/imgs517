#pragma once

/**
 * @file primes.h
 * @brief Prime number utility functions (pure C++)
 */

/**
 * @brief Return true if the given value is prime
 *
 * @param value Integer to test
 * @return true if prime, false otherwise
 */
bool is_prime(int value);

/**
 * @brief Return the Nth prime number (1-based indexing)
 *
 * Example:
 *   nth_prime(1) == 2
 *   nth_prime(2) == 3
 *
 * @param N Index of the prime to return (must be >= 1)
 * @return The Nth prime
 * @throws std::invalid_argument if N < 1
 */
int nth_prime(int N);
