from typing import List, Optional

def slices(series: str, slice_length: int) -> Optional[List[str]]:
    """
    Generates all possible consecutive substrings (slices) of the specified length from the input series.

    Args:
        series (str): The input string from which slices are to be created.
        slice_length (int): The length of each substring slice.

    Returns:
        Optional[List[str]]: A list of consecutive substrings of the specified length if successful, or None.

    Raises:
        ValueError: If slice_length is zero, negative, greater than the length of series, 
                    or if the series is empty or contains only whitespace.
    """
    # Check if the slice length is zero, negative, or greater than the series length
    if slice_length == 0:
        raise ValueError("slice length cannot be zero")
    if slice_length < 0:
        raise ValueError("slice length cannot be negative")
    if not series.strip():  # Check if the series is empty or contains only whitespace
        raise ValueError("series cannot be empty")
    if slice_length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    # Initialize pointers and result list
    start = 0
    end = slice_length
    result = []

    # Generate slices of specified length
    while end <= len(series):
        result.append(series[start:end])
        start += 1
        end += 1

    return result
