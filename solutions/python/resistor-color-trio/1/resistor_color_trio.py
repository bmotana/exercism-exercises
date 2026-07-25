# Define a dictionary with color names as keys and their corresponding indices as values
color_indices = {
    color: str(index) 
    for index, color in enumerate(["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"])
}

def label(colors):
    """
    Calculates the resistance value based on the color bands provided.

    Args:
    - colors (list of str): A list containing color names representing the bands of a resistor.

    Returns:
    - str: A string representing the resistance value with appropriate units.
    """
    # Extract the indices of the first two colors and the multiplier
    indices = [color_indices.get(color) for color in colors[:2]]  # Get indices of the first two colors
    multiplier = "0" * int(color_indices.get(colors[2]))          # Get multiplier and convert to string
    
    # Combine indices and multiplier to form the resistance value
    resistance_value = int("".join(indices + [multiplier]))
    
    if resistance_value == 0:
        return "0 ohms"
    
    # Convert resistance value to string and determine the appropriate unit based on the number of digits
    resistance_str = str(resistance_value)
    num_digits = len(resistance_str)
    
    if num_digits >= 11:
        return f"{resistance_str[:-9]} gigaohms"
    elif num_digits >= 8:
        return f"{resistance_str[:-6]} megaohms"
    elif num_digits >= 4:
        return f"{resistance_str[:-3]} kiloohms"
    else:
        return f"{resistance_str} ohms"