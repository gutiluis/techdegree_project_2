# calculation, callable function, or a block of logic, go in this file
# read from the constants. players and teams.
	# translate into a new collection of your choosing
from constants import PLAYERS
from constants import TEAMS
import random


def x():
	while True:
		try:
			print("BASKETBALL TEAM STATS TOOL \n")
			print("-------------MENU------------- \n")
			print("Here are your choices: ")
			print("1) Display Team Stats")
			print("2) Quit")
			choices_var = int(input("Enter an option > "))
			if choices_var == 1:
				print("1) Panthers")
				print("2) Bandits")
				print("3) Warriors\n")
			if choices_var == 2:
				break
				sys.exit()
			if choices_var == 0:
				break
			else:
				break
		except ValueError as err:
			print("Do not enter a letter. Enter a number in between 1 or 2 only.")
x()


def sec_option():
	while True:
		try:
			var_y = int(input("Enter an option > \n"))
			if var_y == 1:
				Panthers
				# team stats panthers
				# total players 18
				# total experienced 9
				# total inexperienced 9
				# add = average height # different every 6 numbers. 3 teams
			    # panthers deepcopy
			if var_y == 2:
				Bandits
				# team stats bandits
				# total players
				# total inexperienced
				# average height
		# bandits deepcopy
			variable
			if var_y == 3:
			    warr_cp
			# team stats
		except ValueError as err:
			print("Error: Enter an integer only")

sec_option()



def clean_panthers(PLAYERS):
	cleaned = []
	var_pant = copy.deepcopy(PLAYERS)
	for user in var_pant:
		fixed = {}
		fixed["guardians"] = user["guardians"]
		if user["experience"] == "YES":
			fixed["experience"] = True
		else:
			fixed["experience"] = False
		cleaned.append(fixed)
	return cleaned

clean_panthers(PLAYERS)
# [expression for temp_var in original_iterablea]


def clean_bandits(PLAYERS):
	cleaned = []
	var_ban = copy.deepcopy(PLAYERS)
	if user in var_ban:
		fixed = {}
		fixed["first_and_last"] = user["name"]
		fixed["guardians"] = user["guardians"]
		if user["experience"] == "YES":
			fixed["experience"] = True
		else:
			fixed["experience"] = False
		cleaned.append(fixed)
	return cleaned

clean_bandits(PLAYERS)
# [expression for temp_var in original_iterablea]


def clean_warriors(PLAYERS):
	cleaned = []
	warr_copy = copy.deepcopy(PLAYERS)
	for user in warr:
		fixed = {}
		fixed["first_and_last"] = user["name"]
		fixed["guardians"] = user["guardians"]
		if user["experience"] == "YES":
			fixed["experience"] = True
		else:
			fixed["experience"] = False
		cleaned.append(fixed)
	return cleaned

clean_warriors(PLAYERS)


def gather_players_and_teams():
	print("Bread, jelly, and peanut butter.")
	def experienced_(PLAYERS):
		cleaned = []
		var_copy = copy.deepcopy(PLAYERS)
		for user in var_copy:
			fixed ={}
			if user["experience"] == "YES":
				fixed["experience"] = True
			else:
				fixed["experience"] = False
			cleaned.append(fixed)
		return cleaned

	experienced_(PLAYERS)


# how to enter the 3 teams
	def inexper(PLAYERS):
		cleaned = []
		var_inex = copy.deepcopy(PLAYERS)
		for user in var_inex:
			fixed = {}
			if user["experience"] == "False":
				fixed["experience"] = False
			cleaned.append(fixed)
		return cleaned

	inexper(PLAYERS)

# for the stats
def average_height(PLAYERS):
	cleaned = []
	a = copy.deepcopy(PLAYERS)
	for user in a:
		fixed = {}
		fixed["how_tall"] = user["height"].split(" ")[0]
#		fixed["height"] = user["height"]
		cleaned.append(fixed)
	return cleaned


average_height(PLAYERS)



#Average height per team or per players???



def guardians_extract(PLAYERS):
	cleaned = []
	var = copy.deepcopy(PLAYERS)
	for user in var:
		fixed = {}
		fixed["guardians"] = user["guardians"]
		cleaned.append(fixed)
	return cleaned

guardians_extract(PLAYERS)

# balance same experienced and inexperienced 3 and 3
def combine_elements(TEAMS):
	player0 = [{"name": "Karl Saygan", "guardians": "Heather Bledsoe", "experience": "YES", "height": "42 inches"}]
	player1 = [{"name": "Matt Gill", "guardians" : "Charles Gill and Sylvia Gill", "experience": "NO", "hight": "40 inches"}]
	player2 = [{"name": "Sammy Adams", "guardians": "Jeff Adams and Gary Adams", "experience": "NO", "height": "45 inches"}]
	player3 = [{"name": "Chloe Alaska", "guardians": "David Alaska and Jamie Alaska", "experience": "NO", "height": "47 inches"}]
	player4 = [{"name": "Bill Bon", "guardians": "Sara Bon and Jenny Bon", "experience": "YES", "height": "43 inches"}]
	player5 = [{"name": "Joe Kavalier", "guardians": "Sam Kavalier and Elaine Kavalier", "experience": "NO", "height": "39 inches"}]
	player6 = [{"name": "Phillip Helm", "guardians": "Thomas Helm and Eva Jones", "experience": "YES", "height": "44 inches"}]
	player7 = [{"name": "Les Clay", "guardians": "Wyonna Brown", "experience": "YES", "height": "42 inches"}]
	player8 = [{"name": "Sal Dali", "guardians": "Gala Dali", "experience": "NO", "height": "41 inches"}]
	player9 = [{"name": "Suzane Greenberg", "guardians": "Henrietta Dumas", "experience": "YES", "height": "44 inches"}]
	player10 = [{"name": "Jill Tanner", "guardians": "Mark Tanner", "exxperience": "YES", "height": "36 inches"}]
	player11 = [{"name": "Arnold Willis", "guardians": "Clair Willis", "experience": "NO", "height": "43 inches"}]
	player12 = [{"name": "Herschel Krustofski", "guardians": "Hyman Krustofski and Ranchel Krustofski", "experience": "YES", "height": "45 inches"}]
	player13 = [{"name": "Eva Gordon", "guardians": "Wendy Martin", "experience": "NO", "height": "45 inches"}]
	player14 = [{"name": "Ben Finkelstein", "guardidans": "Aaron Lanning and Jill Fikelstein", "experience": "NO", "height": "44 inches"}]
	player15 = [{"name": "Joe Smith", "guardians": "Jim Smith and Jan Smith", "experience": "YES", "height": "42 inches"}]
	player16 = [{"name": "Diego Soto", "guardians": "Robin Soto and Sarika Soto", "experience": "YES", "height": "41 inches"}]
	player17 = [{"name": "Kimmy Stein", "guardians": "Bill Stein and Hillary Stein", "experience": "NO", "height": "41 inches"}]

	def unique_random(PLAYERS):
		rand_list = []
		for_copy_var = copy.deepcopy(PLAYERS)
		for user in for_copy_var:
			fixed = {}
			while True:
				var_random = int()
				var_random = random.sample(range(0, 18), 18)
				Panthers = var_random[:6]
				Bandits = var_random[6:12]
				Warriors = var_random[12:19]
				rand_list.append(fixed)
				print(Panthers)
				print(Bandits)
				print(Warriors)
				return

	unique_random(PLAYERS)





def main():
	x()
	function_a()
	clean_panthers(PLAYERS)
	clean_bandits(PLAYERS)
	clean_warriors(PLAYERS)
	gather_players_and_teams()
	combine_elements()


# in the bottom of the script always:
# for calculation,
	# callable function
		# block of logic
if __name__ == "__main__":
	main()

