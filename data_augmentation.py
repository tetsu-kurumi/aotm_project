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
"""

# Have to remove hands where olayer quits or get's kicked out

import json

#total = 0
#two_player_count = 0
# player_dict = {}
count = 0

for n in range (6):
    file_path = f"/workspaces/aotm_project/data/hands_valid_{n+1}.json"
    with open(file_path, 'r') as file:
    # Load the JSON data from the file
        data_list = [json.loads(line) for line in file]

        # Iterate through the data
        for entry in data_list:
            #total += 1
            if entry["num_players"] == 2:
                #two_player_count += 1
                # for player in entry["players"]:
                #     if player["user"] in player_dict:
                #         player_dict[player["user"]] += 1
                #     else:
                #         player_dict[player["user"]] = 1
                if len(entry["board"]) == 5:
                    count += 1

# player_dict = dict(sorted(player_dict.items(), key=lambda item: item[1], reverse=True))



#print("total hands:", total)
#print("num of hands with 2 players:", two_player_count)
# print("Player Library:")
# print(player_dict)
print("hands that went to the river:", count)



