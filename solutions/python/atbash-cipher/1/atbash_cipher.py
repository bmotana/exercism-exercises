import string 

# Define the plain alphabet and reversed cipher alphabet
plain = string.ascii_lowercase  # Regular alphabet: 'abcdefghijklmnopqrstuvwxyz'
cipher = string.ascii_lowercase[::-1]  # Reversed alphabet: 'zyxwvutsrqponmlkjihgfedcba'

def encode(plain_text: str) -> str:
    """
    Encodes a plain text string using a substitution cipher where each letter is replaced
    with its corresponding letter from a reversed alphabet. The output is formatted with
    spaces every 5 characters.
    
    Args:
        plain_text (str): The text to be encoded. Can contain any characters, but only
                         letters will be encoded. Case-insensitive.
    
    Returns:
        str: The encoded text with the following transformations applied:
             - All letters are substituted with their cipher equivalents
             - All punctuation and whitespace are removed
             - Spaces are inserted every 5 characters
             - Leading and trailing spaces are stripped
    
    Example:
        >>> encode("Hello, World!")
        "svool dligo"
    """
    lowercase_plain_text = plain_text.lower()
    # Create translation table: maps plain alphabet to cipher alphabet and removes punctuation/whitespace
    mytable = str.maketrans(plain, cipher, string.punctuation + string.whitespace)
    new_txt = lowercase_plain_text.translate(mytable)
    chars = [letter if indx % 5 != 0 else f" {letter}"
             for indx, letter in enumerate(new_txt)]
    ciphered_text = "".join(chars).strip()
    return ciphered_text
    
def decode(ciphered_text: str) -> str:
    """
    Decodes a text that was encoded using the encode() function by reversing
    the substitution cipher.
    
    Args:
        ciphered_text (str): The encoded text to be decoded. Expected to contain
                            only letters and spaces.
    
    Returns:
        str: The decoded text with all substituted letters converted back to their
             original form. Spaces are removed during decoding.
    
    Example:
        >>> decode("svool dligo")
        "helloworld"
    """
    # Create translation table: maps cipher alphabet back to plain alphabet and removes spaces
    mytable = str.maketrans(cipher, plain, string.whitespace)
    plain_text = ciphered_text.translate(mytable)
    return plain_text