numerals = {"M":1000,  "D":500, "C":100, "L":50, "X":10, "V": 5, "I": 1}

def is_power_of_ten(number: int) -> bool:
    """
    Check if a given number is a power of 10 with an integer exponent.
    """
    if number <= 0:
        return False  # Powers of 10 are positive numbers
    while number > 1:
        if number % 10 != 0:
            return False
        number //= 10
    return True


def roman(number:int) -> str:
    """
    Converts an interger into Roman Numeral String
    
    Arg:
        number (int): the interger you wish to convert to Roman numeral
    
    Returns
        str: Roman Numeral as a string
    """
    result = number
    roman_str = ""
    numeral_list = list(numerals.keys())
    for num ,(letter, value) in enumerate(numerals.items()):
        if (result/value) >= 1:
            res = result//value
            result = result - (res * value)
            roman_str += letter*res
            
        if (is_power_of_ten(value) and value != 1):
            v = int(value -(value * 0.10))
            if result/v >= 1:
                res = result//v
                result = result - (res * v)
                roman_str += numeral_list[num+2] + letter
                
        val = numerals[numeral_list[num-1]]
        if (is_power_of_ten(val) and val != 1):
            x = int(val -(val * 0.60))
            if result/x >= 1:
                res = result//x
                result = result - (res * x)
                roman_str += numeral_list[num+1] + numeral_list[num]
        
        if not result:
            break
    return roman_str