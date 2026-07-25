import string

def rotate(text: str, key: int) -> str:
    """
    Rotate characters in the text by a given key.

    Args:
        text (str): The text to be rotated.
        key (int): The number of positions to rotate the characters.

    Returns:
        str: The rotated text.
    """
    # Create a translation table to shift characters
    shift = key % 26
    trans_table = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] +
        string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    )
    
    # Return the rotated text using translate
    return text.translate(trans_table)
