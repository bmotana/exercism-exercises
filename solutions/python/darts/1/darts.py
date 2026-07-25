import math

def score(x_coordinate: float, y_coordinate: float) -> int:
    """
    Calculate the score based on the distance from the origin (0, 0).

    Args:
    - x_coordinate (float): The x-coordinate of the point.
    - y_coordinate (float): The y-coordinate of the point.

    Returns:
    - int: The calculated score.
    """

    # Calculate the distance between (x, y) and the origin (0, 0)
    distance_from_origin = math.sqrt(x_coordinate**2 + y_coordinate**2)

    # Assign points based on the distance ranges
    if distance_from_origin > 10:
        # Out of the target area
        points = 0
    elif 5 < distance_from_origin <= 10:
        # Outer circle
        points = 1
    elif 1 < distance_from_origin <= 5:
        # Middle circle
        points = 5
    elif distance_from_origin <= 1:
        # Inner circle
        points = 10

    return points

