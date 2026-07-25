from typing import List
from collections import Counter

# Score categories
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def count_specific_number(dice: List[int], target: int) -> int:
    """
    Count occurrences of a specific number in dice and multiply by the number.
    
    Args:
        dice: List of integers representing dice values
        target: The number to count and multiply by
        
    Returns:
        int: Score calculated by multiplying count by target number
    """
    return sum(1 for d in dice if d == target) * target


def is_n_of_a_kind(dice: List[int], n: int) -> bool:
    """
    Check if dice contain at least n of any number.
    
    Args:
        dice: List of integers representing dice values
        n: Number of identical dice required
        
    Returns:
        bool: True if condition is met, False otherwise
    """
    return any(count >= n for count in Counter(dice).values())


def score(dice: List[int], category: str) -> int:
    """
    Calculate the score for a given category in Yacht dice game.
    
    Args:
        dice: List of 5 integers between 1 and 6 representing dice values
        category: String representing the scoring category
        
    Returns:
        int: Score for the given category based on dice values
    """
    # Convert dice to sorted tuple for easier comparison
    sorted_dice = tuple(sorted(dice))
    
    # Basic number categories (ones through sixes)
    number_categories = {
        ONES: 1, TWOS: 2, THREES: 3,
        FOURS: 4, FIVES: 5, SIXES: 6
    }
    if category in number_categories:
        return count_specific_number(dice, number_categories[category])
    
    # Special categories
    if category == FULL_HOUSE:
        counts = Counter(dice)
        if len(counts) == 2 and 3 in counts.values():
            return sum(dice)
        return 0
    
    elif category == FOUR_OF_A_KIND:
        if is_n_of_a_kind(dice, 4):
            # Find the number that appears at least 4 times
            number = max(set(dice), key=dice.count)
            return number * 4
        return 0
    
    elif category == LITTLE_STRAIGHT:
        return 30 if sorted_dice == (1, 2, 3, 4, 5) else 0
    
    elif category == BIG_STRAIGHT:
        return 30 if sorted_dice == (2, 3, 4, 5, 6) else 0
    
    elif category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    
    elif category == CHOICE:
        return sum(dice)
    
    return 0  # Return 0 for invalid categories