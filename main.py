import pandas as pd
from functions import *
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

for team in ten_wins:
    print(team)