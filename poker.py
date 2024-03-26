import itertools
from collections import Counter

def evaluate_hand_strength(hand):
    """
    Function to evaluate the strength of a poker hand.
    Returns a numeric value representing the hand strength.
    """
    # Assign values to card ranks for simplicity
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    # Get counts of each rank and each suit in the hand
    rank_counts = Counter([card[0] for card in hand])
    suit_counts = Counter([card[1] for card in hand])
    sorted_ranks = sorted([card_values[card[0]] for card in hand])
    
    # Check for flush and straight possibilities
    is_flush = len(suit_counts) == 1
    is_straight = all(sorted_ranks[i] == sorted_ranks[0] + i for i in range(1, len(hand)))
    
    # Check for specific poker hands
    if is_flush and is_straight:
        # Royal Flush
        if sorted_ranks[-1] == 14:
            return 100
        # Straight Flush
        return 90 + sorted_ranks[-1]
    
    # Four of a Kind
    for rank, count in rank_counts.items():
        if count == 4:
            return 80 + card_values[rank]
    
    # Full House
    if sorted(rank_counts.values()) == [2, 3]:
        return 70 + card_values[max(rank_counts, key=rank_counts.get)]
    
    # Flush
    if is_flush:
        return 60 + max(sorted_ranks)
    
    # Straight
    if is_straight:
        return 50 + sorted_ranks[-1]
    
    # Three of a Kind
    for rank, count in rank_counts.items():
        if count == 3:
            return 40 + card_values[rank]
    
    # Two Pair
    if sorted(rank_counts.values()) == [1, 2, 2]:
        pairs = [rank for rank, count in rank_counts.items() if count == 2]
        return 30 + max(card_values[pairs[0]], card_values[pairs[1]])
    
    # One Pair
    if 2 in rank_counts.values():
        pair_rank = max(rank_counts, key=rank_counts.get)
        return 20 + card_values[pair_rank]
    
    # High Card
    return max(sorted_ranks)
