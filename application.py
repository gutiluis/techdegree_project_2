#name:
#list of teams
#list of players
# total number of players
# equal number. 2 teams
# dunder main, html, javascript, clean_data, debbuger, (set-dictionary-list_comprehensions)
# flake8, debugger, pep8, pep20, clean
# python3 applications will not run the content of the dm.py file
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
# loop
# copy.deepcopy()
# save the cleaned data to a new collection
# split is for string
# sliciing or iteration for a list with nested dictionary

print("\n")
print("BASKETBALL TEAM STATS TOOL\n")

print("---- MENU ----\n")


def first_paragraph():
	print("Here are your choices:")
	print("  1) Display Team stats")
	print("  2) Quit\n")
	while True:
		try:
			var_x = int(input("Enter an option >\n "))
			if var_x == 1:
				panthers
				print("1) Panthers")
			if var_x == 2:
				bandits
				print("2) Bandits")
			if var_x == 3:
				warriors
				print("3) Warriors")
				break
			if var_x == 0:
				break
			else:
				continue
			print("\n")
			while True:
				try:
					var_y = int(input("Enter an option >\n ")
					if var_y == 1:
						print("Team: Panthers Stats")
						print("_____________________")
						print("Total players: ")
						print("Total experienced: ")
						print("Total inexperienced:  ")
						print("Average height: ")
					if var_y == 2:
						print("Team: Bandits Stats")
						print("---------------------")
						print("Total players: ")
						print("Total experienced: ")
						print("Total inexperienced: ")
						print("Average height: ")
					if var_y == 3:
						print("Team: Warriors Stats")
						print("--------------------")
						print("Total players: ")
						print("Total experienced: ")
						print("Total inexperienced: ")
						print("Average height: ")
						print("")
					if var_y == 0:
						break
				except ValueError as err: # show type of error?
					print("Enter a valid input")
		except ValueError as err:
			print("Enter a valid input")

first_paragraph()




def clean_data(PLAYERS):
	var = input("A) Display Team stats")
	if var == "A":
	quit_var = input("B) Quit")
	if quit_var == "B":
		break
	cleaned = []
	copy.deepcopy(cleaned)
# clan also guardian. before adding it to the newly created collection. split up the guradian string into a list
	for user in PLAYERS:
		fixed = {} # dictionary per user
		fixed["feet_tall"] = user["height"].split(" ")[0] # use to filter per height
		fixed["var"] = user["guardians"].split("")[]
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

print("Enter an option")
print("\n")

print("Enter an option")
if 1, 2, or 3:
print("\n")

Panther stats = 

print(f "Team: {Panther stats}")
print("-------------------------")
print("Total players:")
print("Total experienced: ")
print("Total inexperienced: ")
print("Average height: ")



print("Players on Team:")


# guardianss use and keyword for 2 values. to indicate more than one guardian
print("Guardians:")



keep_var = input("Press ENTER to continue...")
if keep_var == "ENTER":

