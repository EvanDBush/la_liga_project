import pandas as pd
spain_clean_df = pd.read_csv("results/spain_clean.csv")
user_input = 'FC Barcelona'

# get total wins
def getTotalWins(user_input):
    team_records = spain_clean_df[user_input]

# get total ties
# get total losses
# get total goals scored 
# get total goals conceded

# get largest win-streak
# get largest losing streak
# get best season (top 3) 

# get records above selected by season
# add season standings: places goal differential


# get two teams head-to-head records.
# total wins ties losses
# last 20 years
# last 5 matches 