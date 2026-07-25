import string 

LETTERS = string.ascii_uppercase

def rows(letter: str) -> list:
    """
    Returns a Diamond Shape
    
    
    Args:
        letter (str): A letter 
        
    Returns:
        list : a rows of strings that comes together form a diamond
    
    """
    limit = LETTERS.index(letter)
    distance = LETTERS[:limit+1]
    sequence = distance  + distance[::-1][1:]
    diamond_len = len(distance)
    diamond_spaces = [" "for i in range(diamond_len)]
    stack = []
    
    for i, x in enumerate(sequence):
        if i < diamond_len:
            diamond_spaces [i] = x
            diamond_line = diamond_spaces [::-1] + diamond_spaces [1:]
            stack.append(diamond_line)
            diamond_spaces  = [" "for i in range(diamond_len)]
            
    uncleaned_diamond = stack  + stack[::-1][1:]
    diamond = ["".join(row) for row in uncleaned_diamond]
    return diamond
    
    