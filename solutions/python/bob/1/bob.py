def response(remark):
    """
    Provides a response based on the given remark.

    Args:
    - remark (str): The input remark to be processed.

    Returns:
    - str: The appropriate response based on the input remark.
    """
    # Remove leading and trailing whitespaces from the remark
    cleaned_remark = remark.strip()

    # Check if the cleaned remark is in all uppercase
    if cleaned_remark.isupper():
        # Check if the cleaned remark ends with a question mark
        if cleaned_remark.endswith("?"):
            return "Calm down, I know what I'm doing!"
            # If no question mark, respond with "Whoa, chill out!"
        return "Whoa, chill out!"

        # Check if the cleaned remark ends with a question mark
    elif cleaned_remark.endswith("?"):
        return "Sure."

        # Check if the cleaned remark is empty or consists of only spaces
    elif cleaned_remark.isspace() or cleaned_remark == "":
        return "Fine. Be that way!"

        # Default response if none of the above conditions are met
    else:
        return "Whatever."
