def reverse(text: str) -> str:
    """
    Reverse the input string.

    Args:
        text (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    # Using slicing to reverse the string
    reversed_str = text[::-1]
    
    # Return the reversed string
    return reversed_str
