from typing import Union



def flatten(nested_list: list) -> list:
    """
    Flattens a nested list of integers into a single list of integers.

    Args:
        nested_list (list): A nested list of integers.

    Returns:
        list: A single flattened list of integers.

    Examples:
        >>> flatten([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
    """
    flattened_list = []

    for item in nested_list:
        # Handle each item in the nested list
        flatten_limited(item, flattened_list)

    return flattened_list


def flatten_limited(item: list, flattened_list: list, max_depth: int = 1) -> None:
    """
    Flattens a nested list up to a specified depth.

    Args:
        item (list): The item to be handled (either a list or an integer).
        flattened_list (list): The list to append the flattened items to.
        max_depth (int, optional): The maximum depth to flatten. Defaults to 1.

    Examples:
        >>> flattened = []
        >>> flatten_limited([1, [2, 3], [4, [5, 6]]], flattened, max_depth=1)
        >>> flattened
        [1, 2, 3, 4, [5, 6]]
    """
    if max_depth <= 0 or not isinstance(item, list):
        flattened_list.append(item)
    else:
        for subitem in item:
            flatten_limited(subitem, flattened_list, max_depth - 1)


def append(list1: list, list2: list) -> list:
    """
    Given two lists, add all items in the second list to the end of the first list.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: The combined list.
    """
    return list1 + list2


def concat(lists: list) -> list:
    """
    Given a series of lists, combine all items in all lists into one flattened list.

    Args:
        lists (list): A list of lists.

    Returns:
        list: A single flattened list of items.
    """
    return flatten(lists)


def filter(predicate, lst: list) -> list:
    """
    Given a predicate and a list, return the list of all items for which predicate(item) is True.

    Args:
        predicate (function): The predicate function.
        lst (list): The input list.

    Returns:
        list: A new list containing items for which the predicate is True.
    """
    return [item for item in lst if predicate(item)]


def length(lst: list) -> int:
    """
    Returns the length of the list.

    Args:
        lst (list): The input list.

    Returns:
        int: The length of the list.
    """
    return len(lst)


def map(function, lst: list) -> list:
    """
    Given a function and a list, return the list of the results of applying function(item) on all items.

    Args:
        function (function): The function to apply.
        lst (list): The input list.

    Returns:
        list: A list of the results of applying the function to each item.
    """
    return [function(item) for item in lst]


def foldl(function, lst: list, initial: Union[int, float]) -> Union[int, float]:
    """
    Given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the left.

    Args:
        function (function): The function to apply.
        lst (list): The input list.
        initial (Union[int, float]): The initial accumulator value.

    Returns:
        Union[int, float]: The result of the reduction.
    """
    acc = initial
    for el in lst:
        acc = function(acc, el)
    return acc


def foldr(function, lst: list, initial: Union[int, float]) -> Union[int, float]:
    """
    Given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right.

    Args:
        function (function): The function to apply.
        lst (list): The input list.
        initial (Union[int, float]): The initial accumulator value.

    Returns:
        Union[int, float]: The result of the reduction.
    """
    acc = initial
    for el in reverse(lst):
        acc = function(acc, el)
    return acc


def reverse(lst: list) -> list:
    """
    Given a list, return a list with all the original items in reversed order.

    Args:
        lst (list): The input list.

    Returns:
        list: The reversed list.
    """
    return lst[::-1]