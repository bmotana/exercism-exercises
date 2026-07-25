"""
Module that generates verses for the 'Green Bottles' song.
"""

from typing import List

# List of number words from One to Ten
NUMBER_WORDS = [
    "One", "Two", "Three", "Four", "Five",
    "Six", "Seven", "Eight", "Nine", "Ten"
]


def add_verse_line(number_word: str) -> List[str]:
    """
    Generate a verse of the 'Green Bottles' song for a given number word.

    Args:
        number_word (str): The word form of a number (e.g., "Three").

    Returns:
        List[str]: A list of 4 lines representing the verse.
    """
    index = NUMBER_WORDS.index(number_word)

    # When more than two bottles
    if index > 1:
        return [
            f"{number_word} green bottles hanging on the wall,",
            f"{number_word} green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {NUMBER_WORDS[index - 1].lower()} green bottles hanging on the wall."
        ]

    # When exactly two bottles (next will be singular)
    elif index == 1:
        return [
            f"{number_word} green bottles hanging on the wall,",
            f"{number_word} green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {NUMBER_WORDS[index - 1].lower()} green bottle hanging on the wall."
        ]

    # When only one bottle (next will be "no green bottles")
    else:
        return [
            f"{number_word} green bottle hanging on the wall,",
            f"{number_word} green bottle hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be no green bottles hanging on the wall."
        ]


def recite(start: int, take: int = 1) -> List[str]:
    """
    Generate multiple verses of the 'Green Bottles' song.

    Args:
        start (int): Starting number of green bottles (1-based index).
        take (int, optional): How many verses to recite. Defaults to 1.

    Returns:
        List[str]: List of all lines for the selected verses, including spacing.
    """
    song = []

    # Get the list of number words to use in reverse order for recitation
    chosen_numbers = NUMBER_WORDS[start - take:start][::-1]

    for i, number_word in enumerate(chosen_numbers):
        song.extend(add_verse_line(number_word))
        # Add a blank line between verses, except after the last one
        if i < len(chosen_numbers) - 1:
            song.append("")

    return song


    
