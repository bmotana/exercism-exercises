def find_anagrams(word, candidates) -> list:
    """
    Find anagrams of a given word from a list of candidates.

    Args:
    - word (str): The input word to find anagrams for.
    - candidates (list of str): A list of candidate words.

    Returns:
    - list of str: A list containing all anagrams of the input word found in the candidates list.
    """
    # Sort the characters of the input word to compare with candidates
    word_sorted = sorted(word.lower())
    
    # Use list comprehension to filter candidates that are anagrams of the input word
    anagrams = [
        candidate for candidate in candidates
        if sorted(candidate.lower()) == word_sorted  # Check if sorted characters match
        and candidate.lower() != word.lower()        # Exclude the input word itself
    ]
    
    return anagrams
