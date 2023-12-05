# Check how much null there is in each stage (if too much, don't use data)
import scipy.stats as stats
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def remove_nulls(list):
    return [x for x in list if x is not None]

def plot():

    # Data
    metrics = ['avg_correlation_coefficient_t', 'avg_correlation_coefficient_r', 'avg_p_value_t', 'avg_p_value_r']
    categories = ['All Players', 'Top 10 Players']

    data_top_94 = [0.2604, 0.2346, 0.0793, 0.0670]

    # Data for Top 10 Players
    data_top_10 = [0.2864, 0.2792, 5.45e-05, 0.0020]

    # Set up positions for bars
    bar_width = 0.35
    bar_positions_top_94 = np.arange(len(metrics))
    bar_positions_top_10 = bar_positions_top_94 + bar_width

    # Plot grouped bar charts
    plt.figure(figsize=(8, 4))
    plt.bar(bar_positions_top_94, data_top_94, width=bar_width, color='blue', alpha=0.7, label='Top 94 Players')
    plt.bar(bar_positions_top_10, data_top_10, width=bar_width, color='orange', alpha=0.7, label='Top 10 Players')

    # Customize the plot
    plt.title('Metrics for All and Top 10 Players')
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.xticks(bar_positions_top_94 + bar_width / 2, metrics)
    plt.legend()

    # Show the plot
    plt.show()
    """
    player_of_interest_dict = {'azspinner': 0.6327519379844961, 'CFigor': 0.6212259835315646, 'perfecdoh': 0.6202635914332785, 'keeae': 0.6077519379844961, 'DopeyTwat': 0.597621407333994, 'fuhzee': 0.5939115450890293, 'carrot': 0.5896103896103896, 'JKhearts': 0.58758109360519, 'kfish': 0.5866286180187525, 'gfw': 0.5833919774806474, 'sagerbot': 0.582638279192274, 'Gabe': 0.5821469796075414, 'panfried': 0.5816640986132512, 'coming': 0.5785074626865672, 'Funky': 0.5784865540963102, 'ile': 0.5770720371804803, 'ChrisLinn': 0.5752380952380952, 'gsr': 0.5743200506008855, 'DrOakland': 0.5735367683841921, 'mt': 0.5720294426919033, 'BlackBart': 0.5719557195571956, 'Benja': 0.5706521739130435, 'lexstraus': 0.5693481276005548, 'sass': 0.569219440353461, 'beaty': 0.5691318327974276, 'neverx': 0.5690454124189064, 'JADC': 0.5689655172413793, 'Blaze': 0.5676741130091985, 'lilly': 0.5666140073723012, 'SnakeEyes': 0.5660559305689489, 'is314onu': 0.5660247592847317, 'Harry^T': 0.5654261704681873, 'Patoot': 0.5650557620817844, 'Sakura': 0.5579584775086506, 'TripSixes': 0.5577689243027888, 'tctim': 0.5564444444444444, 'Zwierdo': 0.5546282245827011, 'Zag': 0.5525568181818182, 'evercall': 0.5519904931669638, 'K6': 0.5508701472556894, '__': 0.5490584737363726, 'snoball': 0.548768472906404, 'gustav': 0.5479662317728319, 'Massa': 0.5464435146443515, 'Rumford': 0.5452488687782805, 'tvp': 0.5447968836950473, 'superman': 0.5440503432494279, 'DM': 0.5433255269320844, 'going': 0.5418242959226566, 'condor': 0.5406698564593302, 'Gunshot': 0.5403899721448467, 'show': 0.5396825396825397, 'jvegas2': 0.5396410524481617, 'FX': 0.5394265232974911, 'GAR2': 0.5382916053019146, 'alfalfa': 0.5369318181818182, 'bigkicker': 0.5368480725623582, 'Eldon': 0.5348837209302325, 'CybrTigr': 0.5339304168101964, 'Sham': 0.533727227966519, 'Voyeur': 0.5336405529953917, 'RiverMan': 0.5333333333333333, 'Nermal': 0.5323886639676113, 'MegaHertz': 0.5321393523061825, 'Gremlin': 0.5300380228136882, 'DP': 0.5294912201710941, 'Muck': 0.5289429530201343, 'reTTard': 0.524024024024024, 'Patti': 0.5238365493757094, 'EmtaE': 0.5238095238095238, 'Kevin_Un': 0.5238095238095238, 'Muck_It': 0.521383075523203, 'robw': 0.5204435204435205, 'RiverRatt': 0.5198423127463864, 'Benway': 0.5176646706586826, 'donguy': 0.5148247978436657, 'numskull': 0.5142198308993082, 'kk': 0.5126732004055424, 'rivrgod': 0.5125743026977595, 'Flash_man': 0.5123226288274833, 'KisMyAce': 0.5119255381035486, 'Sonar': 0.5099490976399815, 'Grizz': 0.5057162071284466, 'Quick': 0.5045351473922902, 'brian': 0.504424778761062, 'zxc': 0.502851711026616, 'num': 0.5026737967914439, 'Swagger': 0.49948682860075266, 'tilted': 0.49831365935919053, 'spew-boy': 0.49508196721311476, 'exosis': 0.490590248075278, 'Winner666': 0.4804161566707466, 'po147': 0.47808988764044946, 'theking': 0.4699546485260771}
    player_of_interest = list(player_of_interest_dict.keys())[:10]
    observation_betsize_list = []
    model_betsize_list = []
    for player in player_of_interest:
        file_path = f'/Users/tetsu/Documents/School/Class/CGSC274/aotm_project/analysis_and_modeling/data/betting_amounts{player}.json'
        with open(file_path, 'r') as file:
            data_list = [json.loads(line) for line in file]
            stages = ["f"] #, "t", "r"
            for stage in stages:
                for entry in data_list:
                    if entry["variable_type"] == "observation":
                        observation_betsize_list = observation_betsize_list + entry["data"][stage]
                        #print(observation_betsize_list + entry["data"][stage])
                    if entry["variable_type"] == "over_confidence":
                        model_betsize_list = model_betsize_list + entry["data"][stage]
                        
    observation_betsize_list = remove_nulls(observation_betsize_list)
    model_betsize_list = remove_nulls(model_betsize_list)
    #print(observation_betsize_list)
    pddata = pd.DataFrame({'Observation Betsizes': observation_betsize_list, 'Overconfidence Model Betsizes': model_betsize_list
    })
    # Choose the variables for the scatter plot
    x_variable = 'Observation Betsizes'
    y_variable = 'Overconfidence Model Betsizes'

    # Calculate the correlation coefficient
    correlation_coefficient = np.corrcoef(pddata[x_variable], pddata[y_variable])[0, 1]

    # Create a scatter plot
    plt.scatter(pddata[x_variable], pddata[y_variable], label=f'Correlation: {correlation_coefficient:.2f}')

    # Calculate the regression line parameters (slope and intercept)
    slope, intercept = np.polyfit(pddata[x_variable], pddata[y_variable], 1)

    # Plot the regression line
    x_range = np.linspace(min(pddata[x_variable]), max(pddata[x_variable]), 100)
    y_range = slope * x_range + intercept
    plt.plot(x_range, y_range, color='red', label='Regression Line')

    # Add labels and title
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)
    plt.title(f'Scatter Plot with Regression Line ({x_variable} vs {y_variable})')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()
    """
"""
    # Example data
    pddata = pd.DataFrame({'observation_betsize': observation_betsize_list, 'model_betsize': model_betsize_list
    })

    # Choose the variables for the scatter plot
    observation_betsize = 'Observation Betsizes'
    model_betsize = 'Optimal Model Betsizes'

    # Create a scatter plot
    plt.scatter(pddata['observation_betsize'], pddata['model_betsize'])

    # Add labels and title
    plt.xlabel(observation_betsize)
    plt.ylabel(model_betsize)
    plt.title(f'Scatter Plot of {observation_betsize} vs {model_betsize}')

    # Show the plot
    plt.show()
"""

if __name__ == "__main__":
    stages = ["f", "t", "r"]
    plot()
            
