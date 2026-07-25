import re

VOWELS = "AEIOUaeiou"

def find_initial_consonant_index(word: str) -> int:
    """
    Find the index of the first vowel in the given word.
    If the word starts with a vowel, return 0.
    If the word contains only consonants, return the length of the word.
    """
    for index, letter in enumerate(word):
        if letter in VOWELS:
            return index
    return len(word)

def starts_with(prefix: str, word: str) -> bool:
    """
    Check if the given word starts with the specified prefix.
    """
    return word.startswith(prefix)

def has_consonant_before_vowel(letter: str, word: str) -> bool:
    """
    Check if the given letter appears before the first vowel in the word.
    """
    consonant_end = find_initial_consonant_index(word)
    if letter in word:
        letter_position = word.find(letter)
        return letter_position < consonant_end
    return False

def translate_word(word: str) -> str:
    """
    Translate the given word according to the Pig Latin rules.
    """
    consonant_index = find_initial_consonant_index(word)

    # Rule 3: Words that start with consonant clusters of "qu"
    if has_consonant_before_vowel("qu", word):
        qu_index = word.find("qu")
        return word[qu_index + 2:] + word[:qu_index + 2] + "ay"

    # Rule 1: Words that start with a vowel or "xr" or "yt"
    if consonant_index == 0 or starts_with("xr", word) or starts_with("yt", word):
        return word + "ay"

    # Rule 4: Words that start with "y" followed by a consonant
    if has_consonant_before_vowel("y", word):
        y_index = word.find("y")
        if y_index == 0:
            y_index += 1
        return word[y_index:] + word[:y_index] + "ay"

    # Rule 2: Words that start with one or more consonants
    return word[consonant_index:] + word[:consonant_index] + "ay"

def translate(text: str) -> str:
    """
    Translate the given text by applying the Pig Latin rules to each word.
    """
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return " ".join(translated_words)
