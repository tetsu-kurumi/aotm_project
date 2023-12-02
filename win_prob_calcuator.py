import random
from collections import Counter

def generate_pocket_combination_range(betting_rate):
    range = round(betting_rate * 2652)
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
        set1 = set(own_hand + board)
        set2 = set(opponent_hand)
        # Check if there is an intersection between the sets
        while set1.intersection(set2):
            opponent_hand = random.choice(opponent_range)
            set1 = set(own_hand + board)
            set2 = set(opponent_hand)

        # Simulate the rest of the game by dealing the remaining cards
        remaining_deck = [card for card in deck if card not in (own_hand + opponent_hand + board)]
        random.shuffle(remaining_deck)

        remaining_board = board.copy()
        while len(remaining_board) < 5:
            remaining_board.append(remaining_deck.pop())

        # Evaluate hands and determine the winner
        own_total_hand = own_hand + remaining_board
        opponent_total_hand = opponent_hand + remaining_board

        if compare_hands(own_total_hand, opponent_total_hand) == 1:
            wins += 1
        if compare_hands(own_total_hand, opponent_total_hand) == 2:
            wins += 0.5

    win_probability = wins / num_simulations
    return win_probability

def extract_nums(cards):
    num_list = []
    for i in range (len(cards)):
        key_to_convert = cards[i][0]
        num_list.append(values[key_to_convert])
    return(sorted(num_list))

def flush_checker(cards, flush_list):
    spade_count = 0
    heart_count = 0
    club_count = 0
    diamonds_count = 0
    for i in range (len(cards)):
        if cards[i][1] == 's':
            spade_count += 1
            flush_list.append(values[cards[i][0]])
        if cards[i][1] == 'h':
            heart_count += 1
            flush_list.append(values[cards[i][0]])
        if cards[i][1] == 'c':
            club_count += 1
            flush_list.append(values[cards[i][0]])
        if cards[i][1] == 'd':
            diamonds_count += 1
            flush_list.append(values[cards[i][0]])
    if spade_count >= 5 or heart_count >= 5 or club_count >= 5 or diamonds_count >= 5:
        return True
    else:
        return False

def evaluate_hand(cards):
    flush_list = []
    # Sort the cards by their values
    cards.sort(key=lambda card: values[card[:-1]])
    #print(cards)
    
    # Count occurences
    num_list = extract_nums(cards)
    counter = Counter(num_list)
    most_common = counter.most_common()

    # Check for a straight
    straight = False
    consec = 0
    for i in range(len(num_list)-1):
        if num_list[i] != num_list[i+1]:
            if num_list[i] == num_list[i+1] - 1:
                if consec == 0:
                    beginning_of_straight = num_list[i]
                    num_before_beginning_of_straight = i
                consec += 1             
    if consec >= 4:
        straight = True
    if consec == 3 and num_list[0] == 2 and 14 in num_list:
        straight = True
    
    # Check for a straight flush
    straight_flush = False
    if straight:
        if flush_checker(cards[num_before_beginning_of_straight:], flush_list):
            straight_flush = True
    if straight_flush:
        return 8, beginning_of_straight+consec #"Straight Flush"

    # Check for four of a kind
    if most_common[0][1] >= 4:
        return 7, most_common[0][0] #"Four of a Kind"

    # Check for a full house
    if most_common[0][1] + most_common[1][1] > 5:
        return 6, (most_common[0][0], most_common[1][0])  #"Full House"
                    
    if flush_checker(cards, flush_list):
        return 5, sorted(flush_list) #"Flush"

    if straight:
        return 4, beginning_of_straight+consec #"Straight"

    # Check for three of a kind
    if most_common[0][1] == 3:
        return 3, most_common[0][0] #"Three of a Kind"

    # Check for two pair
    if most_common[0][1] == 2 and most_common[1][1] == 2 and most_common[2][1] == 2:
        return 2, (most_common[0][0], most_common[1][0], most_common[2][0]) #"Two Pair"
    
    if most_common[0][1] == 2 and most_common[1][1] == 2:
        return 2, (most_common[0][0], most_common[1][0]) #"Two Pair"

    # Check for one pair
    if most_common[0][1] == 2:
        return 1, most_common[0][0]

    # If none of the above, the best hand is a high card
    return 0, num_list[-1] #"High Card"


def compare_hands(hand1, hand2):
    eval_hand1 = evaluate_hand(hand1)
    eval_hand2 = evaluate_hand(hand2)

    if eval_hand1[0] > eval_hand2[0]:
        return 1
        #print ("Hand 1 wins", eval_hand1[0])
    elif eval_hand1[0] < eval_hand2[0]:
        print ("Hand 2 wins", eval_hand2[0])
        return 0
    else:
        if handle_ties(eval_hand1, eval_hand2, hand1, hand2) == "tie":
            print("It's a tie", eval_hand1, eval_hand2)
            return 2
        elif handle_ties(eval_hand1, eval_hand2, hand1, hand2) == "hand1":
            return 1
            #print ("Hand 1 wins", eval_hand1[0])
        elif handle_ties(eval_hand1, eval_hand2, hand1, hand2) == "hand2":
            print ("Hand 2 wins", eval_hand2[0]) 
            return 0   

def handle_ties(hand1, hand2, board1, board2):
    num_list_1 = extract_nums(board1)
    num_list_2 = extract_nums(board2)
    if hand1[0] == 0:
        return "tie"
    if hand1[0] == 1:
        if hand1[1] > hand2[1]:
            return "hand1"
        if hand1[1] < hand2[1]:
            return "hand2"
        else:
            best_kicker_1 = [element for element in num_list_1 if element != hand1[1]][2:][-1]
            second_best_kicker_1 = [element for element in num_list_1 if element != best_kicker_1][2:][-2]
            best_kicker_2 = [element for element in num_list_2 if element != hand2[1]][2:][-1]
            second_best_kicker_2 = [element for element in num_list_2 if element != best_kicker_2][2:][-2]
            if best_kicker_1 > best_kicker_2:
                return "hand1"
            if best_kicker_1 < best_kicker_2:
                return "hand2"
            else:
                if second_best_kicker_1 > second_best_kicker_2:
                    return "hand1"
                if second_best_kicker_1 < second_best_kicker_2:
                    return "hand2"
                else:
                    return "tie"
    if hand1[0] == 2:
        if max(hand1[1]) > max(hand2[1]):
            return "hand1"
        if max(hand1[1]) < max(hand2[1]):
            return "hand2"
        else:
            hand1_pairs = [element for element in hand1[1] if element != (max(hand1[1]))]
            hand2_pairs = [element for element in hand2[1] if element != (max(hand2[1]))]
            best_kicker_1 = [element for element in num_list_1 if element != max(hand1_pairs)][2:][-1]
            best_kicker_2 = [element for element in num_list_2 if element != max(hand2_pairs)][2:][-1]
            if best_kicker_1 > best_kicker_2:
                return "hand1"
            if best_kicker_1 < best_kicker_2:
                return "hand2"
            else:
                return "tie"
    if hand1[0] == 3:
        if hand1[1] > hand2[1]:
            return "hand1"
        if hand1[1] < hand2[1]:
            return "hand2"
        else:
            best_kicker_1 = [element for element in num_list_1 if element != hand1[1]][2:][-1]
            second_best_kicker_1 = [element for element in num_list_1 if element != best_kicker_1][2:][-2]
            best_kicker_2 = [element for element in num_list_2 if element != hand2[1]][2:][-1]
            second_best_kicker_2 = [element for element in num_list_2 if element != best_kicker_2][2:][-2]
            if best_kicker_1 > best_kicker_2:
                return "hand1"
            if best_kicker_1 < best_kicker_2:
                return "hand2"
            else:
                if second_best_kicker_1 > second_best_kicker_2:
                    return "hand1"
                if second_best_kicker_1 < second_best_kicker_2:
                    return "hand2"
                else:
                    return "tie"
    if hand1[0] == 4:
        if hand1[1] > hand2[1]:
            return "hand1"
        if hand1[1] < hand2[1]:
            return "hand2"
        else:
            return "tie"
    if hand1[0] == 5:
        for i in range (1,6):
            if hand1[1][-i] > hand2[1][-i]:
                return "hand1"
            if hand1[1][-i] < hand2[1][-i]:
                return "hand2"
        else:
            return "tie"
    if hand1[0] == 6:
        if hand1[1][0] > hand2[1][0]:
            return "hand1"
        if hand1[1][0] < hand2[1][0]:
            return "hand2"
        elif hand1[1][1] > hand2[1][1]:
            return "hand1"
        elif hand1[1][1] < hand2[1][1]:
            return "hand2"
        else:
            return "tie"
    if hand1[0] == 7:
        if hand1[1] > hand2[1]:
            return "hand1"
        if hand1[1] < hand2[1]:
            return "hand2"
        else:
            kicker_1 = [element for element in num_list_1 if element != hand1[1]][2:][-1]
            kicker_2 = [element for element in num_list_2 if element != hand2[1]][2:][-1]
            if kicker_1 > kicker_2:
                return "hand1"
            if kicker_1 < kicker_2:
                return "hand2"
            else:
                return "tie"
    if hand1[0] == 8:
        if hand1[1] > hand2[1]:
            return "hand1"
        if hand1[1] < hand2[1]:
            return "hand2"
        else:
            return "tie"

if __name__ == "__main__":
    # Variables
    board = ["Ts", "5c", "7h"]
    opponent_betting_rate = 0.3
    own_hands = ["Qh", "Td"]

    suits = "cdhs"
    ranks = "AKQJT98765432"
    deck = [f"{rank}{suit}" for rank in ranks for suit in suits]
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    opponent_range = generate_pocket_combination_range(opponent_betting_rate)
    win_prob = calculate_win_percentage(own_hands, opponent_range, board)
    print("win prob is", win_prob)

