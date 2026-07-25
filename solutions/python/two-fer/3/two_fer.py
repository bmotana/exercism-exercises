"""
This module contains a function `two_fer` that returns a string formatted to share an item with someone.
"""

def two_fer(name: str = "you") -> str:
    """
    Returns a string formatted to share an item with someone (or 'you' if no name is provided).

    Args:
    - name (str): The name of the person to share with. Defaults to "you".

    Returns:
    - str: A string in the format "One for {name}, one for me." or "One for you, one for me." if no name is provided.
    """
    # Format the string with the given name or "you" by default
    return f"One for {name}, one for me."
