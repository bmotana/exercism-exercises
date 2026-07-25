"""Poker hand evaluation module.

Provides functionality to evaluate and rank standard (and custom) poker hands,
determining the best hand(s) from a list of given hands.
"""

from collections import Counter
from enum import IntEnum

# Mapping card rank characters to numerical values
CARD_RANKS: dict[str, int] = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class HandCategory(IntEnum):
    """Hierarchy of poker hand strengths."""

    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    FIVE_OF_A_KIND = 10


def parse_card(card_str: str) -> tuple[int, str]:
    """Parse a card string (e.g., '10S', 'AH') into (rank_value, suit)."""
    return CARD_RANKS[card_str[:-1]], card_str[-1]


def hand_score(hand_str: str) -> tuple[HandCategory, list[int]]:
    """Compute a score tuple (category, tie_breaker_ranks) for a given 5-card hand."""
    cards = [parse_card(card_token) for card_token in hand_str.split()]
    ranks = sorted([rank for rank, card_suit in cards], reverse=True)
    suits = [suit for card_rank, suit in cards]
    is_flush = len(set(suits)) == 1

    # Check for straight condition
    is_straight = False
    straight_high = 0
    if len(set(ranks)) == 5:
        if ranks[0] - ranks[4] == 4:
            is_straight = True
            straight_high = ranks[0]
        elif ranks == [14, 5, 4, 3, 2]:  # Ace-low straight (A-2-3-4-5)
            is_straight = True
            straight_high = 5

    # Group cards by frequency descending, then by rank descending
    counts = Counter(ranks)
    by_freq = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)

    # 10. Five of a Kind
    if by_freq[0][1] == 5:
        return (HandCategory.FIVE_OF_A_KIND, [by_freq[0][0]])

    # 9. Straight Flush
    if is_straight and is_flush:
        return (HandCategory.STRAIGHT_FLUSH, [straight_high])

    # 8. Four of a Kind
    if by_freq[0][1] == 4:
        return (HandCategory.FOUR_OF_A_KIND, [by_freq[0][0], by_freq[1][0]])

    # 7. Full House
    if by_freq[0][1] == 3 and by_freq[1][1] == 2:
        return (HandCategory.FULL_HOUSE, [by_freq[0][0], by_freq[1][0]])

    # 6. Flush
    if is_flush:
        return (HandCategory.FLUSH, ranks)

    # 5. Straight
    if is_straight:
        return (HandCategory.STRAIGHT, [straight_high])

    # 4. Three of a Kind
    if by_freq[0][1] == 3:
        kickers = [rank for rank, count in by_freq[1:]]
        return (HandCategory.THREE_OF_A_KIND, [by_freq[0][0]] + kickers)

    # 3. Two Pair
    if by_freq[0][1] == 2 and by_freq[1][1] == 2:
        pair1 = max(by_freq[0][0], by_freq[1][0])
        pair2 = min(by_freq[0][0], by_freq[1][0])
        kicker = by_freq[2][0]
        return (HandCategory.TWO_PAIR, [pair1, pair2, kicker])

    # 2. One Pair
    if by_freq[0][1] == 2:
        pair = by_freq[0][0]
        kickers = [rank for rank, count in by_freq[1:]]
        return (HandCategory.ONE_PAIR, [pair] + kickers)

    # 1. High Card
    return (HandCategory.HIGH_CARD, ranks)


def best_hands(hands: list[str]) -> list[str]:
    """Return the winning hand(s) from a list of poker hand strings."""
    scored_hands = [(hand_score(hand), hand) for hand in hands]
    max_score = max(scored_hands, key=lambda item: item[0])[0]
    return [hand for score, hand in scored_hands if score == max_score]
