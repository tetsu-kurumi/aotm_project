"""
{"game": "holdempot", 
"dealer": 1, 
"num_players": 2, 
"pots": [
    {"stage": "f", "num_players": 2, "size": 60}, 
    {"stage": "t", "num_players": 2, "size": 180}, 
    {"stage": "r", "num_players": 2, "size": 540}, 
    {"stage": "s", "num_players": 2, "size": 540}], 
"board": ["Ts", "5c", "7h", "8s", "Js"], 
"players": 
[
    {"user": "PoTz", 
        "bets": [
            {"actions": ["B", "c"], "stage": "p"}, 
            {"actions": ["c"], "stage": "f"}, 
            {"actions": ["c"], "stage": "t"}, 
            {"actions": ["k"], "stage": "r"}], 
        "bankroll": 4877, 
        "action": 270, 
        "winnings": 540, 
        "pocket_cards": ["Qh", "Td"], 
        "pos": 2}, 
    {"user": "__", 
        "bets": [
            {"actions": ["B", "r"], "stage": "p"}, 
            {"actions": ["b"], "stage": "f"}, 
            {"actions": ["b"], "stage": "t"}, 
            {"actions": ["k"], "stage": "r"}], 
        "bankroll": 47590, 
        "action": 270, 
        "winnings": 0, 
        "pocket_cards": ["6c", "Kh"], 
        "pos": 1}], 
"time": "199809", 
"id": 113}
"""

import random
from win_prob_calculator import *

flop = entry["board"][:3]
turn = entry["board"][:4]
river = entry["board"][:5]

for n in range (6):
    file_path = f"/workspaces/aotm_project/data/hands_valid_{n+1}.json"
    with open(file_path, 'r') as file:
    # Load the JSON data from the file
        data_list = [json.loads(line) for line in file]
        dict_per_file = {}
        # Iterate through the data
        for entry in data_list:
            entry_dict = {}
            if entry["num_players"] == 2:
                for user_dict in entry["players"]:
                    hands_dict = win_percentage_dict(user_dict, flop, turn, river)
                    entry_dict["user"] = hands_dict
            dict_per_file[entry["id"]] = entry_dict
    print(dict_per_file)

def win_percentage_dict(user_dict, flop, turn, river):
    hands_dict = {}
    pocket_cards = user_dict["pocket_cards"]
    hands_dict["p"] = win_prob_calculator.win_prob([], pocket_cards)
    hands_dict["f"] = win_prob_calculator.win_prob(flop, pocket_cards)
    hands_dict["t"] = win_prob_calculator.win_prob(turn, pocket_cards)
    hands_dict["r"] = win_prob_calculator.win_prob(river, pocket_cards)
    return hands_dict

