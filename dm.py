# read from the constants. players and teams. 
	# translate into a new collection of your choosing 
from constants import PLAYERS
from constants import TEAMS

# 3 teams
# 18 players
def gather_players_and_teams():
	var_players = []
	var_players = PLAYERS
	var_players
	var_teams = []
	var_teams = TEAMS
	var_teams


def combine_elements():
	oper = var_players / var_teams # players divided by 3 teams = 6 players per team
	var_players = 18
	team1_ = oper.a
	team2_ = oper.b
	team3_ = oper.c
	print(oper)

# in the bottom of the script
if __name__ == "__main__":
	gather_players_and_teams()
	combine_elements()
