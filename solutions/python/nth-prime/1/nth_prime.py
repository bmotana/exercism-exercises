def gen_primes() -> int:
    """
    Generate an infinite sequence of prime numbers using a memory-efficient
    Sieve of Eratosthenes-like approach.

    Yields:
        int: The next prime number in the sequence.
    """
    # Dictionary to store composites and the list of primes that divide them
    # This allows marking of future composites without excessive memory use.
    composites = {}

    # Initialize the first integer to check for primeness
    candidate = 2

    while True:
        if candidate not in composites:
            # `candidate` is a prime number as it’s not in the composites dictionary.
            yield candidate
            # Mark the square of the candidate as composite with the candidate as a witness.
            composites[candidate * candidate] = [candidate]
        else:
            # `candidate` is composite. Update its witness primes to mark new composites.
            for prime in composites[candidate]:
                # Mark the next multiple of each witness prime as composite.
                composites.setdefault(prime + candidate, []).append(prime)
            # Remove `candidate` from the dictionary as it’s fully processed.
            del composites[candidate]

        # Move to the next integer to check
        candidate += 1


def prime(n: int) -> int:
    """
    Returns the n-th prime number.

    Args:
        n (int): The position (1-indexed) of the desired prime number.

    Returns:
        int: The n-th prime number.

    Raises:
        ValueError: If n is zero, as there is no zeroth prime.
    """
    if n <= 0:
        raise ValueError('there is no zeroth prime')

    # Create a generator for prime numbers
    prime_generator = gen_primes()

    # Extract the n-th prime number by iterating n times
    prime_number = 0
    for _ in range(n):
        prime_number = next(prime_generator)

    return prime_number
