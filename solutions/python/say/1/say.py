"""
Module for converting an integer to its word representation.

This module contains utility functions to convert a number (up to 9999_9999_9999) 
into its English word equivalent. It supports large numbers with magnitudes such 
as million, billion, trillion, etc.

Functions:
    say(i: int) -> str: Converts an integer to its word form.
"""

# Dictionary mapping numbers 0-19 to their word representation.
ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

# Dictionary mapping tens (20-90) to their word representation.
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'
}

# Dictionary mapping large numbers (illions) to their word representation.
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'
}


def say(number: int) -> str:
    """
    Convert an integer to its word representation.

    Args:
        number (int): The integer to convert, must be between 0 and 9999_9999_9999.

    Returns:
        str: The word representation of the integer.

    Raises:
        ValueError: If the input number is negative or exceeds the limit.
    """
    if number > 9999_9999_9999 or number < 0:
        raise ValueError("input out of range")
    
    if number == 0:
        return 'zero'

    # For positive numbers, proceed with converting to words.
    return _say_number_pos(number)


def _say_number_pos(number: int) -> str:
    """
    Convert a positive integer to its word representation (helper function).

    Args:
        number (int): The integer to convert (must be positive).

    Returns:
        str: The word representation of the number.
    """
    if number < 20:
        return ones[number]
    if number < 100:
        # Handle two-digit numbers using the tens dictionary.
        return _join(tens[number // 10], ones[number % 10], use_hyphen=True)
    if number < 1000:
        # Handle three-digit numbers by dividing into hundreds.
        return _divide(number, 100, 'hundred')
    
    # Handle larger numbers (thousands, millions, billions, etc.)
    for illions_index, illions_name in illions.items():
        if number < 1000 ** (illions_index + 1):
            break

    return _divide(number, 1000 ** illions_index, illions_name)


def _divide(dividend: int, divisor: int, magnitude: str) -> str:
    """
    Helper function to handle division of large numbers and convert them to words.

    Args:
        dividend (int): The number to be divided.
        divisor (int): The divisor, such as 100 (hundred), 1000 (thousand), etc.
        magnitude (str): The word corresponding to the magnitude (e.g., 'hundred', 'thousand').

    Returns:
        str: The word representation of the dividend.
    """
    return _join(
        _say_number_pos(dividend // divisor),  # Part before the magnitude
        magnitude,  # Magnitude (e.g., 'hundred', 'thousand')
        _say_number_pos(dividend % divisor)  # Part after the magnitude
    )


def _join(*args: str, use_hyphen: bool = False) -> str:
    """
    Helper function to join words into a single string.

    Args:
        *args (str): Strings to join.
        use_hyphen (bool): If True, join with a hyphen, otherwise with a space.

    Returns:
        str: Joined string.
    """
    # Filter out any empty strings before joining.
    if use_hyphen:
        return '-'.join(filter(bool, args))
    return ' '.join(filter(bool, args))



