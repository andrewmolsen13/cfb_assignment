import pandas as pd

def team_counter(teams):
    team_list = []
    for team in teams:
        team_list.append(team)
    return team_list

football_stats = pd.read_csv("cfb.csv")
menu_run = True
seasons = [2013,2014,2015,2016,2017,2018,2019,2020]

while menu_run:
    try:
        menu = int(input("What season would you like to analyze? Pick any season from 2013-2020 "))
        while menu not in seasons:
            menu = int(input("Please input a year from 2013-2020 "))
        menu_run = False
    except ValueError:
        print("Please enter a valid number")

year = football_stats.loc[football_stats["Season"] == menu]
ten_wins = team_counter(year.query("Win >= 10")["Team"])
eight_nine_wins = team_counter(year.query("Win >= 8 and Win < 10")["Team"])
six_seven_wins = team_counter(year.query("Win >= 6 and Win < 8")["Team"])
five_and_less = team_counter(year.query("Win < 6")["Team"])

print("\nTeams with 10+ wins:\n")
for team in ten_wins:
    print(team)
print("\nTeams with 8-9 wins:\n")
for team in eight_nine_wins:
    print(team)
print("\nTeams with 6-7 wins:\n")
for team in six_seven_wins:
    print(team)
print("\nTeams with 5 and less wins:\n")
for team in five_and_less:
    print(team)

