def square(number):
    # Check if the number is within the valid range
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    # Calculate the number of grains on the 'number'th square of a chessboard
    return 2 ** (number - 1)


def total():
    total_grains = 0
    
    # Loop through all squares on the chessboard
    for i in range(1, 65):
        # Calculate the number of grains on the current square
        number_grains = square(i)
        # Add the grains on this square to the total
        total_grains += number_grains
    
    return total_grains

