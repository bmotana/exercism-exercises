import string
import random


class Robot:
    """
    A class to represent a Robot with a unique name.

    The robot's name is a combination of 2 uppercase letters followed by 3 unique digits.
    """
    random.seed(1)
    def __init__(self) -> None:
        """
        Initializes a Robot instance with a unique name.
        """
        # Seed the random generator for deterministic behavior (optional)
        
        self.name = self._generate_name()

    def _generate_name(self) -> str:
        """
        Generates a unique robot name consisting of 2 uppercase letters
        and 3 unique digits.

        Returns:
            str: A string representing the robot's name.
        """
        # Generate 3 unique random digits
        unique_digits = random.sample(string.digits, 3)

        # Generate 2 unique random uppercase letters
        unique_letters = random.sample(string.ascii_uppercase, 2)

        # Combine letters and digits into a single name
        return "".join(unique_letters + unique_digits)

    def reset(self) -> None:
        """
        Resets the robot's name by reseeding the random generator and 
        generating a new unique name.
        """
        # Reset the random seed to system-level randomness
        random.seed(None)

        # Assign a new name to the robot
        self.name = self._generate_name()
