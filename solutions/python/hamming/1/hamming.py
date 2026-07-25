  
def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculates the Hamming distance between two DNA strands of equal length.

    The Hamming distance is the number of positions where the corresponding nucleotides
    are different. This function takes two DNA strands as input and returns the Hamming
    distance between them.

    If the two strands are not of equal length, a ValueError is raised.

    Args:
        strand_a (str): The first DNA strand.
        strand_b (str): The second DNA strand.

    Returns:
        int: The Hamming distance between the two DNA strands.

    Raises:
        ValueError: If the two DNA strands are not of equal length.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(a != b for a, b in zip(strand_a, strand_b))
    
