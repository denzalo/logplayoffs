# Import libraries
import random
import numpy as np
# import matplotlib.pyplot as plt
top2 = 0
power = 0
# List for each team and playoff probability
#BG = ["BG",0.3293,top2,9900]
#CHA = ["CHA",0.2227,top2,9700]
#BT = ["BT",0.1800,top2,9500]
#KCT = ["KCT",0.0917,top2,8200]
#BSC = ["BSC",0.0601,top2,6800]
#TDP = ["TDP",0.0450,top2,5700]
#EJ = ["EJ",0.0355,top2,4800]
#AA = ["AA",0.0226,top2,3300]
#DDB = ["DDB",0.0069,top2,1100]
#THR = ["THR",0.0056,top2,900]
#MTA = ["MTA",0.0006,top2,100]
#NSR = ["NSR",0.0000,top2,0]

# List from cross validated
BG = ["BG",0.2863,top2,9900]
CHA = ["CHA",0.2181,top2,9700]
BT = ["BT",0.1863,top2,9500]
KCT = ["KCT",0.1066,top2,8200]
BSC = ["BSC",0.0709,top2,6800]
TDP = ["TDP",0.0525,top2,5700]
EJ = ["EJ",0.0407,top2,4800]
AA = ["AA",0.0249,top2,3300]
DDB = ["DDB",0.0072,top2,1100]
THR = ["THR",0.0059,top2,900]
MTA = ["MTA",0.0006,top2,100]
NSR = ["NSR",0.0000,top2,0]

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
        odds.append(team[1])
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
    print(i[0],count_playoff_teams.count(i[0]),"expected:",i[3]*100-150,"-",i[3]*100+150)

#playoff_teams = playoff_choices()
#print(playoff_teams)
