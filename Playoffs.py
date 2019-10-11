# Import libraries
import random
import numpy as np
# import matplotlib.pyplot as plt
top2 = 0
power = 0
# List for each team and playoff probability
AA = ["AA",0.33,top2,power]
BG = ["BG",0.99,top2,power]
BSC = ["BSC",0.68,top2,power]
BT = ["BT",0.95,top2,power]
CHA = ["CHA",0.97,top2,power]
DDB = ["DDB",0.11,top2,power]
EJ = ["EJ",0.48,top2,power]
KCT = ["KCT",0.82,top2,power]
MTA = ["MTA",0.01,top2,power]
NSR = ["NSR",0.00,top2,power]
TDP = ["TDP",0.57,top2,power]
THR = ["THR",0.09,top2,power]

teams = [
    AA,
    BG,
    BSC,
    BT,
    CHA,
    DDB,
    EJ,
    KCT,
    MTA,
    NSR,
    TDP,
    THR
]

# Below function is just used for data validation
def test_data_entry():
    test_counter = 0
    test_data_totalplayoffs = 0
    while test_counter < 12 :
         test_data_totalplayoffs = test_data_totalplayoffs + teams[test_counter][1]
         test_counter += 1
    print("Total Playoffs",test_data_totalplayoffs)
# Run the line below to test validity of the data, should output 6
# test_data_entry()

# Select the playoff teams
# Normalized odds / 6 - returns very skewed results 
def playoff_choices():
    population = []
    odds = []
    select = []
    i = 0
    for team in teams:
        population.append(team[0])
    for team in teams:
        odds.append(team[1]/6)
    select = np.random.choice(population,6,replace=False,p=odds)
    # print(population)
    # print(odds)
    # print(select)
    return select

# Below function is just used for selection validation
def test_playoffs_check():
    test_playoff_teams = []
    test_playoff_test = 0
    while test_playoff_test < 10000:
        test_playoff_teams.extend(playoff_choices())
        test_playoff_test += 1
    return test_playoff_teams

# Test count each result so you can compare to the original probabilities
count_playoff_teams = test_playoffs_check()
for i in teams:
    print(i[0],count_playoff_teams.count(i[0]))

#playoff_teams = playoff_choices()
#print(playoff_teams)
