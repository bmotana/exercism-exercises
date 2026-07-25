def is_valid(isbn):
       # Clean the ISBN by removing non-alphanumeric characters
    processed_isbn = [char for char in isbn if char.isdigit() or char.isalpha()]

    # Check if the length of processed ISBN is not equal to 10 and check
    # If 'X' is present, it should be at the last position
    if len(processed_isbn) != 10 or ("X" in processed_isbn and processed_isbn[-1] != "X") :
        return False
        
    # List to store multiplication results
    multiplication_results = []
    weight = 10

    # Iterate over each character in processed ISBN
    for char in processed_isbn:
        # Check if the character is alphabetical
        if char.isalpha():
            # 'X' is only allowed at the end
            if char.lower() != "x":
                return False
            else:
                # If 'X' is encountered, it's considered as 10
                char = "10"
        # Convert the character to integer and multiply with weight
        multiplication_result = int(char) * weight
        multiplication_results.append(multiplication_result)
        weight -= 1

    # Check if the sum of multiplication results is divisible by 11
    return sum(multiplication_results) % 11 == 0