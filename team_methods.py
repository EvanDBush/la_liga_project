import pandas as pd
spain_clean_df = pd.read_csv("results/spain_clean.csv")

team_input = 'FC Barcelona'
season_input = 2020
season_records = spain_clean_df[spain_clean_df['Season'] == int(season_input)]
team_records = spain_clean_df[spain_clean_df['home'] == int(team_input)]

#get season records
def getSeasonRecords(team):
    team_home_record = season_records[season_records['home'] == team]
    team_visitor_record = season_records[season_records['visitor'] == team]
    team_season_records_df = [team_home_record, team_visitor_record]
    team_season_records_df = pd.concat(team_season_records_df).sort_values( by= 'Date')
    return team_season_records_df

# get total wins
def getTotalWins(user_input):
    team_home_df = spain_clean_df[spain_clean_df['home'] == user_input]
    team_away_df = spain_clean_df[spain_clean_df['visitor'] == user_input]
    team_totals = [team_home_df, team_away_df]
    team_totals_df = pd.concat(team_totals)
    return team_totals

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