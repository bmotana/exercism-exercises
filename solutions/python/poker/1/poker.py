from collections import Counter

CARD_RANKS = {
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


def parse_card(card_str: str) -> tuple[int, str]:
    rank_str = card_str[:-1]
    suit = card_str[-1]
    return CARD_RANKS[rank_str], suit


def hand_score(hand_str: str):
    cards = [parse_card(c) for c in hand_str.split()]
    ranks = sorted([r for r, s in cards], reverse=True)
    suits = [s for r, s in cards]
    is_flush = len(set(suits)) == 1

    is_straight = False
    straight_high = 0
    if len(set(ranks)) == 5:
        if ranks[0] - ranks[4] == 4:
            is_straight = True
            straight_high = ranks[0]
        elif ranks == [14, 5, 4, 3, 2]:
            is_straight = True
            straight_high = 5

    counts = Counter(ranks)
    by_freq = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)

    if by_freq[0][1] == 5:
        return (10, [by_freq[0][0]])

    if is_straight and is_flush:
        return (9, [straight_high])

    if by_freq[0][1] == 4:
        return (8, [by_freq[0][0], by_freq[1][0]])

    if by_freq[0][1] == 3 and by_freq[1][1] == 2:
        return (7, [by_freq[0][0], by_freq[1][0]])

    if is_flush:
        return (6, ranks)

    if is_straight:
        return (5, [straight_high])

    if by_freq[0][1] == 3:
        kickers = [r for r, c in by_freq[1:]]
        return (4, [by_freq[0][0]] + kickers)

    if by_freq[0][1] == 2 and by_freq[1][1] == 2:
        pair1 = max(by_freq[0][0], by_freq[1][0])
        pair2 = min(by_freq[0][0], by_freq[1][0])
        kicker = by_freq[2][0]
        return (3, [pair1, pair2, kicker])

    if by_freq[0][1] == 2:
        pair = by_freq[0][0]
        kickers = [r for r, c in by_freq[1:]]
        return (2, [pair] + kickers)

    return (1, ranks)


def best_hands(hands: list[str]) -> list[str]:
    scores = [(hand_score(h), h) for h in hands]
    max_score = max(scores, key=lambda x: x[0])[0]
    return [h for s, h in scores if s == max_score]

