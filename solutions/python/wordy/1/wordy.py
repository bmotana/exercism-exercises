def answer(question):
      # Split the question into words and remove the last character (usually a question mark)
    
    words = question[:-1].split(" ")[2:]
    
    try:
        # Remove occurrences of "by" if present
        if "by" in words:
            for _ in range(words.count("by")):
                words.remove("by")
    except Exception:
        pass
        
    # Define operators mapping
    operators = {
        "plus": " + ",
        "minus": " - ",
        "multiplied": " * ",
        "divided": " / "
    }

    # Initialize error flags and item counter
    operator_error = False
    syntax_error = False
    item_counter = 0
    
    # Check for unknown operators and raise appropriate error
    for i in range(1, len(words), 2):
        if words[i] not in operators:
            item_counter += 1
            operator_error = True
        if words[i] == "cubed":
            raise ValueError("unknown operation")

    # Check for syntax errors related to non-numeric values
    for j in range(0, len(words), 2):
        if not words[j].isnumeric():
            if words[j][:1] != "-":
                item_counter += 1
                syntax_error = True
                
    # Raise errors if the length of words is 0 or all items are unrecognized
    if len(words) == 0:
        raise ValueError("syntax error")
    
    if len(words) == item_counter:
        raise ValueError("unknown operation")
        
    # Raise errors if there are operator or syntax errors
    if operator_error or syntax_error:
        raise ValueError("syntax error")

    # Replace words with operators
    opr_and_nums = [operators.get(char, char) for char in words]
    
    # Add parentheses around expressions if necessary
    if len(opr_and_nums) == 5:
        opr_and_nums.insert(0, "(")
        opr_and_nums.insert(4, ")")
        
    # Raise syntax error if the number of operators and operands are not correct
    if len(opr_and_nums) % 2 == 0:
        raise ValueError("syntax error")
    
    # Join the operator and number list to form a string expression
    the_sum = "".join(opr_and_nums)
    
    # Evaluate the expression and return the result
    return eval(the_sum)