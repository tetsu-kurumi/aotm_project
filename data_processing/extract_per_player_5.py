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

import fcntl
import json
import win_prob_calculator as win_prob_calculator
import numpy as np

# Will do this based on bankroll because they never fold, and the pot odds are almost always 50/50 when it's headsup
def get_betsize(stage, user_dict, entry, betted, bankroll):
    """
    'k': 'check',
    'b': 'bet',
    'c': 'call',
    'r': 'raise',
    """
    undefined = False
    
    if stage == "p":
        n = 0
        betsize = entry["pots"][n]["size"] / 2 - betted
        betsize_to_pot = None
    if stage == "f":
        n = 1
        if entry["pots"][n-1]["num_players"] == 0:
            undefined = True
        betsize = entry["pots"][n]["size"] / 2 - betted
        if not undefined:
            betsize_to_pot = betsize / entry["pots"][n-1]["size"] + betsize
    if stage == "t":
        n = 2
        if entry["pots"][n-1]["num_players"] == 0:
            undefined = True
        betsize = entry["pots"][n]["size"] / 2 - betted
        if not undefined:
            betsize_to_pot = betsize / entry["pots"][n-1]["size"] + betsize
    if stage == "r":
        n = 3
        if entry["pots"][n-1]["num_players"] == 0:
            undefined = True
        betsize = entry["pots"][n]["size"] / 2 - betted
        if not undefined:
            betsize_to_pot = betsize / entry["pots"][n-1]["size"] + betsize
    
    if bankroll != 0:
        betsize_to_bankroll = betsize / bankroll
    else:
        betsize_to_bankroll = None

    if undefined:
        return {"action": "undefined", "betsize": 0, "betsize_to_bankroll": 0, "betsize_to_pot": 0}
    if "r" in user_dict["bets"][n]["actions"] or "b" in user_dict["bets"][n]["actions"] or "A" in user_dict["bets"][n]["actions"]:
        return {"action": "b", "betsize": betsize, "betsize_to_bankroll": betsize_to_bankroll, "betsize_to_pot": betsize_to_pot}
    if "c" in user_dict["bets"][n]["actions"]:
        return {"action": "c", "betsize": betsize, "betsize_to_bankroll": betsize_to_bankroll, "betsize_to_pot": betsize_to_pot}
    if "k" in user_dict["bets"][n]["actions"]:
        return {"action": "k", "betsize": betsize, "betsize_to_bankroll": betsize_to_bankroll, "betsize_to_pot": betsize_to_pot}
    else:
        return {"action": "undefined", "betsize": 0, "betsize_to_bankroll": 0, "betsize_to_pot": 0}
    
# gotta check if undefined and not add it

def win_percentage_dict(user_dict, flop, turn, river, entry):
    hands_dict = {}
    pocket_cards = user_dict["pocket_cards"]
    bankroll = user_dict["bankroll"]
    betted = 0
    
    win_prob_p = win_prob_calculator.win_prob([], pocket_cards)
    betsize_info_p = get_betsize("p", user_dict, entry, betted, bankroll)
    betsize_p = betsize_info_p["betsize"]
    betted += betsize_p
    bankroll -= betsize_p
    hands_dict["p"] = {"winprob": win_prob_p, "bet_info": betsize_info_p}
     
    win_prob_f = win_prob_calculator.win_prob(flop, pocket_cards)
    betsize_info_f = get_betsize("f", user_dict, entry, betted, bankroll)
    betsize_f = betsize_info_f["betsize"]
    betted += betsize_f
    bankroll -= betsize_f
    hands_dict["f"] = {"winprob": win_prob_f, "bet_info": betsize_info_f}

     
    win_prob_t = win_prob_calculator.win_prob(turn, pocket_cards)
    betsize_info_t = get_betsize("t", user_dict, entry, betted, bankroll)
    betsize_t = betsize_info_t["betsize"]
    betted += betsize_t
    bankroll -= betsize_t
    hands_dict["t"] = {"winprob": win_prob_t, "bet_info": betsize_info_t}

    
    win_prob_r = win_prob_calculator.win_prob(river, pocket_cards)
    betsize_info_r = get_betsize("r", user_dict, entry, betted, bankroll)
    betsize_r = betsize_info_r["betsize"]
    betted += betsize_r
    hands_dict["r"] = {"winprob": win_prob_r, "bet_info": betsize_info_r}

    return hands_dict

if __name__ == "__main__":
    users_to_extract={'sagerbot': 9111, 'jvegas2': 5738, 'BlackBart': 5148, 'MegaHertz': 4076, 'DrOakland': 3998, 'RiverRatt': 3805, 'show': 3780, 'Rumford': 3536, 'Benway': 3340, 'kk': 2959, 'Swagger': 2923, 'CybrTigr': 2902, 'lexstraus': 2884, 'Gabe': 2599, 'kfish': 2451, 'Benja': 2390, 'Muck': 2383, 'going': 2379, 'exosis': 2338, 'Blaze': 2283, 'num': 2244, 'FX': 2232, 'DP': 2220, 'rivrgod': 2186, 'beaty': 2176, 'CFigor': 2175, 'Sonar': 2160, 'neverx': 2158, 'Sham': 2031, 'Nermal': 1976, 'mt': 1902, 'lilly': 1898, 'tvp': 1797, 'po147': 1780, 'Quick': 1764, 'bigkicker': 1763, 'Patti': 1762, 'theking': 1761, 'superman': 1746, 'fuhzee': 1741, 'KisMyAce': 1718, 'DM': 1708, 'evercall': 1683, 'coming': 1675, 'condor': 1672, 'Harry^T': 1665, 'Winner666': 1634, 'Funky': 1599, 'gsr': 1580, 'carrot': 1540, 'spew-boy': 1525, 'K6': 1493, 'Grizz': 1485, 'RiverMan': 1455, 'is314onu': 1454, 'robw': 1443, 'gfw': 1421, 'Zag': 1407, 'EmtaE': 1407, 'sass': 1358, 'GAR2': 1358, 'Flash_man': 1338, 'reTTard': 1332, 'Zwierdo': 1317, 'Gremlin': 1315, 'gustav': 1303, 'numskull': 1301, 'panfried': 1298, 'ile': 1291, 'keeae': 1290, 'Eldon': 1290, 'Kevin_Un': 1260, 'perfecdoh': 1213, 'Massa': 1195, 'tilted': 1183, 'Sakura': 1156, 'tctim': 1125, 'donguy': 1112, 'Muck_It': 1099, 'Voyeur': 1085, 'JKhearts': 1079, 'Gunshot': 1077, 'Patoot': 1075, 'alfalfa': 1056, 'zxc': 1052, 'ChrisLinn': 1048, 'JADC': 1044, 'SnakeEyes': 1036, 'azspinner': 1032, 'brian': 1017, 'snoball': 1015, 'DopeyTwat': 1009, '__': 1008, 'TripSixes': 1004}
    file_path = f"/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/data/hands_valid_5.json"
    with open(file_path, 'r') as file:
            # Load the JSON data from the file
            data_list = [json.loads(line) for line in file]
            # Iterate through the data
            for entry in data_list:
                if entry["id"] >= 0:
                    continue_switch = True
                    flop = entry["board"][:3]
                    turn = entry["board"][:4]
                    river = entry["board"][:5]
                    entry_dict = {}
                    if entry["num_players"] == 2:
                        for user_dict in entry["players"]:
                            user = user_dict["user"]
                            if user in users_to_extract:
                                hands_dict = win_percentage_dict(user_dict, flop, turn, river, entry)
                                # Write to a JSON file
                                with open(f'/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/data/data_per_player/data_{user}.json', 'a') as json_file:
                                    data_to_write = {"id": entry["id"], "win_prob_to_bet_info": hands_dict, "bankroll": user_dict["bankroll"], "total_bet": user_dict["action"], "winnings": user_dict["winnings"]}
                                    fcntl.flock(file, fcntl.LOCK_EX)  # Acquire an exclusive lock
                                    json_file.seek(0, 2)
                                    json_file.write(json.dumps(data_to_write) + '\n') 
                                    fcntl.flock(file, fcntl.LOCK_UN)
                                id = entry["id"]
                                print(f"processed id {id}")

"""
undefined: is because when a player goes all in, there is no action to be played anymore

Data to delete:
when action is undefined & when bet is negative

{"id": 2, "win_prob_to_bet_info": {"p": {"winprob": 0.4088, "bet_info": {"action": "c", "betsize": 10.0, "betsize_to_bankroll": 0.0031525851197982345, "betsize_to_pot": null}}, "f": {"winprob": 0.38515, "bet_info": {"action": "k", "betsize": 0.0, "betsize_to_bankroll": 0.0, "betsize_to_pot": 0.0}}, "t": {"winprob": 0.315, "bet_info": {"action": "k", "betsize": 0.0, "betsize_to_bankroll": 0.0, "betsize_to_pot": 0.0}}, "r": {"winprob": 0.08075, "bet_info": {"action": "k", "betsize": 0.0, "betsize_to_bankroll": 0.0, "betsize_to_pot": 0.0}}}, "bankroll": 3172, "total_bet": 10, "winnings": 0}
"""