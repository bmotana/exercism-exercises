
def find(search_list, value) -> int:
    """
    Finds the index of the first occurrence of the given value in the provided search list.

    Args:
         search_list (list): The list to search for the value.
        value (Any): The value to search for in the list.

    Returns:
        int: The index of the first occurrence of the value in the list, or raises a ValueError if the value is not found.
    """
    working_list = search_list.copy()
    search_dict = {number: index for index, number, in enumerate(working_list)}
    while working_list:
        list_length = len(working_list)
        middle_index = int(list_length / 2)
        middle_value = working_list[middle_index]
        if middle_value < value:
            working_list = working_list[middle_index + 1:]
        elif middle_value > value:
            working_list = working_list[:middle_index]
        if middle_value == value:
            return search_dict[value]

    raise ValueError("value not in array")
    
