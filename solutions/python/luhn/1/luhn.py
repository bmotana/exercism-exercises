import string

class Luhn:
    """
    A class to validate card numbers using the Luhn algorithm.
    """
    
    @staticmethod
    def is_non_empty_string(item: str) -> bool:
        """
        Check if the given item is a non-empty string.
        
        Args:
            item (str): The string to check.
        
        Returns:
            bool: True if the string is non-empty, False otherwise.
        """
        return bool(item.strip())
    
    @staticmethod
    def convert_to_int(item: str) -> int:
        """
        Convert a string to an integer.
        
        Args:
            item (str): The string to convert.
        
        Returns:
            int: The integer representation of the input string.
        """
        return int(item)
    
    def __init__(self, card_number: str):
        """
        Initialize the Luhn validator with a card number.
        
        Args:
            card_number (str): The card number to validate.
        """
        # Remove spaces and split into individual digits
        cleaned_card_num = card_number.replace(" ", "")
        self.card_num = list(filter(self.is_non_empty_string, list(cleaned_card_num)))
    
    @staticmethod
    def check_if_only_digits(digits: list) -> bool:
        """
        Check if all characters in the list are digits or whitespace.
        
        Args:
            digits (list): List of characters to validate.
        
        Returns:
            bool: True if all characters are digits or whitespace, False otherwise.
        """
        return all(char in (string.whitespace + string.digits) for char in digits)
    
    def valid(self) -> bool:
        """
        Validate the card number using the Luhn algorithm.
        
        Returns:
            bool: True if the card number is valid, False otherwise.
        """
        # Check if the card number contains only digits
        if not self.check_if_only_digits(self.card_num):
            return False
        
        # Calculate checksum
        checksum, length = self._calculate_checksum()
        
        # Validate card number
        return length > 1 and checksum % 10 == 0
    
    def _calculate_checksum(self) -> tuple:
        """
        Calculate the checksum for the Luhn algorithm.
        
        Returns:
            tuple: A tuple containing the checksum and the length of the card number.
        """
        # Convert card number to integers
        card_digits = list(map(self.convert_to_int, self.card_num))
        
        # Apply Luhn algorithm
        processed_digits = []
        for index, digit in enumerate(reversed(card_digits), 1):
            if index % 2 == 0:
                # Double every second digit from the right
                doubled_digit = digit * 2
                processed_digits.append(doubled_digit - 9 if doubled_digit > 9 else doubled_digit)
            else:
                processed_digits.append(digit)
        
        # Return checksum and length
        return sum(processed_digits), len(card_digits)