"""
{"game": "holdempot", 
"dealer": 1, 
"num_players": 2, 
"pots": [{"stage": "f", "num_players": 2, "size": 60}, {"stage": "t", "num_players": 2, "size": 180}, {"stage": "r", "num_players": 2, "size": 540}, {"stage": "s", "num_players": 2, "size": 540}], 
"board": ["Ts", "5c", "7h", "8s", "Js"], 
"players": 
[
    {"user": "PoTz", 
        "bets": [{"actions": ["B", "c"], "stage": "p"}, {"actions": ["c"], "stage": "f"}, {"actions": ["c"], "stage": "t"}, {"actions": ["k"], "stage": "r"}], 
        "bankroll": 4877, "action": 270, 
        "winnings": 540, 
        "pocket_cards": ["Qh", "Td"], "pos": 2}, 
    {"user": "__", 
        "bets": [{"actions": ["B", "r"], "stage": "p"}, {"actions": ["b"], "stage": "f"}, {"actions": ["b"], "stage": "t"}, {"actions": ["k"], "stage": "r"}], "bankroll": 47590, 
        "action": 270, 
        "winnings": 0, 
        "pocket_cards": ["6c", "Kh"], "pos": 1}], 
"time": "199809", 
"id": 113}
"""

import random

flop = entry["board"][:3]
turn = entry["board"][:4]
river = entry["board"][:5]

for user_dict in entry["players"]:
    win_percentage_dict(user_dict)
user_dict["user"]

def win_percentage_dict(user_dict, ):
    hands_dict = {}
    pocket_cards = user_dict["pocket_cards"]
    hands_dict["flop"] = calculate_win_percentage("flop", flop, pocket_cards)
    hands_dict["turn"] = calculate_win_percentage("turn", turn, pocket_cards)
    hands_dict["river"] = calculate_win_percentage("river", river, pocket_cards)
    return hands_dict

# Example usage with ranges
own_hands = ['Ac', 'As']
opponent_range = generate_pocket_combination_range(betting_rate)

def generate_pocket_combination_range(betting_rate):
    suits = "cdhs"
    ranks = "AKQJT98765432"
    range = round(betting_rate * 2652)

    deck = [f"{rank}{suit}" for rank in ranks for suit in suits]

    pocket_range = []
    for card1 in deck:
        for card2 in deck:
            if card1 != card2:
                pocket_range.append([card1, card2])
                if len(pocket_range) >= range:
                    break
        if len(pocket_range) >= range:
            break

    return pocket_range

def calculate_win_percentage(own_hand, opponent_range, board, num_simulations=10000):
    wins = 0

    for _ in range(num_simulations):
        # Randomly choose hands for opponent
        opponent_hand = random.choice(opponent_range)

        # Simulate the rest of the game by dealing the remaining cards
        remaining_deck = [card for card in all_cards if card not in (own_hand + opponent_hand + board)]
        random.shuffle(remaining_deck)

        remaining_board = board.copy()
        while len(remaining_board) < 5:
            remaining_board.append(remaining_deck.pop())

        # Evaluate hands and determine the winner
        player1_total_hand = own_hand + remaining_board
        player2_total_hand = opponent_hand + remaining_board

        if evaluate_hand(player1_total_hand) > evaluate_hand(player2_total_hand):
            wins += 1

    win_probability = wins / num_simulations
    return win_probability

def evaluate_hand(cards):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    # Sort the cards by their values
    cards.sort(key=lambda card: values[card[:-1]])

    # Check for a straight flush
    straight_flush = all(cards[i][-1] == cards[i+1][-1] for i in range(len(cards)-1)) and \
                     all(values[cards[i+1][:-1]] - values[cards[i][:-1]] == 1 for i in range(len(cards)-1))
    if straight_flush:
        return "Straight Flush"

    # Check for four of a kind
    for i in range(len(cards) - 3):
        if all(cards[i][:-1] == cards[j][:-1] for j in range(i+1, i+4)):
            return "Four of a Kind"

    # Check for a full house
    for i in range(len(cards) - 2):
        if all(cards[i][:-1] == cards[j][:-1] for j in range(i+1, i+3)):
            for k in range(i+3, len(cards)-1):
                if all(cards[k][:-1] == cards[l][:-1] for l in range(k+1, k+2)):
                    return "Full House"

    # Check for a flush
    if any(cards.count(cards[i]) >= 5 for i in range(len(cards))):
        return "Flush"

    # Check for a straight
    straight = any(values[cards[i+4][:-1]] - values[cards[i][:-1]] == 4 and len(set(cards[i:i+5])) == 5 for i in range(len(cards)-4))
    if straight:
        return "Straight"

    # Check for three of a kind
    for i in range(len(cards) - 2):
        if all(cards[i][:-1] == cards[j][:-1] for j in range(i+1, i+3)):
            return "Three of a Kind"

    # Check for two pair
    pairs = [cards[i][:-1] for i in range(len(cards)-1) if cards[i][:-1] == cards[i+1][:-1]]
    if len(set(pairs)) == 2:
        return "Two Pair"

    # Check for one pair
    for i in range(len(cards) - 1):
        if cards[i][:-1] == cards[i+1][:-1]:
            return "One Pair"

    # If none of the above, the best hand is a high card
    return "High Card"

# Example usage
hand = ["Ts", "5c", "7h", "8s", "Js", "As", "Ac"]
result = evaluate_hand(hand)
print(f"The hand is: {result}")