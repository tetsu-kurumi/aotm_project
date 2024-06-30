import json
import matplotlib.pyplot as plt

def create_histogram(data, bins=1000):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

def create_histogram_no_zero(data, bins_increment=10):
    filtered_data = [x for x in data if x != 0]  # Remove zeros
    max_value = max(filtered_data)
    bins = list(range(0, int(max_value) + bins_increment, bins_increment))
    plt.hist(filtered_data, bins=bins, edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

DATA_FOLDER = '/Users/tetsu/Documents/School/Class/CGSC 472/aotm_project/data'
HAND_NUM_DICT = {'sagerbot': 9111, 'jvegas2': 5738, 'BlackBart': 5148, 'MegaHertz': 4076, 'DrOakland': 3998, 'RiverRatt': 3805, 'show': 3780, 'Rumford': 3536, 'Benway': 3340, 'kk': 2959, 'Swagger': 2923, 'CybrTigr': 2902, 'lexstraus': 2884, 'Gabe': 2599, 'kfish': 2451, 'Benja': 2390, 'Muck': 2383, 'going': 2379, 'exosis': 2338, 'Blaze': 2283, 'num': 2244, 'FX': 2232, 'DP': 2220, 'rivrgod': 2186, 'beaty': 2176, 'CFigor': 2175, 'Sonar': 2160, 'neverx': 2158, 'Sham': 2031, 'Nermal': 1976, 'mt': 1902, 'lilly': 1898, 'tvp': 1797, 'po147': 1780, 'Quick': 1764, 'bigkicker': 1763, 'Patti': 1762, 'theking': 1761, 'superman': 1746, 'fuhzee': 1741, 'KisMyAce': 1718, 'DM': 1708, 'evercall': 1683, 'coming': 1675, 'condor': 1672, 'Harry^T': 1665, 'Winner666': 1634, 'Funky': 1599, 'gsr': 1580, 'carrot': 1540, 'spew-boy': 1525, 'K6': 1493, 'Grizz': 1485, 'RiverMan': 1455, 'is314onu': 1454, 'robw': 1443, 'gfw': 1421, 'Zag': 1407, 'EmtaE': 1407, 'sass': 1358, 'GAR2': 1358, 'Flash_man': 1338, 'reTTard': 1332, 'Zwierdo': 1317, 'Gremlin': 1315, 'gustav': 1303, 'numskull': 1301, 'panfried': 1298, 'ile': 1291, 'keeae': 1290, 'Eldon': 1290, 'Kevin_Un': 1260, 'perfecdoh': 1213, 'Massa': 1195, 'tilted': 1183, 'Sakura': 1156, 'tctim': 1125, 'donguy': 1112, 'Muck_It': 1099, 'Voyeur': 1085, 'JKhearts': 1079, 'Gunshot': 1077, 'Patoot': 1075, 'alfalfa': 1056, 'zxc': 1052, 'ChrisLinn': 1048, 'JADC': 1044, 'SnakeEyes': 1036, 'azspinner': 1032, 'brian': 1017, 'snoball': 1015, 'DopeyTwat': 1009, '__': 1008, 'TripSixes': 1004}
STAGES = ["f", "t", "r"]

bet_to_pot_f_list = []
bet_to_pot_t_list = []
bet_to_pot_r_list = []
bet_to_pot_lists = [bet_to_pot_f_list, bet_to_pot_t_list, bet_to_pot_r_list]

for player in HAND_NUM_DICT:
    filepath = f'{DATA_FOLDER}/data_per_player/data_{player}.json'
    with open(filepath, 'r') as file:
        handlist = [json.loads(line) for line in file]
    for hand in handlist:
        win_prob_to_bet_info = hand["win_prob_to_bet_info"]

        for idx, stage in enumerate(STAGES):
            bet_info = win_prob_to_bet_info[stage]["bet_info"]
            bet_to_pot = bet_info[stage]["bet_info"]["betsize_to_pot"]
            
            # if 
            # bet_to_pot_lists[idx].append(bet_to_pot)

# Example usage:
create_histogram_no_zero(bet_to_pot_f)
    