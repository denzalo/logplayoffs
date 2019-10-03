I'm trying to develop an algorithm that predicts who will be the league champion in my fantasy football league.
I assign each team an "odds to make playoffs" and then a power ranking from 50 to 100
We will then run a monte carlo simulation 10,000 times to see how many times each team wins the league

The "odds to make playoffs" number is pre-determined from another source. As is the team's power ranking.

My first step I'm trying to accomplish is to come up with a method to pick the 6 playoff teams (out of 12 in the league).
The algorithm I have in place at the moment is close, but not quite right as it's producing results about 3-5% off of the actual probabilities, fairly consistently.
