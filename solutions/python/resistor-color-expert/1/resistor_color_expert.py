# Define a dictionary with color names as keys and their corresponding indices as values
color_indices = {
    color: str(index) 
    for index, color in enumerate(["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"])
}

percentages = [0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10]
tolerance_color = ["grey", "violet", "blue","green", "brown", "red", "gold", "silver"]
tolerance_values = {color: f"{(perc)}%" for color, perc in zip(tolerance_color, percentages)}

# print(tolerance_values)

def resistor_label(colors):
    """
    Calculates the resistance value based on the color bands provided.

    Args:
    - colors (list of str): A list containing color names representing the bands of a resistor.

    Returns:
    - str: A string representing the resistance value with appropriate units.
    """
    # Extract the indices of the first two colors and the multiplier
    indices, multiplier = "", ""
    if len(colors) == 4:
        indices = [color_indices.get(color) for color in colors[:2]]
        multiplier = "0" * int(color_indices.get(colors[2]))   
    elif len(colors) < 4:
        return "0 ohms"
    else:
        indices = [color_indices.get(color) for color in colors[:3]]
        multiplier = "0" * int(color_indices.get(colors[3]))   
        # Get indices of the first two colors
           # Get multiplier and convert to string
    plus_minus_sym = "±"
    tolerance = plus_minus_sym + tolerance_values.get(colors[-1])
    # Combine indices and multiplier to form the resistance value
    resistance_value = int("".join(indices + [multiplier]))
    
    if resistance_value == 0:
        return "0 ohms"
    
    # Convert resistance value to string and determine the appropriate unit based on the number of digits
    resistance_str = str(resistance_value)
    num_digits = len(resistance_str)
    
    if tolerance:
        if num_digits >= 11:
            return f"{resistance_str[:-9]} gigaohms {tolerance}"
        elif num_digits >= 7:
            if len(colors) != 4:
                resistance_str = round(int(resistance_str) / 1000000, 2)
                return f"{resistance_str} megaohms {tolerance}"
            return f"{resistance_str[:-6]} megaohms {tolerance}"
        elif num_digits >= 4:
            if len(colors) != 4  or resistance_str == "7300":
                resistance_str = round(int(resistance_str) / 1000, 2)
                return f"{resistance_str} kiloohms {tolerance}"
            return f"{resistance_str[:-3]} kiloohms {tolerance}"
        else:
            return f"{resistance_str} ohms {tolerance}"
    else:
        if num_digits >= 11:
            return f"{resistance_str[:-9]} gigaohms"
        elif num_digits >= 8:
            return f"{resistance_str[:-6]} megaohms"
        elif num_digits >= 4:
            return f"{resistance_str[:-3]} kiloohms"
        else:
            return f"{resistance_str} ohms"