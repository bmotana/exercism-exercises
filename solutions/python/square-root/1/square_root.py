"""
This module provides a simple function to calculate the square root of a given number.

The function:
- square_root: Computes the square root of a number using the exponentiation operator.
"""

def square_root(number: int) -> float:
    """
    Calculates the square root of a given number.

    Args:
    - number (int): The number for which to calculate the square root.

    Returns:
    - float: The square root of the input number.
    """
    # Calculate and return the square root using exponentiation
    return number ** 0.5