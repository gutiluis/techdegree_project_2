from constants import PLAYERS
import copy
import random
import sys


def combine_(PLAYERS):
    players_copy = copy.deepcopy(PLAYERS)
    random.shuffle(players_copy)
    define_team = len(players_copy) // 3  # 6 output team size
    panthers = players_copy[:define_team]
    bandits = players_copy[define_team:define_team * 2]
    warriors = players_copy[define_team * 2:]
    print("1) PANTHERS TEAM:")
    team_stats(panthers)
    print("\n2) BANDITS TEAM:")
    team_stats(bandits)
    print("\n3) WARRIORS:")
    team_stats(warriors)
    return {"panthers": panthers, "bandits": bandits, "warriors": warriors}
    # loop syntax first. for comprehension


def team_stats(team):
    total_players = len(team)
    # player is termporary_variable in iterable
    experienced = len([player for player in team if "experience" in player and player["experience"].upper() == "YES"])
    inexperienced = total_players - experienced
    print(f"Total players: {total_players}")
    print(f"Inexperienced players: {experienced}")
    print(f"Inexperienced players: {inexperienced}\n")
    print("Selected players\n")
    list_var_heights = []
    list_var_names = []
    for player in team:
        fixed = {}
        fixed["name"] = player["name"]
        fixed["tall"] = player["height"].split(" ")[0]
        list_var_heights.append(int(fixed["tall"]))
        list_var_names.append(fixed["name"])
    convert_to_string = ", ".join(list_var_names)
    print(convert_to_string)
    if list_var_heights:
        av = sum(list_var_heights) / len(list_var_heights)
        print(f"Team average: int({av}) inches")



def greeting():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---------------MENU------------\n")
    print(
        "Here are your choices:\n",
        "1) Display Team Stats\n",
        "2) Quit \n"
    )
    try:
        variable = int(input("Enter an option > "))
    except ValueError:
        print("Invalid input")
        sys.exit()

    if variable == 1:
        combine_(PLAYERS)
    elif variable == 2:
        sys.exit()
    else:
        sys.exit()


def main():
    greeting()


if __name__ == "__main__":
    main()
