#name:
#guardians
#experience
#height
#list of teams
#list of players
# cleaning up player data
# total number of players
# equal number. 2 teams
# dunder main, html, javascript, 
# flake8, debugger, pep8, pep20, clean
# python3 applications will not run the content of the dm.py file
# nested lists and dictionaries
import dm
import copy
from constants import PLAYERS



# no hard-coding
#print(__name__, " = app.py's value")

# the expression of the comprehension returns a value
# [expression for temp_iterable in original_iterable]
# a loop is not the only way to iterate
# use comprehensions instead of iterable loops
# comprehension with and without conditions
# lists with nested dictionaries
# clean data
# clean and loop
# read the existing player data from the PLAYERS constants 
# copy.deepcopy()
# save the cleaned data to a new collection
# lists with nested dictionaries
# clean height, experience
# split is for string
# sliciing or iteration for a list with nested dictionary


				# use copy.deepcopy()
				# save the cleaned data to a new collenction

print("\n")
print("BASKETBALL TEAM STATS TOOL\n")

print("---- MENU ----\n")


def first():
	var = input("A) Display Team stats")
	if var == "A":
		clean_data



def clean_data(PLAYERS):
#new list named cleaned
	var = input("A) Display Team stats")
	if var == "A":
	quit_var = input("B) Quit")
	if quit_var == "B":
		break
	cleaned = []
	copy.deepcopy(cleaned)
#	int(height)	
#	bool(experience)
	for user in PLAYERS:
		fixed = {} # dictionary per user
		fixed["feet_tall"] = user["height"].split(" ")[0] # use to filter per height
#		fixed["experience"] = user["experience"]
#		print(user["height"]) # use to filter per height
		if user["experience"] == True:
			fixed["experience"] = True
		else:
			fixed["experience"] = False
		cleaned.append(fixed) # append the whole previous dictionary
	return cleaned

print(clean_data(PLAYERS))



# 3 teams same number of players
# divide length of players by the number of teams
# num_players_team = len(PLAYERS) / len(TEAMS)
def balance_(cleaned_data):
	TEAMS = "Panthers", "Bandits", "Warriors"
	num_players_teams = len(PLAYERS) / len(TEAMS)
#	balance_teams

#balance_()


# display selected teams stats
# include teams name as a string
# total players on that team as an integer
# player names as strings separated by commas
# do not display the list representation object






