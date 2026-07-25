"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def are_lists_ordered(list1, list2):
    if not list1 or not list2:
        return True
    fst_num: str =  list1[0]
    print(fst_num)
    start_ind = list2.index(fst_num)
    print(start_ind)
    new_list2 = list2[start_ind:]
    for x, y in enumerate(list1):
        try:
            if list1[x] != new_list2[x]:
                print("yes")
                return False
        except IndexError:
            return False
    return True
        
    
   
def is_sublist(smaller, larger):
    """Check if 'smaller' list is a sublist of 'larger' list."""
    len_smaller = len(smaller)
    len_larger = len(larger)

    # Check every possible slice of the larger list that could match the smaller list
    for i in range(len_larger - len_smaller + 1):
        if larger[i:i + len_smaller] == smaller:
            return True
    return False

def sublist(list_a, list_b):
    """
    Compare two lists and determine if one is a sublist, superlist, or equal.
    
    Args:
        list_a (list): The first list to compare.
        list_b (list): The second list to compare.
    
    Returns:
        str: One of the following - "equal", "sublist", "superlist", or "unequal".
    """
    if list_a == list_b:
        return EQUAL
    
    if is_sublist(list_a, list_b):
        return SUBLIST
    
    if is_sublist(list_b, list_a):
        return SUPERLIST
    
    return UNEQUAL


