from typing import List
import random


class Character:
    """
    Represents a character in a role-playing game with various ability scores
    and hit points calculated based on those abilities.
    """
    
    def __init__(self) -> None:
        """
        Initialize a new character with randomly generated ability scores
        and calculated hit points.
        """
        self.strength: int = self.ability()
        self.dexterity: int = self.ability()
        self.constitution: int = self.ability()
        self.intelligence: int = self.ability()
        self.wisdom: int = self.ability()
        self.charisma: int = self.ability()
        
        # Calculate initial hit points based on constitution modifier
        self.hitpoints: int = 10 + modifier(self.constitution)
    
    def ability(self) -> int:
        """
        Generate an ability score using the "4d6 drop lowest" method.
        
        This method rolls 4 six-sided dice, drops the lowest roll,
        and returns the sum of the remaining three dice.
        
        Returns:
            int: The calculated ability score (sum of the three highest dice rolls)
        """
        # Roll 4 dice and store the results
        dice_rolls: List[int] = [random.randint(1, 6) for _ in range(4)]
        
        # Sort in descending order and drop the lowest roll
        dice_rolls.sort(reverse=True)
        highest_three_rolls = dice_rolls[:-1]
        
        return sum(highest_three_rolls)


def modifier(ability_score: int) -> int:
    """
    Calculate the ability modifier based on an ability score.
    
    The modifier is calculated as (ability_score - 10) // 2,
    which matches standard RPG rules where a score of 10-11 gives
    a modifier of 0, and every 2 points above or below changes
    the modifier by 1.
    
    Args:
        ability_score (int): The base ability score to calculate modifier from
        
    Returns:
        int: The calculated ability modifier
    """
    return (ability_score - 10) // 2