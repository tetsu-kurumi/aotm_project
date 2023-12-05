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

    
# CHANGE THE DEVIATION FROM THE OPTIMAL POLICY DEPENDING ON THE GENERATIVE MODEL TYPE
def compute_adjusted_betting_amount(variable_type, optimal_betting_amount, call):
    if variable_type == "over_confidence":
        return optimal_betting_amount * 2
    if variable_type == "optimal":
        return optimal_betting_amount 
    if variable_type == "under_confidence": # opposite of bluffing
        prob = 0.3
        random_number = random.random()
        if random_number < prob:
            return 0
        else:
            return optimal_betting_amount
    
    

# TODO: Write add_noise
def add_noise(betting_amount, variable_type):
    if variable_type == "optimal":
        noise_rate = 1
    else:
        mean = 1
        std_dev = 0.1  # Adjust the standard deviation based on your requirements

        # Generate random samples from a normal distribution
        noise_rate = [random.gauss(mean, std_dev) for _ in range(1)][0]

    betting_amount_with_noise = betting_amount * noise_rate

    return betting_amount_with_noise

def simulate_generative_model(variable_type):

# DATASETS
    hand_num_dict = {'sagerbot': 9111, 'jvegas2': 5738, 'BlackBart': 5148, 'MegaHertz': 4076, 'DrOakland': 3998, 'RiverRatt': 3805, 'show': 3780, 'Rumford': 3536, 'Benway': 3340, 'kk': 2959, 'Swagger': 2923, 'CybrTigr': 2902, 'lexstraus': 2884, 'Gabe': 2599, 'kfish': 2451, 'Benja': 2390, 'Muck': 2383, 'going': 2379, 'exosis': 2338, 'Blaze': 2283, 'num': 2244, 'FX': 2232, 'DP': 2220, 'rivrgod': 2186, 'beaty': 2176, 'CFigor': 2175, 'Sonar': 2160, 'neverx': 2158, 'Sham': 2031, 'Nermal': 1976, 'mt': 1902, 'lilly': 1898, 'tvp': 1797, 'po147': 1780, 'Quick': 1764, 'bigkicker': 1763, 'Patti': 1762, 'theking': 1761, 'superman': 1746, 'fuhzee': 1741, 'KisMyAce': 1718, 'DM': 1708, 'evercall': 1683, 'coming': 1675, 'condor': 1672, 'Harry^T': 1665, 'Winner666': 1634, 'Funky': 1599, 'gsr': 1580, 'carrot': 1540, 'spew-boy': 1525, 'K6': 1493, 'Grizz': 1485, 'RiverMan': 1455, 'is314onu': 1454, 'robw': 1443, 'gfw': 1421, 'Zag': 1407, 'EmtaE': 1407, 'sass': 1358, 'GAR2': 1358, 'Flash_man': 1338, 'reTTard': 1332, 'Zwierdo': 1317, 'Gremlin': 1315, 'gustav': 1303, 'numskull': 1301, 'panfried': 1298, 'ile': 1291, 'keeae': 1290, 'Eldon': 1290, 'Kevin_Un': 1260, 'perfecdoh': 1213, 'Massa': 1195, 'tilted': 1183, 'Sakura': 1156, 'tctim': 1125, 'donguy': 1112, 'Muck_It': 1099, 'Voyeur': 1085, 'JKhearts': 1079, 'Gunshot': 1077, 'Patoot': 1075, 'alfalfa': 1056, 'zxc': 1052, 'ChrisLinn': 1048, 'JADC': 1044, 'SnakeEyes': 1036, 'azspinner': 1032, 'brian': 1017, 'snoball': 1015, 'DopeyTwat': 1009, '__': 1008, 'TripSixes': 1004}
    bluff_prob_dict = {'f': {'sagerbot': 0.03808165057067603, 'jvegas2': 0.07753964105244816, 'BlackBart': 0.040396193435618566, 'MegaHertz': 0.0323846908734053, 'DrOakland': 0.062281140570285144, 'RiverRatt': 0.06806833114323259, 'show': 0.03968253968253968, 'Rumford': 0.041289592760180995, 'Benway': 0.09850299401197604, 'kk': 0.032105441027374115, 'Swagger': 0.023947998631542934, 'CybrTigr': 0.08852910781949708, 'lexstraus': 0.039875173370319004, 'Gabe': 0.05348210850327049, 'kfish': 0.02160619649408887, 'Benja': 0.04096989966555184, 'Muck': 0.08850671140939598, 'going': 0.03825136612021858, 'exosis': 0.10949529512403763, 'Blaze': 0.04161191414805081, 'num': 0.10249554367201426, 'FX': 0.04973118279569892, 'DP': 0.039171544349392164, 'rivrgod': 0.054412437128486514, 'beaty': 0.0399632521819017, 'CFigor': 0.011436413540713633, 'Sonar': 0.09717723276260991, 'neverx': 0.041241890639481, 'Sham': 0.03545051698670606, 'Nermal': 0.08198380566801619, 'mt': 0.04153522607781283, 'lilly': 0.008952080042127435, 'tvp': 0.09515859766277128, 'po147': 0.12022471910112359, 'Quick': 0.08333333333333333, 'bigkicker': 0.09126984126984126, 'Patti': 0.07150964812712826, 'theking': 0.09297052154195011, 'superman': 0.05377574370709382, 'fuhzee': 0.010913268236645606, 'KisMyAce': 0.09133216986620128, 'DM': 0.09836065573770492, 'evercall': 0.07605466428995841, 'coming': 0.042388059701492536, 'condor': 0.046052631578947366, 'Harry^T': 0.02100840336134454, 'Winner666': 0.15850673194614442, 'Funky': 0.023764853033145718, 'gsr': 0.018975332068311195, 'carrot': 0.02142857142857143, 'spew-boy': 0.07672131147540984, 'K6': 0.03815261044176707, 'Grizz': 0.0941492938802959, 'RiverMan': 0.06391752577319587, 'is314onu': 0.03576341127922971, 'robw': 0.0990990990990991, 'gfw': 0.03870513722730472, 'Zag': 0.06392045454545454, 'EmtaE': 0.09523809523809523, 'sass': 0.020618556701030927, 'GAR2': 0.039764359351988215, 'Flash_man': 0.05451829723674384, 'reTTard': 0.06681681681681682, 'Zwierdo': 0.0417298937784522, 'Gremlin': 0.02585551330798479, 'gustav': 0.039140445126630855, 'numskull': 0.10453497309761722, 'panfried': 0.02157164869029276, 'ile': 0.053446940356312936, 'keeae': 0.0069767441860465115, 'Eldon': 0.06201550387596899, 'Kevin_Un': 0.05, 'perfecdoh': 0.023887973640856673, 'Massa': 0.06276150627615062, 'tilted': 0.081787521079258, 'Sakura': 0.020761245674740483, 'tctim': 0.059555555555555556, 'donguy': 0.09164420485175202, 'Muck_It': 0.07370336669699727, 'Voyeur': 0.05898617511520737, 'JKhearts': 0.014828544949026877, 'Gunshot': 0.11234911792014857, 'Patoot': 0.03531598513011153, 'alfalfa': 0.04734848484848485, 'zxc': 0.058935361216730035, 'ChrisLinn': 0.03142857142857143, 'JADC': 0.031609195402298854, 'SnakeEyes': 0.024108003857280617, 'azspinner': 0.012596899224806201, 'brian': 0.12094395280235988, 'snoball': 0.10541871921182266, 'DopeyTwat': 0.007928642220019821, '__': 0.03270564915758176, 'TripSixes': 0.07171314741035857}, 't': {'sagerbot': 0.03808165057067603, 'jvegas2': 0.07753964105244816, 'BlackBart': 0.040396193435618566, 'MegaHertz': 0.0323846908734053, 'DrOakland': 0.062281140570285144, 'RiverRatt': 0.06806833114323259, 'show': 0.03968253968253968, 'Rumford': 0.041289592760180995, 'Benway': 0.09850299401197604, 'kk': 0.032105441027374115, 'Swagger': 0.023947998631542934, 'CybrTigr': 0.08852910781949708, 'lexstraus': 0.039875173370319004, 'Gabe': 0.05348210850327049, 'kfish': 0.02160619649408887, 'Benja': 0.04096989966555184, 'Muck': 0.08850671140939598, 'going': 0.03825136612021858, 'exosis': 0.10949529512403763, 'Blaze': 0.04161191414805081, 'num': 0.10249554367201426, 'FX': 0.04973118279569892, 'DP': 0.039171544349392164, 'rivrgod': 0.054412437128486514, 'beaty': 0.0399632521819017, 'CFigor': 0.011436413540713633, 'Sonar': 0.09717723276260991, 'neverx': 0.041241890639481, 'Sham': 0.03545051698670606, 'Nermal': 0.08198380566801619, 'mt': 0.04153522607781283, 'lilly': 0.008952080042127435, 'tvp': 0.09515859766277128, 'po147': 0.12022471910112359, 'Quick': 0.08333333333333333, 'bigkicker': 0.09126984126984126, 'Patti': 0.07150964812712826, 'theking': 0.09297052154195011, 'superman': 0.05377574370709382, 'fuhzee': 0.010913268236645606, 'KisMyAce': 0.09133216986620128, 'DM': 0.09836065573770492, 'evercall': 0.07605466428995841, 'coming': 0.042388059701492536, 'condor': 0.046052631578947366, 'Harry^T': 0.02100840336134454, 'Winner666': 0.15850673194614442, 'Funky': 0.023764853033145718, 'gsr': 0.018975332068311195, 'carrot': 0.02142857142857143, 'spew-boy': 0.07672131147540984, 'K6': 0.03815261044176707, 'Grizz': 0.0941492938802959, 'RiverMan': 0.06391752577319587, 'is314onu': 0.03576341127922971, 'robw': 0.0990990990990991, 'gfw': 0.03870513722730472, 'Zag': 0.06392045454545454, 'EmtaE': 0.09523809523809523, 'sass': 0.020618556701030927, 'GAR2': 0.039764359351988215, 'Flash_man': 0.05451829723674384, 'reTTard': 0.06681681681681682, 'Zwierdo': 0.0417298937784522, 'Gremlin': 0.02585551330798479, 'gustav': 0.039140445126630855, 'numskull': 0.10453497309761722, 'panfried': 0.02157164869029276, 'ile': 0.053446940356312936, 'keeae': 0.0069767441860465115, 'Eldon': 0.06201550387596899, 'Kevin_Un': 0.05, 'perfecdoh': 0.023887973640856673, 'Massa': 0.06276150627615062, 'tilted': 0.081787521079258, 'Sakura': 0.020761245674740483, 'tctim': 0.059555555555555556, 'donguy': 0.09164420485175202, 'Muck_It': 0.07370336669699727, 'Voyeur': 0.05898617511520737, 'JKhearts': 0.014828544949026877, 'Gunshot': 0.11234911792014857, 'Patoot': 0.03531598513011153, 'alfalfa': 0.04734848484848485, 'zxc': 0.058935361216730035, 'ChrisLinn': 0.03142857142857143, 'JADC': 0.031609195402298854, 'SnakeEyes': 0.024108003857280617, 'azspinner': 0.012596899224806201, 'brian': 0.12094395280235988, 'snoball': 0.10541871921182266, 'DopeyTwat': 0.007928642220019821, '__': 0.03270564915758176, 'TripSixes': 0.07171314741035857}, 'r': {'sagerbot': 0.03808165057067603, 'jvegas2': 0.07753964105244816, 'BlackBart': 0.040396193435618566, 'MegaHertz': 0.0323846908734053, 'DrOakland': 0.062281140570285144, 'RiverRatt': 0.06806833114323259, 'show': 0.03968253968253968, 'Rumford': 0.041289592760180995, 'Benway': 0.09850299401197604, 'kk': 0.032105441027374115, 'Swagger': 0.023947998631542934, 'CybrTigr': 0.08852910781949708, 'lexstraus': 0.039875173370319004, 'Gabe': 0.05348210850327049, 'kfish': 0.02160619649408887, 'Benja': 0.04096989966555184, 'Muck': 0.08850671140939598, 'going': 0.03825136612021858, 'exosis': 0.10949529512403763, 'Blaze': 0.04161191414805081, 'num': 0.10249554367201426, 'FX': 0.04973118279569892, 'DP': 0.039171544349392164, 'rivrgod': 0.054412437128486514, 'beaty': 0.0399632521819017, 'CFigor': 0.011436413540713633, 'Sonar': 0.09717723276260991, 'neverx': 0.041241890639481, 'Sham': 0.03545051698670606, 'Nermal': 0.08198380566801619, 'mt': 0.04153522607781283, 'lilly': 0.008952080042127435, 'tvp': 0.09515859766277128, 'po147': 0.12022471910112359, 'Quick': 0.08333333333333333, 'bigkicker': 0.09126984126984126, 'Patti': 0.07150964812712826, 'theking': 0.09297052154195011, 'superman': 0.05377574370709382, 'fuhzee': 0.010913268236645606, 'KisMyAce': 0.09133216986620128, 'DM': 0.09836065573770492, 'evercall': 0.07605466428995841, 'coming': 0.042388059701492536, 'condor': 0.046052631578947366, 'Harry^T': 0.02100840336134454, 'Winner666': 0.15850673194614442, 'Funky': 0.023764853033145718, 'gsr': 0.018975332068311195, 'carrot': 0.02142857142857143, 'spew-boy': 0.07672131147540984, 'K6': 0.03815261044176707, 'Grizz': 0.0941492938802959, 'RiverMan': 0.06391752577319587, 'is314onu': 0.03576341127922971, 'robw': 0.0990990990990991, 'gfw': 0.03870513722730472, 'Zag': 0.06392045454545454, 'EmtaE': 0.09523809523809523, 'sass': 0.020618556701030927, 'GAR2': 0.039764359351988215, 'Flash_man': 0.05451829723674384, 'reTTard': 0.06681681681681682, 'Zwierdo': 0.0417298937784522, 'Gremlin': 0.02585551330798479, 'gustav': 0.039140445126630855, 'numskull': 0.10453497309761722, 'panfried': 0.02157164869029276, 'ile': 0.053446940356312936, 'keeae': 0.0069767441860465115, 'Eldon': 0.06201550387596899, 'Kevin_Un': 0.05, 'perfecdoh': 0.023887973640856673, 'Massa': 0.06276150627615062, 'tilted': 0.081787521079258, 'Sakura': 0.020761245674740483, 'tctim': 0.059555555555555556, 'donguy': 0.09164420485175202, 'Muck_It': 0.07370336669699727, 'Voyeur': 0.05898617511520737, 'JKhearts': 0.014828544949026877, 'Gunshot': 0.11234911792014857, 'Patoot': 0.03531598513011153, 'alfalfa': 0.04734848484848485, 'zxc': 0.058935361216730035, 'ChrisLinn': 0.03142857142857143, 'JADC': 0.031609195402298854, 'SnakeEyes': 0.024108003857280617, 'azspinner': 0.012596899224806201, 'brian': 0.12094395280235988, 'snoball': 0.10541871921182266, 'DopeyTwat': 0.007928642220019821, '__': 0.03270564915758176, 'TripSixes': 0.07171314741035857}}
    stages = ["f", "t", "r"]

    for player in hand_num_dict:
        betting_amounts = {"variable_type": variable_type, "data":{}}
        file_path = f'/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/data/data_per_player/data_{player}.json'
        with open(file_path, 'r') as file:
            data_list = [json.loads(line) for line in file]
            for stage in stages:
                bluff_prob = bluff_prob_dict[stage][player]
                bluff = get_bluff_boolean(bluff_prob)
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
                            else: 
                                if action == 'c':
                                    if win_prob >= 0.5:
                                        optimal_betting_amount = bet_size
                                        adjusted_betting_amount = compute_adjusted_betting_amount(variable_type, optimal_betting_amount, True)
                                        stage_betting_amounts.append(adjusted_betting_amount)
                                        will_continue = False
                                else:
                                    optimal_betting_amount = win_prob * pot / (1 - win_prob)
                        
                        if will_continue:
                            adjusted_betting_amount = compute_adjusted_betting_amount(variable_type, optimal_betting_amount, False)
                            if adjusted_betting_amount < 10 and bluff and win_prob < 0.3:
                                adjusted_betting_amount = (1 - win_prob) * pot / win_prob
                            # Add noise
                            adjusted_betting_amount_with_noise = add_noise(adjusted_betting_amount, variable_type)

                            if adjusted_betting_amount_with_noise < 0:
                                adjusted_betting_amount_with_noise = 0
                            stage_betting_amounts.append(adjusted_betting_amount_with_noise)

                betting_amounts["data"][stage] = stage_betting_amounts

        with open(f'/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/analysis_and_modeling/data/betting_amounts{player}.json', 'a') as json_file:
            data_to_write = betting_amounts
            json_file.write(json.dumps(data_to_write) + '\n') 
        print(f"processed {player}")
                    

if __name__ == "__main__":
    variable_type_list = ["optimal", "over_confidence", "under_confidence"]
    variable_type = "under_confidence"
    simulate_generative_model(variable_type)
    print("DONE!")

"""
WHEN DATA is NONE:
when the action is undefined
or
when the win prob is 1 or 0 -> you can bet however much you want or never bet: deterministic

variables I can change to make the model predict human behavior better:
- noise

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

