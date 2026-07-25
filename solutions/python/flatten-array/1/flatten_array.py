def flatten(nested_list: list) -> list:
    """
    Flattens a nested list of integers into a single list of integers.

    Args:
    - nested_list (list): A nested list of integers.

    Returns:
    - list: A single flattened list of integers.
    """
    flattened_list = []
    
    for item in nested_list:
        # Handle each item in the nested list
        handle_item(item, flattened_list)
        
    return flattened_list

def handle_item(item, flattened_list: list) -> None:
    """
    Handles each item in the nested list, either by flattening it further if it's a list
    or appending it to the flattened list if it's an integer.

    Args:
    - item: The item to be handled (either a list or an integer).
    - flattened_list (list): The list to append the flattened items to.
    """
    if isinstance(item, list):
        # Recursively flatten the nested list
        deeper_list = flatten(item)
        flattened_list.extend(deeper_list)
    elif isinstance(item, int):
        # Append integer items directly to the flattened list
        flattened_list.append(item)

