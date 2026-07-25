"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    number_list = [number, number+1, number+2]
    return number_list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    con_list = rounds_1 + rounds_2
    return con_list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    average = sum(hand)/len(hand)
    return average


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    actual_avg = card_average(hand)
    first_last_avg = (hand[-1] + hand[0])/2
    number_of_cards = len(hand)
    
    if number_of_cards % 2 == 1:
        middle_card = hand[number_of_cards // 2]
    else:
        middle_card = (hand[number_of_cards // 2 - 1] + hand[number_of_cards // 2]) / 2

    if actual_avg in (middle_card ,first_last_avg):
        return True
    return False
    # You need test this before moving on


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_cards = hand[1::2]
    odd_cards = hand[::2]
    
    avg_evn_card = card_average(even_cards)
    avg_odd_card = card_average(odd_cards)
    
    return avg_evn_card == avg_odd_card


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand