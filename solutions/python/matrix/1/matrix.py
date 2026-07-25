from typing import List


class Matrix:
    """
    A class to represent a matrix from a string input.

    Attributes:
        matrix_data (List[List[int]]): The matrix represented as a nested list of integers.
    """

    def __init__(self, matrix_string: str) -> None:
        """
        Initialize a new Matrix instance.

        Args:
            matrix_string (str): A string representation of the matrix,
                                 where rows are separated by newline characters
                                 and elements in a row are separated by spaces.
        """
        # Split the string by newlines to get rows, then split each row into integers
        self.matrix_data: List[List[int]] = [
            list(map(int, row.split()))
            for row in matrix_string.strip().split('\n')
        ]

    def row(self, index: int) -> List[int]:
        """
        Get a specific row from the matrix.

        Args:
            index (int): The 1-based row index to retrieve.

        Returns:
            List[int]: The list of integers in the specified row.
        """
        return self.matrix_data[index - 1]

    def column(self, index: int) -> List[int]:
        """
        Get a specific column from the matrix.

        Args:
            index (int): The 1-based column index to retrieve.

        Returns:
            List[int]: The list of integers in the specified column.
        """
        return [row[index - 1] for row in self.matrix_data]

