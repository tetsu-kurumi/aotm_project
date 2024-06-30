# For correlation analysis
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

DATA_FOLDER = '/Users/tetsu/Documents/School/Class/CGSC 472/aotm_project/data'
SIMULATION_RESULTS_FOLDER = f'{DATA_FOLDER}/simulation_results'

HAND_NUM_DICT = {'sagerbot': 9111, 'jvegas2': 5738, 'BlackBart': 5148, 'MegaHertz': 4076, 'DrOakland': 3998, 'RiverRatt': 3805, 'show': 3780, 'Rumford': 3536, 'Benway': 3340, 'kk': 2959, 'Swagger': 2923, 'CybrTigr': 2902, 'lexstraus': 2884, 'Gabe': 2599, 'kfish': 2451, 'Benja': 2390, 'Muck': 2383, 'going': 2379, 'exosis': 2338, 'Blaze': 2283, 'num': 2244, 'FX': 2232, 'DP': 2220, 'rivrgod': 2186, 'beaty': 2176, 'CFigor': 2175, 'Sonar': 2160, 'neverx': 2158, 'Sham': 2031, 'Nermal': 1976, 'mt': 1902, 'lilly': 1898, 'tvp': 1797, 'po147': 1780, 'Quick': 1764, 'bigkicker': 1763, 'Patti': 1762, 'theking': 1761, 'superman': 1746, 'fuhzee': 1741, 'KisMyAce': 1718, 'DM': 1708, 'evercall': 1683, 'coming': 1675, 'condor': 1672, 'Harry^T': 1665, 'Winner666': 1634, 'Funky': 1599, 'gsr': 1580, 'carrot': 1540, 'spew-boy': 1525, 'K6': 1493, 'Grizz': 1485, 'RiverMan': 1455, 'is314onu': 1454, 'robw': 1443, 'gfw': 1421, 'Zag': 1407, 'EmtaE': 1407, 'sass': 1358, 'GAR2': 1358, 'Flash_man': 1338, 'reTTard': 1332, 'Zwierdo': 1317, 'Gremlin': 1315, 'gustav': 1303, 'numskull': 1301, 'panfried': 1298, 'ile': 1291, 'keeae': 1290, 'Eldon': 1290, 'Kevin_Un': 1260, 'perfecdoh': 1213, 'Massa': 1195, 'tilted': 1183, 'Sakura': 1156, 'tctim': 1125, 'donguy': 1112, 'Muck_It': 1099, 'Voyeur': 1085, 'JKhearts': 1079, 'Gunshot': 1077, 'Patoot': 1075, 'alfalfa': 1056, 'zxc': 1052, 'ChrisLinn': 1048, 'JADC': 1044, 'SnakeEyes': 1036, 'azspinner': 1032, 'brian': 1017, 'snoball': 1015, 'DopeyTwat': 1009, '__': 1008, 'TripSixes': 1004}
WIN_RATE_DICT = {'azspinner': 0.6327519379844961, 'CFigor': 0.6212259835315646, 'perfecdoh': 0.6202635914332785, 'keeae': 0.6077519379844961, 'DopeyTwat': 0.597621407333994, 'fuhzee': 0.5939115450890293, 'carrot': 0.5896103896103896, 'JKhearts': 0.58758109360519, 'kfish': 0.5866286180187525, 'gfw': 0.5833919774806474, 'sagerbot': 0.582638279192274, 'Gabe': 0.5821469796075414, 'panfried': 0.5816640986132512, 'coming': 0.5785074626865672, 'Funky': 0.5784865540963102, 'ile': 0.5770720371804803, 'ChrisLinn': 0.5752380952380952, 'gsr': 0.5743200506008855, 'DrOakland': 0.5735367683841921, 'mt': 0.5720294426919033, 'BlackBart': 0.5719557195571956, 'Benja': 0.5706521739130435, 'lexstraus': 0.5693481276005548, 'sass': 0.569219440353461, 'beaty': 0.5691318327974276, 'neverx': 0.5690454124189064, 'JADC': 0.5689655172413793, 'Blaze': 0.5676741130091985, 'lilly': 0.5666140073723012, 'SnakeEyes': 0.5660559305689489, 'is314onu': 0.5660247592847317, 'Harry^T': 0.5654261704681873, 'Patoot': 0.5650557620817844, 'Sakura': 0.5579584775086506, 'TripSixes': 0.5577689243027888, 'tctim': 0.5564444444444444, 'Zwierdo': 0.5546282245827011, 'Zag': 0.5525568181818182, 'evercall': 0.5519904931669638, 'K6': 0.5508701472556894, '__': 0.5490584737363726, 'snoball': 0.548768472906404, 'gustav': 0.5479662317728319, 'Massa': 0.5464435146443515, 'Rumford': 0.5452488687782805, 'tvp': 0.5447968836950473, 'superman': 0.5440503432494279, 'DM': 0.5433255269320844, 'going': 0.5418242959226566, 'condor': 0.5406698564593302, 'Gunshot': 0.5403899721448467, 'show': 0.5396825396825397, 'jvegas2': 0.5396410524481617, 'FX': 0.5394265232974911, 'GAR2': 0.5382916053019146, 'alfalfa': 0.5369318181818182, 'bigkicker': 0.5368480725623582, 'Eldon': 0.5348837209302325, 'CybrTigr': 0.5339304168101964, 'Sham': 0.533727227966519, 'Voyeur': 0.5336405529953917, 'RiverMan': 0.5333333333333333, 'Nermal': 0.5323886639676113, 'MegaHertz': 0.5321393523061825, 'Gremlin': 0.5300380228136882, 'DP': 0.5294912201710941, 'Muck': 0.5289429530201343, 'reTTard': 0.524024024024024, 'Patti': 0.5238365493757094, 'EmtaE': 0.5238095238095238, 'Kevin_Un': 0.5238095238095238, 'Muck_It': 0.521383075523203, 'robw': 0.5204435204435205, 'RiverRatt': 0.5198423127463864, 'Benway': 0.5176646706586826, 'donguy': 0.5148247978436657, 'numskull': 0.5142198308993082, 'kk': 0.5126732004055424, 'rivrgod': 0.5125743026977595, 'Flash_man': 0.5123226288274833, 'KisMyAce': 0.5119255381035486, 'Sonar': 0.5099490976399815, 'Grizz': 0.5057162071284466, 'Quick': 0.5045351473922902, 'brian': 0.504424778761062, 'zxc': 0.502851711026616, 'num': 0.5026737967914439, 'Swagger': 0.49948682860075266, 'tilted': 0.49831365935919053, 'spew-boy': 0.49508196721311476, 'exosis': 0.490590248075278, 'Winner666': 0.4804161566707466, 'po147': 0.47808988764044946, 'theking': 0.4699546485260771}
PLAYER_LIST = list(WIN_RATE_DICT.keys())
STAGES = ["f", "t", "r"]
VERSION = 13
PLOT = True
SAVE = False

check_list = []
coefficient_list = []
pvalue_list = []
lines = []
lines.append(f'Version {VERSION}\n\n')

class Correlation:
    def __init__(self, players_of_interest):
        self.obslist_f = []
        self.simlist_f = []
        self.obslist_t = []
        self.simlist_t = []
        self.obslist_r = []
        self.simlist_r = []

        for player in players_of_interest:
            obs_file_path = f'{SIMULATION_RESULTS_FOLDER}/ver_{VERSION}/ver_{VERSION}_obsvalues_{player}.json'
            sim_file_path = f'{SIMULATION_RESULTS_FOLDER}/ver_{VERSION}/ver_{VERSION}_simvalues_{player}.json'
            with open(obs_file_path, 'r') as obs_file:
                obs_list = [json.loads(line) for line in obs_file]
            with open(sim_file_path, 'r') as sim_file:
                sim_list = [json.loads(line) for line in sim_file]
            
            for idx, line in enumerate(sim_list):
                match line['stage']:
                    case 'f':
                        if line['data'] is not None:
                            self.simlist_f.append(line['data'])
                            self.obslist_f.append(obs_list[idx]['data'])
                    case 't':
                        if line['data'] is not None:
                            self.simlist_t.append(line['data'])
                            self.obslist_t.append(obs_list[idx]['data'])
                    case 'r':
                        if line['data'] is not None:
                            self.simlist_r.append(line['data'])
                            self.obslist_r.append(obs_list[idx]['data'])

        print('self.obslist_f:', self.obslist_f[:100])
        print('self.simlist_f:', self.simlist_f[:100])
        print('self.obslist_t:', self.obslist_t[:100])
        print('self.simlist_t:', self.simlist_t[:100])
        print('self.obslist_r:', self.obslist_r[:100])
        print('self.simlist_r:', self.simlist_r[:100])

        self.mae_f = None
        self.correlation_coefficient_f = None
        self.p_value_f = None
        self.mae_t = None
        self.correlation_coefficient_t = None
        self.p_value_t = None
        self.mae_r = None
        self.correlation_coefficient_r = None
        self.p_value_r = None

    def run(self):
        self.mae_f = self.calculate_mae('f')
        self.correlation_coefficient_f, self.p_value_f = self.calculate_correlation('f')
        self.mae_t = self.calculate_mae('t')
        self.correlation_coefficient_t, self.p_value_t = self.calculate_correlation('t')
        self.mae_r = self.calculate_mae('r')
        self.correlation_coefficient_r, self.p_value_r = self.calculate_correlation('r')

        num_zeros = sum(1 for item in self.obslist_r if item == 0)
        check_per = (num_zeros / len(self.obslist_r)) * 100
        check_list.append(check_per)
        coefficient_list.append(self.correlation_coefficient_r)
        pvalue_list.append(self.p_value_r)

    def calculate_correlation(self, stage):
        match stage:
            case 'f':
                observation = self.obslist_f
                model_output = self.simlist_f
            case 't':
                observation = self.obslist_t
                model_output = self.simlist_t
            case 'r':
                observation = self.obslist_r
                model_output = self.simlist_r

        # Check if both lists are of the same length
        if len(observation) != len(model_output):
            raise ValueError("Both lists must be of the same length")

        # Calculate Pearson correlation coefficient and p-value
        correlation_coefficient, p_value = pearsonr(observation, model_output)

        return correlation_coefficient, p_value

    def calculate_mae(self, stage):
        match stage:
            case 'f':
                observation = self.obslist_f
                model_output = self.simlist_f
            case 't':
                observation = self.obslist_t
                model_output = self.simlist_t
            case 'r':
                observation = self.obslist_r
                model_output = self.simlist_r
        # Check if both lists are of the same length
        if len(observation) != len(model_output):
            raise ValueError("Both lists must be of the same length")
        # Calculate absolute differences
        absolute_diff = [abs(actual - predicted) for actual, predicted in zip(observation, model_output)]
        # Calculate MAE
        mae = sum(absolute_diff) / len(observation)
        return mae
    
    def save(self, player_num):
        lines.append(f'Result for top {player_num} players\n')
        lines.append(f'self.mae_f: {self.mae_f:.5f}\n')
        lines.append(f'self.correlation_coefficient_f: {self.correlation_coefficient_f:.5f}\n')
        lines.append(f'self.p_value_f: {self.p_value_f:.10f}\n')
        lines.append(f'self.mae_t: {self.mae_t:.5f}\n')
        lines.append(f'self.correlation_coefficient_t: {self.correlation_coefficient_t:.5f}\n')
        lines.append(f'self.p_value_t: {self.p_value_t:.10f}\n')
        lines.append(f'self.mae_r: {self.mae_r:.5f}\n')
        lines.append(f'self.correlation_coefficient_r: {self.correlation_coefficient_r:.5f}\n')
        lines.append(f'self.p_value_r: {self.p_value_r:.10f}\n\n')

        print(f'Result for top {player_num} players')
        print(f'self.mae_f: {self.mae_f:.5f}')
        print(f'self.correlation_coefficient_f: {self.correlation_coefficient_f:.5f}')
        print(f'self.p_value_f: {self.p_value_f:.10f}')
        print(f'self.mae_t: {self.mae_t:.5f}')
        print(f'self.correlation_coefficient_t: {self.correlation_coefficient_t:.5f}')
        print(f'self.p_value_t: {self.p_value_t:.10f}')
        print(f'self.mae_r: {self.mae_r:.5f}')
        print(f'self.correlation_coefficient_r: {self.correlation_coefficient_r:.5f}')
        print(f'self.p_value_r: {self.p_value_r:.10f}')

        
        if PLOT:
            simlist = self.simlist_f
            obslist = self.obslist_f

            plt.scatter(obslist, simlist)
            plt.plot(np.unique(obslist), np.unique(obslist), color='red', linestyle='--')  # Perfect correlation line
            plt.xlabel('Obs')
            plt.ylabel('Sim')
            plt.title('Correlation between observed and simulated value')
            plt.grid(True)
            plt.show()

def main():
    player_num_list = [94, 50, 25, 10]
    # '/Users/tetsu/Documents/School/Class/CGSC 472/aotm_project/data/correlation_info.txt'
    for n in player_num_list:
        players_of_interest = PLAYER_LIST[:n]
        correlation = Correlation(players_of_interest)
        correlation.run()
        correlation.save(n)
    
    if SAVE:
        # Store params in version_info.txt for cross reference
        with open(f'{DATA_FOLDER}/correlation_info.txt', "a") as file:
            lines.append('-----------------------------------------------------------\n\n')
            file.writelines(lines)

    # for player in PLAYER_LIST[:10]:
    #     print(f"Processing {player}")
    #     players_of_interest = [player]
    #     correlation = Correlation(players_of_interest)
    #     correlation.run()
    #     correlation.save(1)

    # correlation_coefficient, p_value = pearsonr(check_list, coefficient_list)
    # print('')
    # print(f'COEFFICIENT: {correlation_coefficient}')
    # print(f'p-value: {p_value}')
    
    # plt.scatter(check_list, coefficient_list)
    # plt.xlabel('check percentage')
    # plt.ylabel('correlation coefficient')
    # plt.grid(True)
    # plt.show()
        
    # count = 0
    # sig_coefficient_list = []
    # for idx, pvalue in enumerate(pvalue_list):
    #     if pvalue < 0.05:
    #         sig_coefficient_list.append(coefficient_list[idx])
    #         count += 1
    
    # print(f'Significant Percentage: {count/10}')
    # plt.hist(sig_coefficient_list, bins=50, edgecolor='black') 
    # plt.xlabel('Value')
    # plt.ylabel('Frequency')
    # plt.title('Top 10 Players')
    # plt.grid(True)
    # plt.show()

    

    
if __name__ == "__main__":
    main()

