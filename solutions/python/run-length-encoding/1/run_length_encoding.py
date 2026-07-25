def decode(encoded_string: str) -> str:
    """
    Decodes a run-length encoded string.
    
    Args:
        encoded_string (str): The encoded string, where numbers indicate repetitions 
                              of the following character.
    
    Returns:
        str: The decoded string with characters repeated based on the encoded pattern.
    """
    decoded_result = ""   # Final decoded string
    previous_position = 0 # Tracks the position of the last processed character

    # Iterate over the string to identify character-number patterns
    for current_position, character in enumerate(encoded_string):
        if not character.isnumeric():  # Check if the character is not a digit
            next_position = current_position + 1
            segment = encoded_string[previous_position:next_position]

            if len(segment) > 1:
                # Add repeated characters if there's a number before the character
                if segment[:-1].strip():
                    decoded_result += int(segment[:-1]) * segment[-1]
                else:
                    decoded_result += segment[-1]
            else:
                decoded_result += segment

            previous_position = next_position  # Update last processed position
    return decoded_result


def encode(input_string: str) -> str:
    """
    Encodes a string using run-length encoding, where consecutive identical characters 
    are replaced by the character preceded by the count of occurrences.
    
    Args:
        input_string (str): The input string to encode.
    
    Returns:
        str: The run-length encoded string.
    """
    encoded_result = ""    # Final encoded string
    char_sequence = ""     # Tracks the current sequence of identical characters

    # Append a delimiter to ensure the last sequence is processed
    input_string += "."

    # Process each character to group consecutive identical characters
    for char in input_string:
        # Check if char is part of the ongoing sequence
        if char in char_sequence:
            char_sequence += char
        else:
            # Encode the previous sequence if it exists
            if char_sequence:
                if len(char_sequence) > 1:
                    encoded_result += f"{len(char_sequence)}{char_sequence[0]}"
                else:
                    encoded_result += char_sequence[0]
            char_sequence = char  # Start a new sequence

    return encoded_result
