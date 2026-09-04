"""This is a docstring which returns a message for a restraurant """


def line_up(name: str, number: int) -> str:
    """
    name (str): Name of the customer
    number (int): Order Number

    Return:
    (str): Message with name and order number of the customer
    """
    last_number = int(str(number)[-1])
    suffix = "th"
    if last_number in list(range(1,4)) and str(number)[-2:] not in ["11", "12", "13"]:
        suffix = ["st", "nd", "rd"][last_number-1]
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
