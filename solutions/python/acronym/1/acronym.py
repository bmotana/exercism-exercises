from typing import List

def clean_text(text: str) -> str:
    """
    Helper function to clean and standardize input text by replacing specific
    characters with spaces.
    
    Args:
        text (str): Input text to be cleaned.
        
    Returns:
        str: Cleaned text with standardized spacing.
    """
    # Define characters to be replaced with spaces
    replacements = {
        "-": " ",
        "_": " "
    }
    
    # Apply replacements
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

def get_initials(words: List[str]) -> str:
    """
    Helper function to extract initials from a list of words.
    
    Args:
        words (List[str]): List of words to extract initials from.
        
    Returns:
        str: Concatenated string of initials.
    """
    return "".join(word[0] for word in words if word)

def abbreviate(text: str) -> str:
    """
    Creates an abbreviation from a given text string by taking the first letter
    of each word. Handles hyphenated words and underscore-separated words by
    treating them as separate words.
    
    Args:
        text (str): Input string to be abbreviated.
        
    Returns:
        str: Abbreviated string containing the first letter of each word.
        
    Example:
        >>> abbreviate("Hello World")
        "HW"
        >>> abbreviate("Hello-World")
        "HW"
        >>> abbreviate("Hello_World")
        "HW"
    """
    # Convert text to title case
    text = text.title()
    
    # Clean the text by standardizing separators
    cleaned_text = clean_text(text)
    
    # Split into words and extract initials
    words = cleaned_text.split()
    return get_initials(words)