"""
Module for validating bracket pairing in strings.

This module provides functionality to check if brackets in a given string
are correctly paired and nested.
"""

from typing import List, Tuple


def is_paired(input_string: str) -> bool:
    """
    Check if brackets in the input string are correctly paired and nested.

    Args:
        input_string (str): The string to check for paired brackets.

    Returns:
        bool: True if all brackets are correctly paired and nested, False otherwise.
    """
    # Define valid bracket pairs
    BRACKET_PAIRS: List[Tuple[str, str]] = [('[', ']'), ('{', '}'), ('(', ')')]
    
    # Extract only bracket characters from the input string
    cleaned_string: str = ''.join(char for char in input_string 
                                  if char in [b for pair in BRACKET_PAIRS for b in pair])
    
    # Initialize an empty stack to keep track of opening brackets
    stack: List[str] = []
    
    # Create a dictionary for quick lookup of closing brackets
    closing_brackets: dict = {pair[1]: pair[0] for pair in BRACKET_PAIRS}
    
    # Iterate through each character in the cleaned string
    for char in cleaned_string:
        if char in closing_brackets.values():
            # If it's an opening bracket, add it to the stack
            stack.append(char)
        elif char in closing_brackets:
            # If it's a closing bracket
            if not stack or stack.pop() != closing_brackets[char]:
                # If stack is empty or the last opening bracket doesn't match
                return False
    
    # All brackets are paired if the stack is empty
    return len(stack) == 0