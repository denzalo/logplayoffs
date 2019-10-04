#Import libraries
import random
#import matplotlib.pyplot as plt

#List is (team abbreviation, playoff odds, bye odds,.....)
AA = ["AA",.33,.01]
BG = ["BG",.99,.82]
BSC = ["BSC",.68,.07]
BT = ["BT",.95,.34]
CHA = ["CHA",.97,.52]
DDB = ["DDB",.11,.00]
EJ = ["EJ",.48,.03]
KCT = ["KCT",.82,.17]
MTA = ["MTA",.00,.00]
NSR = ["NSR",.01,.00]
TDP = ["TDP",.57,.05]
THR = ["THR",.09,.00]
teams = [AA,BG,BSC,BT,CHA,DDB,EJ,KCT,MTA,NSR,TDP,THR]

#This is a function I wrote to confirm my data entry above
#Should output numbers close to 6 and 2. I'm OK with a little variance
def probability_check():
    test_total_playoffs = 0
    test_total_byes = 0
    test_counter = 0
    while test_counter < 12:
         test_total_playoffs = test_total_playoffs + teams[test_counter][1]
         test_total_byes = test_total_byes + teams[test_counter][2]
         test_counter = test_counter + 1
    print("Total Playoffs",test_total_playoffs)
    print("Total Byes",test_total_byes)
# Run the line below to run the above test function
# probability_check()

# Algorithm to pick the 6 playoff teams
# Dice roll turned into a percentage and compared against each team's probability
# Throw out any results that don't have exactly 6 teams
def playoffs():
    while True:
        playoff_list = []
        for i in teams:
            diceroll = random.randint(1,100) / 100
            if i[1] >= diceroll:
                playoff_list.append(i[0])
            else:
                continue
        if len(playoff_list) == 6:
            break
        else:
            continue
    return playoff_list

# Function to run the playoff selection algorithm 10,000 times
# Add every 6-team scenario to one giant list with 60,000 items
def playoffs_check():
    playoff_teams = []
    playoff_test = 0
    while playoff_test < 1000:
        playoff_teams.extend(playoffs())
        playoff_test = playoff_test + 1
    return playoff_teams

# Run the algorithm test function
# Count each result so you can compare to the original probabilities
playoffs_list = playoffs_check()
for x in teams:
    print(x[0],playoffs_list.count(x[0]))
