import random

#List is (team abbreviation, playoff odds)
AA = ["AA",.33]
BG = ["BG",.99]
BSC = ["BSC",.68]
BT = ["BT",.95]
CHA = ["CHA",.97]
DDB = ["DDB",.11]
EJ = ["EJ",.48]
KCT = ["KCT",.82]
MTA = ["MTA",.00]
NSR = ["NSR",.01]
TDP = ["TDP",.57]
THR = ["THR",.09]
teams = [AA,BG,BSC,BT,CHA,DDB,EJ,KCT,MTA,NSR,TDP,THR]

# Algorithm to pick the 6 playoff teams
# Dice roll turned into a percentage and compared against each team's probability
# Throw out any results that don't have exactly 6 teams

def playoffs():
    while True:
        playoff_list = []
        for i in teams:
            diceroll = random.randint(1,100) / 100
            if diceroll <= i[1]:
                playoff_list.append(i[0])
            else:
                continue
        if len(playoff_list) == 6:
            break
        else:
            continue
    return playoff_list

# Function to run the above selection algorithm 10,000 times
# Add every 6-team scenario to one giant list with 60,000 items

def playoffs_check():
    playoff_teams = []
    playoff_test = 0
    while playoff_test < 10000:
        playoff_teams.extend(playoffs())
        playoff_test += 1
    return playoff_teams

# Run the algorithm
# Count the results so you can compare to the original probabilities

playoffs_list = playoffs_check()
for x in teams:
    print(x[0],playoffs_list.count(x[0]))
