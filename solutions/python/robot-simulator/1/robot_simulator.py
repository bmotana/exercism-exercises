# Define directions
NORTH, EAST, SOUTH, WEST = "NORTH", "EAST", "SOUTH", "WEST"
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

class Robot:
    """
    A class representing a robot that can move in a 2D grid.
    """
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """
        Initializes the Robot object.

        Args:
            direction (str, optional): The initial direction of the robot. Defaults to NORTH.
            x_pos (int, optional): The initial x-coordinate of the robot. Defaults to 0.
            y_pos (int, optional): The initial y-coordinate of the robot. Defaults to 0.
        """
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, movement: str):
        """
        Moves the robot based on the given movement string.

        Args:
            movement (str): A string containing movement commands ('R', 'L', 'A').
                'R' turns the robot right, 'L' turns it left, and 'A' advances it.
        """
        for command in movement:
            if command == "R":
                self._turn_right()
            elif command == "L":
                self._turn_left()
            elif command == "A":
                self._advance()

    def _turn_right(self):
        """
        Turns the robot 90 degrees to the right.
        """
        current_index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_index + 1) % 4]

    def _turn_left(self):
        """
        Turns the robot 90 degrees to the left.
        """
        current_index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_index - 1) % 4]

    def _advance(self):
        """
        Moves the robot one unit forward in its current direction.
        """
        x, y = self.coordinates
        if self.direction == NORTH:
            self.coordinates = (x, y + 1)
        elif self.direction == EAST:
            self.coordinates = (x + 1, y)
        elif self.direction == SOUTH:
            self.coordinates = (x, y - 1)
        elif self.direction == WEST:
            self.coordinates = (x - 1, y)