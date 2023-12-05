import json

def bluff_rate(data_list, stage):
    bluff_count = 0
    total_count = len(data_list)
    if stage == "f":
        for data in data_list:
            if data["win_prob_to_bet_info"]["f"]["winprob"] <= 0.25 and data["win_prob_to_bet_info"]["f"]["bet_info"]["betsize"] > 0:
                bluff_count += 1
        bluff_rate = bluff_count/total_count
        return bluff_rate
    if stage == "t":
        for data in data_list:
            if data["win_prob_to_bet_info"]["t"]["winprob"] <= 0.25 and data["win_prob_to_bet_info"]["t"]["bet_info"]["betsize"] > 0:
                bluff_count += 1
        bluff_rate = bluff_count/total_count
        return bluff_rate
    if stage == "r":
        for data in data_list:
            if data["win_prob_to_bet_info"]["r"]["winprob"] <= 0.25 and data["win_prob_to_bet_info"]["r"]["bet_info"]["betsize"] > 0:
                bluff_count += 1
        bluff_rate = bluff_count/total_count
        return bluff_rate
    

def calculate_bluff_rate():
    stages = ["f", "t", "r"]
    bluff_rate_dict = {'f': {},'t': {}, 'r': {}}
    for player in players:
        file_path = f'/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/data/data_per_player/data_{player}.json'
        with open(file_path, 'r') as file:
            data_list = [json.loads(line) for line in file]
            for stage in stages:
                bluff_rate_dict['f'][player] = bluff_rate(data_list, stage)
                bluff_rate_dict['r'][player] = bluff_rate(data_list, stage)
                bluff_rate_dict['t'][player] = bluff_rate(data_list, stage)
    return bluff_rate_dict

if __name__ == "__main__":
    players={'sagerbot': 9111, 'jvegas2': 5738, 'BlackBart': 5148, 'MegaHertz': 4076, 'DrOakland': 3998, 'RiverRatt': 3805, 'show': 3780, 'Rumford': 3536, 'Benway': 3340, 'kk': 2959, 'Swagger': 2923, 'CybrTigr': 2902, 'lexstraus': 2884, 'Gabe': 2599, 'kfish': 2451, 'Benja': 2390, 'Muck': 2383, 'going': 2379, 'exosis': 2338, 'Blaze': 2283, 'num': 2244, 'FX': 2232, 'DP': 2220, 'rivrgod': 2186, 'beaty': 2176, 'CFigor': 2175, 'Sonar': 2160, 'neverx': 2158, 'Sham': 2031, 'Nermal': 1976, 'mt': 1902, 'lilly': 1898, 'tvp': 1797, 'po147': 1780, 'Quick': 1764, 'bigkicker': 1763, 'Patti': 1762, 'theking': 1761, 'superman': 1746, 'fuhzee': 1741, 'KisMyAce': 1718, 'DM': 1708, 'evercall': 1683, 'coming': 1675, 'condor': 1672, 'Harry^T': 1665, 'Winner666': 1634, 'Funky': 1599, 'gsr': 1580, 'carrot': 1540, 'spew-boy': 1525, 'K6': 1493, 'Grizz': 1485, 'RiverMan': 1455, 'is314onu': 1454, 'robw': 1443, 'gfw': 1421, 'Zag': 1407, 'EmtaE': 1407, 'sass': 1358, 'GAR2': 1358, 'Flash_man': 1338, 'reTTard': 1332, 'Zwierdo': 1317, 'Gremlin': 1315, 'gustav': 1303, 'numskull': 1301, 'panfried': 1298, 'ile': 1291, 'keeae': 1290, 'Eldon': 1290, 'Kevin_Un': 1260, 'perfecdoh': 1213, 'Massa': 1195, 'tilted': 1183, 'Sakura': 1156, 'tctim': 1125, 'donguy': 1112, 'Muck_It': 1099, 'Voyeur': 1085, 'JKhearts': 1079, 'Gunshot': 1077, 'Patoot': 1075, 'alfalfa': 1056, 'zxc': 1052, 'ChrisLinn': 1048, 'JADC': 1044, 'SnakeEyes': 1036, 'azspinner': 1032, 'brian': 1017, 'snoball': 1015, 'DopeyTwat': 1009, '__': 1008, 'TripSixes': 1004}
    print(calculate_bluff_rate())
