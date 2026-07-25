ACTION_MAP = {
    0: "wink",
    1: "double blink",
    2: "close your eyes",
    3: "jump"
}


def commands(binary_str):
    """
    Interprets a binary string and converts it into a list of actions.

    Args:
    - binary_str (str): A string representing a binary number.

    Returns:
    - list: A list of actions based on the binary string.
    """
    binary_str = binary_str[::-1]
    command_list = []
    for i in range(4):
        if binary_str[i] == "1":
            command = ACTION_MAP.get(i)
            command_list.append(command)
    if binary_str[-1] == "1":
        command_list.reverse()
    return command_list
    
