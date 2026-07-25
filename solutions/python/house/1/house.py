def tuple_to_string(tup: tuple, separator='') -> str:
    if len(tup) >= 2:
        return separator.join(map(str, tup))
    else:
        return tup
        
def join_list_to_string(lst, delimiter=' ') -> str:
    """
    Joins elements of a list into a single string with a specified delimiter.

    Parameters:
    lst (list): The list to be joined.
    delimiter (str): The delimiter to separate the list elements.

    Returns:
    str: The joined string.
    """
    return delimiter.join(lst)

phrases = [
        (" the horse and the hound and the horn"),
("that belonged to"," the farmer sowing his corn"),
("that kept"," the rooster that crowed in the morn"),
("that woke"," the priest all shaven and shorn"),
("that married"," the man all tattered and torn"),
("that kissed"," the maiden all forlorn"),
("that milked"," the cow with the crumpled horn"),
("that tossed"," the dog"),
("that worried"," the cat"),
("that killed"," the rat"),
("that ate", " the malt"),
("that lay in", " the house that Jack built.")
    ]


        
def build_verse(start: int) -> list:    
    sen_list = []
    reverse_phrases = list(reversed(phrases))
    for i in range(start):
        if i == start - 1:
            if i == 11:
                reverse_phrases[i] = f"This is{reverse_phrases[i]}"
            else:
                reverse_phrases[i] = f"This is{reverse_phrases[i][1]}"
            sen_list.append(reverse_phrases[i])
            continue
        sen_list.append(tuple_to_string(reverse_phrases[i]))
    return join_list_to_string(list(sen_list[::-1]))


def recite(start_verse: int, end_verse: int) -> list:
    """
  Recites a range of verses from the rhyme.

  Args:
      start_verse (int): The starting verse number (1-based).
      end_verse (int): The ending verse number (1-based).

  Returns:
      list: A list containing the recited verses as strings.
  """
    rhyme_verses = []
    for verse_num in range(start_verse, end_verse + 1):
        rhyme_verses.append(build_verse(verse_num))
    return rhyme_verses

