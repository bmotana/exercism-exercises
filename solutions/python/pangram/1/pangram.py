import string

def is_pangram(sentence: str) -> bool:
    """
    Check if a given sentence is a pangram.

    Pangram: A sentence containing every letter of the alphabet at least once.

    Args:
    - sentence (str): The input sentence to check.

    Returns:
    - bool: True if the sentence is a pangram, False otherwise.
    """

    # Convert the sentence to lowercase and filter out non-alphabetic characters
    sentence_letters = set(letter for letter in sentence.lower() if letter.isalpha())

    # Check if all lowercase alphabets are present in the sentence
    return set(string.ascii_lowercase).issubset(sentence_letters)
