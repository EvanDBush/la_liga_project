import pandas as pd
spain_clean_df = pd.read_csv("results/spain_clean.csv")

# get total wins, ties, losses
# get total goals scored/ conceded

# get records above selected by season
# add season standings: places goal differential
# 
# get two teams head-to-head records.
# total wins ties losses
# last 20 years
# last 5 matches 

def main():

    team_list = spain_clean_df['home'].unique()
    print(team_list)

    while (True):
        team_input = input("What team would you like stats on? (Q to Quit)")
        
        if team_input.upper() == 'Q':
            break
        if team_input in team_list:
            target_team = team_input
            
            
            team_home_df = spain_clean_df[spain_clean_df['home'] == target_team]
            team_away_df = spain_clean_df[spain_clean_df['visitor'] == target_team]
            team_totals = [team_home_df, team_away_df]
            team_totals_df = pd.concat(team_totals)
            print(team_totals_df)
            
            continue
        else:
            print('Input: ' + team_input + ' does not match team from list. Please try again.')   

main()
 
