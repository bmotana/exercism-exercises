def classify(number: int) -> str:
    """Classify a positive integer based on its divisors sum.

    Args:
        number (int): A positive integer to classify.

    Returns:
        str: The classification of the input integer.
    """
    # Check if the input is a positive integer
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # Initialize a list to store positive divisors
    divisors_list = []

    # Iterate through numbers up to 'number' to find divisors
    for potential_divisor in range(1, number):
        if number % potential_divisor == 0:
            divisors_list.append(potential_divisor)

    # Calculate the sum of divisors
    divisors_sum = sum(divisors_list)

    # Classify the number based on the comparison with its divisors sum
    if number == divisors_sum:
        return "perfect"
    elif number < divisors_sum:
        return "abundant"
    else:
        return "deficient"
