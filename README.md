# aotm_project

## Intro
This is the code repository for the project "Generative Model for Simulating Betting Behavior in Poker" which introduces a generative model which aims to serve as a base model upon which human behavior of decision making of bet size in poker can be simulated. We hypothesize that human behavior can be modeled as a certain deviation from a mathematically optimal model, and have tested this by constructing a base model, which is mathematically optimal. The preliminary results have shown that the model correlates with empirical human data acquired from online poker games and the model with latent variables added also performs well when compared to the empirical data, especially when sorting the dataset by proficiency in poker skills (the more proficient the player is, the more the optimal model predicts the empirical decision).
Furthermore, the results have shown that incorporating prospect theory as a utility function improves the generative model's performance in simulating human decision making, and suggests that people's decision making is divided into two stages: whether to bet, and how much to bet.

## Files
- `gen_model.py` is the python file with the generative model
- `correlation.py` is the python file to compute the correlation between the simulated decisions and ground truth decisions
- `data` folder contains the post processed data, which the raw data is obtained from [ICR Poker Database](https://poker.cs.ualberta.ca/irc_poker_database.html), and all the simulated results
- `data_processing` folder contains the script for preprocessing the dataset, as well as the win probability calculator file (`win_prob_calculator.py`)
