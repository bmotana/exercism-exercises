"""
Module for prime factorization using Pollard's Rho algorithm.

This module contains utility functions to factorize large numbers
into their prime factors. It uses Pollard's Rho algorithm for
efficient factorization of composite numbers, even for large primes.
Additionally, it includes helper functions for checking primality
and calculating the greatest common divisor (GCD).
"""

import math
import random
from typing import List

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers.

    The function uses the Euclidean algorithm to find the GCD.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def pollards_rho(n: int) -> int:
    """
    Pollard's Rho algorithm for finding a non-trivial factor of a composite number.

    This function attempts to find a factor of n. If n is even, it returns 2.
    Otherwise, it randomly picks values to find a factor. If a failure occurs,
    it retries with different random values.

    Args:
        n (int): The integer to factorize.

    Returns:
        int: A non-trivial factor of n.
    """
    # Quick check for even numbers
    if n % 2 == 0:
        return 2

    # Random initial values
    x = random.randint(2, n - 1)
    y = x  # Initial y set to x
    c = random.randint(1, n - 1)  # Random constant
    divisor = 1

    # Iterate until a divisor is found
    while divisor == 1:
        # Update x and y with polynomial function
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n  # y moves twice as fast as x

        # Compute gcd of the absolute difference
        divisor = gcd(abs(x - y), n)

        # If failure, retry with different random values
        if divisor == n:
            return pollards_rho(n)
    
    return divisor




def factors(n: int) -> List[int]:
    """
    Recursively factorize a number into its prime factors using Pollard's Rho algorithm.

    Args:
        n (int): The integer to factorize.

    Returns:
        List[int]: A list of prime factors of n.
    """
    # Base case: 1 has no prime factors
    if n == 1:
        return []

    # If the number is prime, return it as the only factor
    if is_prime(n):
        return [n]

    # Use Pollard's Rho to find one non-trivial factor
    factor = pollards_rho(n)

    # Recursively factorize both the factor and the quotient
    return factors(factor) + factors(n // factor)

def is_prime(n: int) -> bool:
    """
    Check whether a given number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

