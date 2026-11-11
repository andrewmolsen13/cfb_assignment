import pandas as pd
#creates a list to store the different teams in the specified win total
def team_counter(teams):
    team_list = []
    for team in teams:
        team_list.append(team)
    return team_list
teams = {}

#puts the csv file in a readable way for pandas
football_stats = pd.read_csv("cfb.csv")

#Validation loop for the menu to make sure we get a valid year
menu_run = True
seasons = football_stats["Season"].unique().tolist()
while menu_run:
    try:
        menu = int(input(f"What season would you like to analyze? Availible seasons: {", ".join(str(season) for season in seasons)} "))
        while menu not in seasons:
            menu = int(input("Season not found, please input another "))
        menu_run = False
    except ValueError:
        print("Please enter a valid number")

#Finds the instances of the year in the file
year = football_stats.loc[football_stats["Season"] == menu]
#pull the different win totals for each team in the selected season and sends it to the team counter func
teams["ten_wins"] = team_counter(year.query("Win >= 10")["Team"])
teams["eight_nine_wins"] = team_counter(year.query("Win >= 8 and Win < 10")["Team"])
teams["six_seven_wins"] = team_counter(year.query("Win >= 6 and Win < 8")["Team"])
teams["five_and_less_wins"] = team_counter(year.query("Win < 6")["Team"])

print("\nTeams with 10+ wins:")
for team in teams["ten_wins"]:
    print(team)
print("\nTeams with 8-9 wins:")
for team in teams["eight_nine_wins"]:
    print(team)
print("\nTeams with 6-7 wins:")
for team in teams["six_seven_wins"]:
    print(team)
print("\nTeams with less than 6 wins:")
for team in teams["five_and_less_wins"]:
    print(team)
