from typing import Generator, List

def primes_sieve(limit: int) -> Generator[int, None, None]:
    """
    Generates prime numbers up to a given limit using the Sieve of Eratosthenes.

    Args:
        limit: The upper limit (exclusive) for generating prime numbers.

    Yields:
        Prime numbers less than the limit.
    """
    if limit <= 1:
        return  # No primes less than or equal to 1

    is_prime = [True] * limit  # Initialize a list to track primality of numbers
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for index, prime_candidate in enumerate(is_prime):
        if prime_candidate:
            yield index  # Yield the prime number
            # Mark all multiples of the prime as non-prime
            for multiple in range(index * index, limit, index):
                is_prime[multiple] = False

def primes(limit: int) -> List[int]:
    """
    Returns a list of prime numbers up to a given limit.

    Args:
        limit: The upper limit (inclusive) for generating prime numbers.

    Returns:
        A list of prime numbers less than or equal to the limit.
    """
    prime_list = list(primes_sieve(limit + 1))  # Generate primes up to limit + 1
    return prime_list
