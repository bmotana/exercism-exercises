from collections import defaultdict
from typing import Dict

def transform(legacy_data: Dict[int, list[str]]) -> Dict[str, int]:
    """
    Transform a dictionary with keys as numbers and values as lists of characters
    into a new dictionary with lowercase characters as keys and their corresponding
    numbers as values.

    Args:
        legacy_data (Dict[int, list[str]]): A dictionary where keys are integers
            and values are lists of characters.

    Returns:
        Dict[str, int]: A dictionary where keys are lowercase characters and
            values are the corresponding numbers from the input dictionary.

    Example:
        >>> transform({1: ['A', 'B'], 2: ['C', 'D']})
        {'a': 1, 'b': 1, 'c': 2, 'd': 2}
    """
    if not legacy_data:
        return {}

    formatted_data = defaultdict(list)
    for num, letters in legacy_data.items():
        for letter in letters:
            formatted_data[letter.lower()].append(num)

    return {k: v[0] for k, v in formatted_data.items()}