"""
# Global variables
pot_cats = ["f", "t", "r", "s"]  # f=flop, t=turn, r=river, s=showdown
deck = {
    'A': 'ace',
    'K': 'king',
    'Q': 'queen',
    'J': 'jack',
    'T': '10'
}  # No longer in use; here as a reference
suits = {
    'c': 'clubs',
    's': 'spades',
    'h': 'hearts',
    'd': 'diamonds'
}  # No longer in use; here as a reference
bet_action_codes = {
    '-': 'no action',
    'B': 'blind bet',
    'f': 'fold',
    'k': 'check',
    'b': 'bet',
    'c': 'call',
    'r': 'raise',
    'A': 'all-in',
    'Q': 'quits game',
    'K': 'kicked from game'
}


{"game": "holdempot", 
"dealer": 1, 
"num_players": 2, 
"pots": [{"stage": "f", "num_players": 2, "size": 20}, {"stage": "t", "num_players": 2, "size": 20}, {"stage": "r", "num_players": 2, "size": 20}, {"stage": "s", "num_players": 2, "size": 20}], 
"board": ["6s", "9h", "7s", "Th", "Ad"], 
"players": [
    {"user": "Benja", 
        "bets": [{"actions": ["B", "c"], "stage": "p"}, {"actions": ["k"], "stage": "f"}, {"actions": ["k"], "stage": "t"}, {"actions": ["k"], "stage": "r"}], 
        "bankroll": 3172, 
        "action": 10, 
        "winnings": 0, 
        "pocket_cards": ["Qs", "5c"], 
        "pos": 1}, 
    {"user": "Loboc", 
        "bets": [{"actions": ["B", "k"], "stage": "p"}, {"actions": ["k"], "stage": "f"}, {"actions": ["k"], "stage": "t"}, {"actions": ["k"], "stage": "r"}], 
        "bankroll": 3513, 
        "action": 10, 
        "winnings": 20, 
        "pocket_cards": ["5h", "6c"], 
        "pos": 2}
        ], 
"time": "199809", 
"id": 2}

{"game": "holdempot", 
"dealer": 1, 
"num_players": 2, 
"pots": [{"stage": "f", "num_players": 2, "size": 60}, {"stage": "t", "num_players": 2, "size": 180}, {"stage": "r", "num_players": 2, "size": 180}, {"stage": "s", "num_players": 2, "size": 180}], 
"board": ["2s", "3c", "5c", "8c", "Tc"], 
"players": [
    {"user": "fuhzee", 
        "bets": [{"actions": ["B", "r"], "stage": "p"}, {"actions": ["k", "c"], "stage": "f"}, {"actions": ["k"], "stage": "t"}, {"actions": ["k"], "stage": "r"}], 
        "bankroll": 56158, 
        "action": 90, 
        "winnings": 180, 
        "pocket_cards": ["6d", "6s"], 
        "pos": 1}, 
    {"user": "halibut", 
        "bets": [{"actions": ["B", "c"], "stage": "p"}, {"actions": ["b"], "stage": "f"}, {"actions": ["k"], "stage": "t"}, {"actions": ["k"], "stage": "r"}], 
        "bankroll": 39369, 
        "action": 90, 
        "winnings": 0, 
        "pocket_cards": ["As", "3h"], 
        "pos": 2}], 
"time": "199809", 
"id": 7}

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

# Have to remove hands where olayer quits or get's kicked out
# Does the first player always win? If so, I have to randomize which one I take from

import json
import matplotlib.pyplot as plt

#total = 0
#two_player_count = 0
# player_dict = {}
bankroll = 0
num = 0
highest_bankroll = 0
lowest_bankroll = float('inf')
data = []

for n in range (6):
    file_path = f"/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/data/hands_valid_{n+1}.json"
    with open(file_path, 'r') as file:
    # Load the JSON data from the file
        data_list = [json.loads(line) for line in file]

        # Iterate through the data
        for entry in data_list:
            if entry["num_players"] == 2:
                #two_player_count += 1
                # for player in entry["players"]:
                #     if player["user"] in player_dict:
                #         player_dict[player["user"]] += 1
                #     else:
                #         player_dict[player["user"]] = 1
                for user_dict in entry["players"]:
                    user_bankroll = user_dict["bankroll"]
                    if user_bankroll > highest_bankroll:
                        highest_bankroll = user_bankroll
                    if user_bankroll < lowest_bankroll:
                        lowest_bankroll = user_bankroll
                    bankroll += user_bankroll
                    data.append(user_bankroll)
                    num += 1

avg_bankroll = bankroll/num
print("Avg bankroll is ", avg_bankroll)
print("Highest bankroll is ", highest_bankroll)
print("Lowest bankroll is ", lowest_bankroll)
data = sorted(data)
print(data[:100])
print(data[-100:])

"""
# Plotting the histogram
plt.hist(data, bins=8000, edgecolor='black')  # Adjust the number of bins as needed

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram Example')

# Show the plot
plt.show()
"""
# player_dict = dict(sorted(player_dict.items(), key=lambda item: item[1], reverse=True))



#print("total hands:", total)
#print("num of hands with 2 players:", two_player_count)
# print("Player Library:")
# print(player_dict)
#print("hands that went to the river:", count)

# QUESTION: do people bet according to the math?


