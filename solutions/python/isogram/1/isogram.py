def is_isogram(string: str) -> bool:
    """
    Check if a given string is an isogram.
    
    An isogram is a string that does not have any repeating letters.
    
    Args:
        string (str): The input string to check.
        
    Returns:
        bool: True if the string is an isogram, False otherwise.
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = [characters.lower() for characters in string if characters.isalpha()]
    # Convert the string to a set of lowercase letters
    letters_set = set(string)
    # If the length of the set is equal to the length of the string, it's an isogram
    return len(letters_set) == len(string)
