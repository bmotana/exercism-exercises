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


    
""" 
The problem with coding is that you make change and run the code, 
then make a change, and run the code, again and again. is there anyway
to reduce this, or to do this more efficient.end

I find myself constantly going back and forth with code, especially web dev 
related.
 """