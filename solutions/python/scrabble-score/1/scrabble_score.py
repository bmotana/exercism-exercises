# Dictionary mapping Scrabble letter point values
LETTER_POINT_VALUES = {
    1: set('AEIOULNRST'),
    2: set('DG'),
    3: set('BCMP'),
    4: set('FHVWY'),
    5: set('K'),
    8: set('JX'),
    10: set('QZ')
}

def score(word: str) -> int:
    """
    Calculate the Scrabble score for a given word.

    Args:
        word (str): The word to score.

    Returns:
        int: The total Scrabble score for the word.

    Examples:
        >>> score('PYTHON')
        16
        >>> score('cabbage')
        14
    """
    # Convert the word to uppercase for consistent scoring
    word = word.upper()

    # Calculate the total score by summing point values for each letter
    return sum(
        point for point, letters in LETTER_POINT_VALUES.items()
        for letter in word if letter in letters
    )