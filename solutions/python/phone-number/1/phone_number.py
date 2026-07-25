import string

class PhoneNumber:
    """
    A class to represent and validate a phone number.

    Attributes:
        number (str): The processed phone number (digits only).
        area_code (str): The area code extracted from the phone number.
    """

    def __init__(self, number: str):
        """
        Initialize a PhoneNumber instance, process the input number, and extract the area code.

        Args:
            number (str): The raw phone number provided as input.
        """
        self.raw_number = number  # Preserve the raw input for debugging if needed.
        self.number = self._process_number()
        self.area_code = self.number[:3]  # First three digits are the area code.
    
    def _process_number(self) -> str:
        """
        Process the raw phone number to ensure it is valid and extract the numeric digits.

        Returns:
            str: A sanitized and validated phone number containing only digits.
        """
        self._validate_characters(self.raw_number)
        digits_only = "".join(char for char in self.raw_number if char in string.digits)
        sanitized_number = self._validate_length_and_prefix(digits_only)
        self._validate_area_and_exchange_codes(sanitized_number)
        return sanitized_number 
        
    def _validate_length_and_prefix(self, number: str) -> str:
        """
        Validate the length of the phone number and handle optional leading '1'.

        Args:
            number (str): The phone number with digits only.

        Returns:
            str: A sanitized phone number without a leading '1'.

        Raises:
            ValueError: If the phone number is invalid in length or format.
        """
        if len(number) == 11 and number[0] == "1":
            return number[1:]  # Remove the leading '1'.
        elif len(number) == 11:
            raise ValueError("11 digits must start with 1")
        elif len(number) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        else:
            return number
    
    def _validate_characters(self, number: str) -> None:
        """
        Ensure the phone number does not contain invalid characters like letters or certain punctuations.

        Args:
            number (str): The raw phone number to validate.

        Raises:
            ValueError: If letters or invalid punctuations are found.
        """
        for char in number:
            if char.isalpha():
                raise ValueError("letters not permitted")
            if char in set(string.punctuation).difference({"+", "-", ".", "(", ")"}):
                raise ValueError("punctuations not permitted")
                
                
    def _validate_area_and_exchange_codes(self, number: str) -> None:
        """
        Validate the area and exchange codes in the phone number.

        Args:
            number (str): The sanitized phone number.

        Raises:
            ValueError: If the area or exchange code starts with invalid digits.
        """
        area_code_start = number[0]
        exchange_code_start = number[3]
        if area_code_start == "0":
            raise ValueError("area code cannot start with zero")
        elif area_code_start == "1":
            raise ValueError("area code cannot start with one")
        elif exchange_code_start == "0":
            raise ValueError("exchange code cannot start with zero")
        elif exchange_code_start == "1":
            raise ValueError("exchange code cannot start with one")

    
    def pretty(self) -> str:
        """
        Return a formatted string representation of the phone number.

        Returns:
            str: The phone number in the format (XXX)-XXX-XXXX.
        """
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
        
    
        