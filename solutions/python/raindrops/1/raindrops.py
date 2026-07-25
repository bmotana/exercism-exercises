def convert(number):
    """
    Convert a number based on its divisibility by 3, 5, and 7.

    Args:
    - number (int): The input number to be converted.

    Returns:
    - str: The converted string or the original number as a string.
    """
    str_num = ""
    if number % 3 == 0:
        str_num += "Pling"
    if number % 5 == 0:
        str_num += "Plang"
    if number % 7 == 0:
        str_num += "Plong"
    if number % 7 != 0 and number % 5 != 0 and number % 3 != 0:
        return str(number)
    return str_num
