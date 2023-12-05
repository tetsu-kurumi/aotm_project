# Check how much null there is in each stage (if too much, don't use data)
import scipy.stats as stats
import json
import numpy as np

def calculate_correlation(observation, model_output):
    # Check if both lists are of the same length
    if len(observation) != len(model_output):
        raise ValueError("Both lists must be of the same length")

    # Calculate Pearson correlation coefficient and p-value
    correlation_coefficient, p_value = stats.pearsonr(observation, model_output)

    return correlation_coefficient, p_value

def calculate_mae(observation, model_output):
    # Check if both lists are of the same length
    if len(observation) != len(model_output):
        raise ValueError("Both lists must be of the same length")

    # Calculate absolute differences
    absolute_diff = [abs(actual - predicted) for actual, predicted in zip(observation, model_output)]

    # Calculate MAE
    mae = sum(absolute_diff) / len(observation)
    
    return mae

def remove_nulls(list):
    return [x for x in list if x is not None]

def data_interaction(data_list):
    stages = ["f", "t", "r"]
    interaction_dict = {}
    for stage in stages:
        for entry in data_list:
            if entry["variable_type"] == "observation":
                observation_betsize_list = entry["data"][stage]
                observation_betsize_list = remove_nulls(observation_betsize_list)
            if entry["variable_type"] == "optimal":
                model_betsize_list = entry["data"][stage]
                model_betsize_list = remove_nulls(model_betsize_list)
            
        correlation_coefficient, p_value = calculate_correlation(observation_betsize_list, model_betsize_list)
        mae = calculate_mae(observation_betsize_list, model_betsize_list)

        interaction_dict[stage] = {}
        interaction_dict[stage]['mae'] = mae
        interaction_dict[stage]['correlation_coefficient'] = correlation_coefficient
        interaction_dict[stage]['p_value'] = p_value

    return interaction_dict

if __name__ == "__main__":
    stages = ["f", "t", "r"]
    hand_num_dict = {'sagerbot': 9111, 'jvegas2': 5738, 'BlackBart': 5148, 'MegaHertz': 4076, 'DrOakland': 3998, 'RiverRatt': 3805, 'show': 3780, 'Rumford': 3536, 'Benway': 3340, 'kk': 2959, 'Swagger': 2923, 'CybrTigr': 2902, 'lexstraus': 2884, 'Gabe': 2599, 'kfish': 2451, 'Benja': 2390, 'Muck': 2383, 'going': 2379, 'exosis': 2338, 'Blaze': 2283, 'num': 2244, 'FX': 2232, 'DP': 2220, 'rivrgod': 2186, 'beaty': 2176, 'CFigor': 2175, 'Sonar': 2160, 'neverx': 2158, 'Sham': 2031, 'Nermal': 1976, 'mt': 1902, 'lilly': 1898, 'tvp': 1797, 'po147': 1780, 'Quick': 1764, 'bigkicker': 1763, 'Patti': 1762, 'theking': 1761, 'superman': 1746, 'fuhzee': 1741, 'KisMyAce': 1718, 'DM': 1708, 'evercall': 1683, 'coming': 1675, 'condor': 1672, 'Harry^T': 1665, 'Winner666': 1634, 'Funky': 1599, 'gsr': 1580, 'carrot': 1540, 'spew-boy': 1525, 'K6': 1493, 'Grizz': 1485, 'RiverMan': 1455, 'is314onu': 1454, 'robw': 1443, 'gfw': 1421, 'Zag': 1407, 'EmtaE': 1407, 'sass': 1358, 'GAR2': 1358, 'Flash_man': 1338, 'reTTard': 1332, 'Zwierdo': 1317, 'Gremlin': 1315, 'gustav': 1303, 'numskull': 1301, 'panfried': 1298, 'ile': 1291, 'keeae': 1290, 'Eldon': 1290, 'Kevin_Un': 1260, 'perfecdoh': 1213, 'Massa': 1195, 'tilted': 1183, 'Sakura': 1156, 'tctim': 1125, 'donguy': 1112, 'Muck_It': 1099, 'Voyeur': 1085, 'JKhearts': 1079, 'Gunshot': 1077, 'Patoot': 1075, 'alfalfa': 1056, 'zxc': 1052, 'ChrisLinn': 1048, 'JADC': 1044, 'SnakeEyes': 1036, 'azspinner': 1032, 'brian': 1017, 'snoball': 1015, 'DopeyTwat': 1009, '__': 1008, 'TripSixes': 1004}
    #hand_num_dict = {'sagerbot': 9111}

    interaction_dicts = {}
    for player in hand_num_dict:
        file_path = f'/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/analysis_and_modeling/data/betting_amounts{player}.json'
        with open(file_path, 'r') as file:
            data_list = [json.loads(line) for line in file]
            interaction_dict = data_interaction(data_list)
        interaction_dicts[player] = interaction_dict

    player_of_interest_dict = {'azspinner': 0.6327519379844961, 'CFigor': 0.6212259835315646, 'perfecdoh': 0.6202635914332785, 'keeae': 0.6077519379844961, 'DopeyTwat': 0.597621407333994, 'fuhzee': 0.5939115450890293, 'carrot': 0.5896103896103896, 'JKhearts': 0.58758109360519, 'kfish': 0.5866286180187525, 'gfw': 0.5833919774806474, 'sagerbot': 0.582638279192274, 'Gabe': 0.5821469796075414, 'panfried': 0.5816640986132512, 'coming': 0.5785074626865672, 'Funky': 0.5784865540963102, 'ile': 0.5770720371804803, 'ChrisLinn': 0.5752380952380952, 'gsr': 0.5743200506008855, 'DrOakland': 0.5735367683841921, 'mt': 0.5720294426919033, 'BlackBart': 0.5719557195571956, 'Benja': 0.5706521739130435, 'lexstraus': 0.5693481276005548, 'sass': 0.569219440353461, 'beaty': 0.5691318327974276, 'neverx': 0.5690454124189064, 'JADC': 0.5689655172413793, 'Blaze': 0.5676741130091985, 'lilly': 0.5666140073723012, 'SnakeEyes': 0.5660559305689489, 'is314onu': 0.5660247592847317, 'Harry^T': 0.5654261704681873, 'Patoot': 0.5650557620817844, 'Sakura': 0.5579584775086506, 'TripSixes': 0.5577689243027888, 'tctim': 0.5564444444444444, 'Zwierdo': 0.5546282245827011, 'Zag': 0.5525568181818182, 'evercall': 0.5519904931669638, 'K6': 0.5508701472556894, '__': 0.5490584737363726, 'snoball': 0.548768472906404, 'gustav': 0.5479662317728319, 'Massa': 0.5464435146443515, 'Rumford': 0.5452488687782805, 'tvp': 0.5447968836950473, 'superman': 0.5440503432494279, 'DM': 0.5433255269320844, 'going': 0.5418242959226566, 'condor': 0.5406698564593302, 'Gunshot': 0.5403899721448467, 'show': 0.5396825396825397, 'jvegas2': 0.5396410524481617, 'FX': 0.5394265232974911, 'GAR2': 0.5382916053019146, 'alfalfa': 0.5369318181818182, 'bigkicker': 0.5368480725623582, 'Eldon': 0.5348837209302325, 'CybrTigr': 0.5339304168101964, 'Sham': 0.533727227966519, 'Voyeur': 0.5336405529953917, 'RiverMan': 0.5333333333333333, 'Nermal': 0.5323886639676113, 'MegaHertz': 0.5321393523061825, 'Gremlin': 0.5300380228136882, 'DP': 0.5294912201710941, 'Muck': 0.5289429530201343, 'reTTard': 0.524024024024024, 'Patti': 0.5238365493757094, 'EmtaE': 0.5238095238095238, 'Kevin_Un': 0.5238095238095238, 'Muck_It': 0.521383075523203, 'robw': 0.5204435204435205, 'RiverRatt': 0.5198423127463864, 'Benway': 0.5176646706586826, 'donguy': 0.5148247978436657, 'numskull': 0.5142198308993082, 'kk': 0.5126732004055424, 'rivrgod': 0.5125743026977595, 'Flash_man': 0.5123226288274833, 'KisMyAce': 0.5119255381035486, 'Sonar': 0.5099490976399815, 'Grizz': 0.5057162071284466, 'Quick': 0.5045351473922902, 'brian': 0.504424778761062, 'zxc': 0.502851711026616, 'num': 0.5026737967914439, 'Swagger': 0.49948682860075266, 'tilted': 0.49831365935919053, 'spew-boy': 0.49508196721311476, 'exosis': 0.490590248075278, 'Winner666': 0.4804161566707466, 'po147': 0.47808988764044946, 'theking': 0.4699546485260771}
    player_of_interest = list(player_of_interest_dict.keys())
    player_num_list = [94, 50, 25, 10]
    

    for n in player_num_list:
        mae_total_f = 0
        correlation_coefficient_total_f = []
        p_values_f = 0
        mae_total_t = 0
        correlation_coefficient_total_t = []
        p_values_t = 0
        mae_total_r = 0
        correlation_coefficient_total_r = []
        p_values_r = 0
        player_of_interest = player_of_interest[:n]
        for player in player_of_interest:
            mae_total_f += interaction_dicts[player]['f']['mae']
            mae_total_t += interaction_dicts[player]['t']['mae']
            mae_total_r += interaction_dicts[player]['r']['mae']
            correlation_coefficient_total_f.append(interaction_dicts[player]['f']['correlation_coefficient'])
            correlation_coefficient_total_t.append(interaction_dicts[player]['t']['correlation_coefficient'])
            correlation_coefficient_total_r.append(interaction_dicts[player]['r']['correlation_coefficient'])
            p_values_f += interaction_dicts[player]['f']['p_value']
            p_values_t += interaction_dicts[player]['t']['p_value']
            p_values_r += interaction_dicts[player]['r']['p_value']

        total = len(player_of_interest)
        avg_mae_f = mae_total_f/total
        avg_mae_t = mae_total_t/total
        avg_mae_r = mae_total_r/total
        # Apply Fisher's Z transformation
        avg_correlation_coefficient_f = np.tanh(np.mean(np.arctanh(correlation_coefficient_total_f)))
        avg_correlation_coefficient_t = np.tanh(np.mean(np.arctanh(correlation_coefficient_total_t)))
        avg_correlation_coefficient_r = np.tanh(np.mean(np.arctanh(correlation_coefficient_total_r))) #correlation_coefficient_total_r/total
        
        # avg_p_value_f = stats.combine_pvalues(p_values_f, method='fisher', weights=None)
        # avg_p_value_t = stats.combine_pvalues(p_values_t, method='fisher', weights=None)
        # avg_p_value_r = stats.combine_pvalues(p_values_r, method='fisher', weights=None)


        avg_p_value_f = p_values_f/total
        avg_p_value_t = p_values_t/total
        avg_p_value_r = p_values_r/total
        #print(interaction_dicts)
        print("player_of_interest:", player_of_interest)
        print("top", total, "players")

        print("avg_mae_f", avg_mae_f)
        print("avg_mae_t", avg_mae_t)
        print("avg_mae_r", avg_mae_r)
        print("avg_correlation_coefficient_f", avg_correlation_coefficient_f)
        print("avg_correlation_coefficient_t", avg_correlation_coefficient_t)
        print("avg_correlation_coefficient_r", avg_correlation_coefficient_r)
        print("avg_p_value_f", avg_p_value_f)
        print("avg_p_value_t", avg_p_value_t)
        print("avg_p_value_r", avg_p_value_r)
