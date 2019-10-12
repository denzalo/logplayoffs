# Import libraries
import random
import numpy as np
# import matplotlib.pyplot as plt
top2 = 0
power = 0
# List for each team and playoff probability
AA = ["AA",0.1363,top2,3300]
BG = ["BG",1.9602,top2,9900]
BSC = ["BSC",0.3608,top2,6800]
BT = ["BT",1.0845,top2,9500]
CHA = ["CHA",1.3414,top2,9700]
DDB = ["DDB",0.0420,top2,1100]
EJ = ["EJ",0.2139,top2,4800]
KCT = ["KCT",0.5529,top2,8200]
MTA = ["MTA",0.0037,top2,100]
NSR = ["NSR",0.0000,top2,0]
TDP = ["TDP",0.2700,top2,5700]
THR = ["THR",0.0343,top2,900]

teams = [
    BG,
    CHA,
    BT,
    KCT,
    BSC,
    TDP,
    EJ,
    AA,
    DDB,
    THR,
    MTA,
    NSR
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
    while test_playoff_test < 1000000:
        test_playoff_teams.extend(playoff_choices())
        test_playoff_test += 1
    return test_playoff_teams

# Test count each result so you can compare to the original probabilities
count_playoff_teams = test_playoffs_check()
for i in teams:
    print(i[0],count_playoff_teams.count(i[0]),"expected:",i[3]*100)

#playoff_teams = playoff_choices()
#print(playoff_teams)
