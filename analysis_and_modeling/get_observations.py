import random
import json

def get_bluff_boolean(probability):
    # Generate a random number between 0 and 1
    random_number = random.random()
    # Check if the random number is less than the given probability
    return random_number < probability

def get_pot(data, stage):
    if stage == "f":
        if data["win_prob_to_bet_info"]["p"]["bet_info"]["betsize"] == 0:
            return None
        else:
            pot = data["win_prob_to_bet_info"]["p"]["bet_info"]["betsize"] * 2
            return pot
    if stage == "t":
        pot = data["win_prob_to_bet_info"]["p"]["bet_info"]["betsize"]*2 + data["win_prob_to_bet_info"]["f"]["bet_info"]["betsize"]*2
        if pot == 0:
            return None
        else:
            return pot
    if stage == "r":
        pot = data["win_prob_to_bet_info"]["p"]["bet_info"]["betsize"]*2 + data["win_prob_to_bet_info"]["f"]["bet_info"]["betsize"]*2 + data["win_prob_to_bet_info"]["t"]["bet_info"]["betsize"]*2
        if pot == 0:
            return None
        else:
            return pot

def simulate_generative_model(variable_type):

# DATASETS
    hand_num_dict = {'sagerbot': 9111, 'jvegas2': 5738, 'BlackBart': 5148, 'MegaHertz': 4076, 'DrOakland': 3998, 'RiverRatt': 3805, 'show': 3780, 'Rumford': 3536, 'Benway': 3340, 'kk': 2959, 'Swagger': 2923, 'CybrTigr': 2902, 'lexstraus': 2884, 'Gabe': 2599, 'kfish': 2451, 'Benja': 2390, 'Muck': 2383, 'going': 2379, 'exosis': 2338, 'Blaze': 2283, 'num': 2244, 'FX': 2232, 'DP': 2220, 'rivrgod': 2186, 'beaty': 2176, 'CFigor': 2175, 'Sonar': 2160, 'neverx': 2158, 'Sham': 2031, 'Nermal': 1976, 'mt': 1902, 'lilly': 1898, 'tvp': 1797, 'po147': 1780, 'Quick': 1764, 'bigkicker': 1763, 'Patti': 1762, 'theking': 1761, 'superman': 1746, 'fuhzee': 1741, 'KisMyAce': 1718, 'DM': 1708, 'evercall': 1683, 'coming': 1675, 'condor': 1672, 'Harry^T': 1665, 'Winner666': 1634, 'Funky': 1599, 'gsr': 1580, 'carrot': 1540, 'spew-boy': 1525, 'K6': 1493, 'Grizz': 1485, 'RiverMan': 1455, 'is314onu': 1454, 'robw': 1443, 'gfw': 1421, 'Zag': 1407, 'EmtaE': 1407, 'sass': 1358, 'GAR2': 1358, 'Flash_man': 1338, 'reTTard': 1332, 'Zwierdo': 1317, 'Gremlin': 1315, 'gustav': 1303, 'numskull': 1301, 'panfried': 1298, 'ile': 1291, 'keeae': 1290, 'Eldon': 1290, 'Kevin_Un': 1260, 'perfecdoh': 1213, 'Massa': 1195, 'tilted': 1183, 'Sakura': 1156, 'tctim': 1125, 'donguy': 1112, 'Muck_It': 1099, 'Voyeur': 1085, 'JKhearts': 1079, 'Gunshot': 1077, 'Patoot': 1075, 'alfalfa': 1056, 'zxc': 1052, 'ChrisLinn': 1048, 'JADC': 1044, 'SnakeEyes': 1036, 'azspinner': 1032, 'brian': 1017, 'snoball': 1015, 'DopeyTwat': 1009, '__': 1008, 'TripSixes': 1004}
    stages = ["f", "t", "r"]

    for player in hand_num_dict:
        betting_amounts = {"variable_type": variable_type, "data":{}}
        file_path = f'/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/data/data_per_player/data_{player}.json'
        with open(file_path, 'r') as file:
            data_list = [json.loads(line) for line in file]
            for stage in stages:
                stage_betting_amounts = []
                for data in data_list:
                    will_continue = True
                    # CHECK IF ACTION IS UNDEFINED
                    if data["win_prob_to_bet_info"][stage]["bet_info"]["action"] == "undefined":
                        stage_betting_amounts.append(None)
                    else:
                        win_prob = data["win_prob_to_bet_info"][stage]["winprob"]
                        bet_size = data["win_prob_to_bet_info"][stage]["bet_info"]["betsize"]
                        action = data["win_prob_to_bet_info"][stage]["bet_info"]["action"]

                        pot = get_pot(data, stage)

                        if pot == None:
                                stage_betting_amounts.append(None)
                                will_continue = False
                        
                        if will_continue:
                            if win_prob == 1 or win_prob == 0:
                                stage_betting_amounts.append(None)
                                will_continue = False

                        if will_continue:
                            stage_betting_amounts.append(bet_size)

                betting_amounts["data"][stage] = stage_betting_amounts

        with open(f'/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/analysis_and_modeling/data/betting_amounts{player}.json', 'a') as json_file:
            data_to_write = betting_amounts
            json_file.write(json.dumps(data_to_write) + '\n') 
        print(f"processed {player}")
                    

if __name__ == "__main__":
    variable_type_list = ["observation"]
    variable_type = "observation"
    simulate_generative_model(variable_type)
    print("DONE!")

"""
WHEN DATA is NONE:
when the action is undefined
or
when the win prob is 1 or 0 -> you can bet however much you want or never bet: deterministic

for each player
    for each stage (but preflop):
        adjusted_betting_amount = inefficiency * betting_amount (= win_prob * pot / (1 - win_prob)
        # win prob = betting_amount/(pot + betting_amount) solved for betting_amount
            # when actually calculating this, pot = (1 - "betsize_to_pot") * "betsize" / "betsize_to_pot"
        # set inefficiency for each stage by incorporating different psychological phenomena each time (e.g. risk perception, sunk cost fallacy, intuitive probability)
        # inefficiency is the variable we are interested in
        if bluff:
 
    add noise and return decided_betting_amount & decided_betting_amount_to_bankroll

    compare these with actual data

    compare these with each other, and also compare it with when the data set is good players vs bad players (correlate with win percentage)
    do a combination of variables too

    then, take the best performing one, and construct a model that actually predicts the betting amount well
    -> by calculating the optimal variable value
"""

