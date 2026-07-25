class Queen:
    """
    Represents a queen on a chessboard with methods to validate position
    and determine if it can attack another queen.
    """

    def __init__(self, row: int, column: int):
        """
        Initialize a Queen object with its position on the chessboard.

        Args:
            row (int): The row position of the queen (0-7).
            column (int): The column position of the queen (0-7).

        Raises:
            ValueError: If the position is invalid.
        """
        self.row = row
        self.column = column
        self._validate_position()
    
    def _validate_position(self) -> None:
        """
        Validate that the queen's position is within the boundaries of a chessboard.

        Raises:
            ValueError: If the row or column is not on the board or not positive.
        """
        if self.row < 0:
            raise ValueError("row not positive")
        elif self.row > 7:
            raise ValueError("row not on board")
        if self.column < 0:
            raise ValueError("column not positive")
        elif self.column > 7:
            raise ValueError("column not on board")
            
    def can_attack(self, another_queen: 'Queen') -> bool:
        """
        Determine if this queen can attack another queen based on their positions.

        Args:
            other_queen (Queen): Another Queen object to check for an attack.

        Returns:
            bool: True if this queen can attack the other queen, False otherwise.

        Raises:
            ValueError: If both queens are on the same square.
        """
        # Ensure the two queens are not on the same square
        if (self.row, self.column) == (another_queen.row, another_queen.column) :
            raise ValueError("Invalid queen position: both queens in the same square")
            
        # Check if the queens are in the same row, column, or diagonal
        same_row = self.row == another_queen.row
        same_column = self.column == another_queen.column
        same_diagonal = abs(self.row - another_queen.row) == abs(self.column - another_queen.column)

        return same_row or same_column or same_diagonal
        
        


