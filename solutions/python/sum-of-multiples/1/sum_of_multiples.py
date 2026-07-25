def sum_of_multiples(limit: int, multiples: list) -> int:
    """
    Calculate the sum of all unique multiples of given numbers up to a specified limit.

    Args:
    - limit (int): The upper limit (non-inclusive) for calculating multiples.
    - multiples (list): A list of integers to find multiples of.

    Returns:
    - int: The sum of all unique multiples of the given numbers below the limit.
    """
    # Use a set comprehension to collect all unique multiples
    unique_multiples = {
        i 
        for multiple in multiples if multiple != 0  # Ensure multiple is not zero to avoid infinite loops
        for i in range(multiple, limit, multiple)   # Generate multiples of 'multiple' up to 'limit'
    }
    
    # Return the sum of all unique multiples
    return sum(unique_multiples)
    

