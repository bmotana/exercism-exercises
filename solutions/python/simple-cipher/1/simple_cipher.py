from random import choice
from string import ascii_lowercase as LETTERS


class Cipher:
    def __init__(self, key: str = None) -> None:
        """
        Initialize the Cipher object with a key.
        If no key is provided, a random key will be generated.

        Args:
            key (str, optional): A string used for encoding/decoding. Defaults to None.
        """
        self.key = key if key else self._generate_random_key()

    def _generate_random_key(self) -> str:
        """
        Generate a random key consisting of a single randomly chosen lowercase letter repeated 10 times.

        Returns:
            str: The generated key.
        """
        return choice(LETTERS) * 10

    def encode(self, plaintext: str) -> str:
        """
        Encode the input text using the Caesar-like cipher with the provided key.

        Args:
            plaintext (str): The text to encode (must contain only lowercase letters).

        Returns:
            str: The encoded string.
        """
        encoded = []
        key_length = len(self.key)

        for i, char in enumerate(plaintext):
            # Get the corresponding key character for this position
            key_char = self.key[i % key_length]
            
            # Get the position of the input character and key character in the alphabet
            text_index = LETTERS.index(char)
            key_index = LETTERS.index(key_char)

            # Perform modular addition to find the encoded character index
            new_index = (text_index + key_index) % 26
            encoded.append(LETTERS[new_index])

        return ''.join(encoded)

    def decode(self, ciphertext: str) -> str:
        """
        Decode the input text using the Caesar-like cipher with the provided key.

        Args:
            ciphertext (str): The encoded text (must contain only lowercase letters).

        Returns:
            str: The decoded (original) string.
        """
        decoded = []
        key_length = len(self.key)

        for i, char in enumerate(ciphertext):
            # Get the corresponding key character for this position
            key_char = self.key[i % key_length]

            # Get the position of the input character and key character in the alphabet
            text_index = LETTERS.index(char)
            key_index = LETTERS.index(key_char)

            # Perform modular subtraction to find the original character index
            new_index = (text_index - key_index) % 26
            decoded.append(LETTERS[new_index])

        return ''.join(decoded)
