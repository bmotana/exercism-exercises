"""
allergies.py - Allergy Score Processor

This module provides functionality for processing allergy test scores and determining
which specific allergens a person is allergic to based on their allergy score.

The scoring system uses a binary approach where each allergen is assigned a power-of-2 value:
- eggs: 2^0 = 1
- peanuts: 2^1 = 2
- shellfish: 2^2 = 4
- strawberries: 2^3 = 8
- tomatoes: 2^4 = 16
- chocolate: 2^5 = 32
- pollen: 2^6 = 64
- cats: 2^7 = 128

A person's allergy score is the sum of the scores for the allergens they're allergic to.
For example, a person allergic to eggs and shellfish would have a score of 1 + 4 = 5.

Usage:
    allergies = Allergies(5)  # Person allergic to eggs and shellfish
    allergies.lst  # Returns ["eggs", "shellfish"]
    allergies.allergic_to("shellfish")  # Returns True
    allergies.allergic_to("peanuts")  # Returns False
"""
from typing import List


class Allergies:
    """
    A class that represents allergy tests and their scores.
    
    Each allergen has a specific power-of-2 score (eggs=1, peanuts=2, etc.).
    A person's allergy score is the sum of the scores of their allergies.
    """
    
    # List of potential allergens ordered by increasing score (2^0 to 2^7)
    ALLERGENS = [
        "eggs",        # 2^0 = 1
        "peanuts",     # 2^1 = 2
        "shellfish",   # 2^2 = 4
        "strawberries", # 2^3 = 8
        "tomatoes",    # 2^4 = 16
        "chocolate",   # 2^5 = 32
        "pollen",      # 2^6 = 64
        "cats"         # 2^7 = 128
    ]
    
    def __init__(self, score: int) -> None:
        """
        Initialize an Allergies object with the given score.
        
        Args:
            score (int): The allergy score representing allergic reactions.
                         Multiple allergies are represented by the sum of their scores.
        """
        # We only care about the lowest 8 bits of the score
        # as there are only 8 possible allergens
        self.score = score % 256
        
    def allergic_to(self, item: str) -> bool:
        """
        Determine if the person is allergic to a specific item.
        
        Args:
            item (str): The allergen to check for.
        
        Returns:
            bool: True if the person is allergic to the item, False otherwise.
        """
        return item in self.lst
    
    @property
    def lst(self) -> List[str]:
        """
        Generate a list of allergens based on the allergy score.
        
        This property computes which allergens are active based on the binary
        representation of the score, where each bit corresponds to a specific allergen.
        
        Returns:
            List[str]: A list of allergens the person is allergic to.
        """
        allergic_items = []
        
        # Check each allergen by calculating its bit position in the score
        for index, allergen in enumerate(self.ALLERGENS):
            # Calculate the allergen's score (2^index)
            allergen_score = 1 << index
            
            # If the allergen's bit is set in the score, add it to the list
            if self.score & allergen_score:
                allergic_items.append(allergen)
                
        return allergic_items
