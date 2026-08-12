
def is_armstrong_number(number):
    # Convert number to a string to easily iterate through its digits
    number_str = str(number)
    
    # Calculate the power once instead of multiple times
    power = len(number_str)
    
    # Calculate the result using a generator expression and the sum function
    result = sum(int(digit) ** power for digit in number_str)
    
    # Simplify the return statement
    return number == result