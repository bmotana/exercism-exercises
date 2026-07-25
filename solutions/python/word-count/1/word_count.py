import string
from typing import Dict

def remove_apostrophes(word: str) -> str:
    """
    Remove leading and trailing apostrophes from a word.

    Args:
        word (str): The word to process.

    Returns:
        str: The word without leading or trailing apostrophes.
    """
    return word.strip("'")


def count_words(sentence: str) -> Dict[str, int]:
    """
    Count the occurrences of each word in a given sentence.

    This function removes punctuation (except apostrophes within words), 
    converts the sentence to lowercase, and returns a dictionary 
    mapping words to their frequencies.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary where keys are words and values are word counts.
    """
    # Replace all punctuation (except apostrophes) with spaces
    for punctuation in string.punctuation.replace("'", ""):
        sentence = sentence.replace(punctuation, " ")
    
    # Split the sentence into words, remove empty strings, and process apostrophes
    words = [
        remove_apostrophes(word).lower()
        for word in sentence.split()
        if remove_apostrophes(word).strip()  # Ensure no empty strings
    ]
    
    # Create a dictionary to count word occurrences
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
