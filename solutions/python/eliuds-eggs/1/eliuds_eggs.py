def egg_count(display_value: int) -> int:
    """
    Determines the minimum number of eggs needed to sum up to `display_value` 
    using powers of 2 (binary representation logic).
    
    Parameters:
        display_value (int): The target number to represent using powers of 2.
    
    Returns:
        int: The minimum count of binary terms (powers of 2) required.
    """
    # List to store powers of 2 (e.g., 1, 2, 4, 8, 16...)
    binary_powers = [1]
    
    # Generate powers of 2 until the last generated number exceeds `display_value`
    power = 1
    while binary_powers[-1] < display_value:
        binary_powers.append(2 ** power)
        power += 1
    
    # Counting the number of binary terms used
    egg_counter = 0

    # Iterate in reverse to prioritize larger powers of 2 first
    for binary_number in reversed(binary_powers):
        if display_value >= binary_number:  # If we can subtract this power of 2
            display_value -= binary_number
            egg_counter += 1

    return egg_counter