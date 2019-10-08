# Import libraries
import random
# import matplotlib.pyplot as plt

# Dictionary for each team and playoff probability
teams = {
    "AA": 0.33,
    "BG": 0.99,
    "BSC": 0.68,
    "BT": 0.95,
    "CHA": 0.97,
    "DDB": 0.11,
    "EJ": 0.48,
    "KCT": 0.82,
    "MTA": 0.01,
    "NSR": 0.01,
    "TDP": 0.57,
    "THR": 0.09,
}

# Below function is just used for testing
def test_data_entry():
    test_data_totalplayoffs = 0
    for i in teams:
         test_data_totalplayoffs = test_data_totalplayoffs + teams[i]
    print("Total Playoffs",test_data_totalplayoffs)
# Run the line below to test validity of the data, should output 6
# test_data_entry()

# Select the playoff teams
def playoff_choices():
    keys = list(teams.keys())
    values = list(teams.values())
    select = random.choices(keys,weights=values, k = 6)
    return select

# Below function is just used for testing
def test_playoffs_check():
    playoff_teams = []
    playoff_test = 0
    while playoff_test < 10000:
        playoff_teams.extend(playoff_choices())
        playoff_test += 1

    return playoff_teams

# Test count each result so you can compare to the original probabilities
playoff_teams = test_playoffs_check()
for x in teams:
    print(x,playoff_teams.count(x))
