import pandas as pd
spain_clean_df = pd.read_csv("results/spain_clean.csv")

def main():

    season_list = spain_clean_df['Season'].unique()
    print(f'Seasons available: {season_list.min()} to {season_list.max()}')

    while (True):
        season_input = input("What Season would you like stats on? (Q to Quit)")
        
        if season_input.upper() == 'Q':
            break
        if int(season_input) in season_list :
            season_records = spain_clean_df[spain_clean_df['Season'] == int(season_input)]

            empty_season_stats = {'Team': [], 'Points': [], 'GS': [], 'GA': [], 'GD': [], 'Wins': [], 'Losses': [], 'Ties': []}   
            season_stats_df = pd.DataFrame(data= empty_season_stats)
            
            team_list = season_records['home'].unique()
            empty_list = []
            for team in team_list:

                # gets team records
                team_home_record = season_records[season_records['home'] == team]
                team_visitor_record = season_records[season_records['visitor'] == team]
                team_season_records_df = [team_home_record, team_visitor_record]
                team_season_records_df = pd.concat(team_season_records_df).sort_values( by= 'Date')
                
                #gets team points
                team_home_points = team_home_record['hpoint'].sum()
                team_visitor_points = team_visitor_record['vpoint'].sum()
                team_season_points = team_home_points + team_visitor_points
                
                #adds team goals
                team_home_goals = team_home_record['hgoal'].sum()
                team_visitor_goals = team_visitor_record['vgoal'].sum()
                team_total_goals = team_home_goals + team_visitor_goals
                
                #gets goal totals
                team_home_goals_allowed = team_home_record['vgoal'].sum()
                team_visitor_goals_allowed = team_visitor_record['hgoal'].sum()
                team_total_goals_allowed = team_home_goals_allowed + team_visitor_goals_allowed
                team_goal_differential = team_total_goals - team_total_goals_allowed

                #gets team home WLT records
                team_home_wins = team_home_record[team_home_record['hgoal'] > team_home_record['vgoal']].shape[0]
                team_home_losses = team_home_record[team_home_record['hgoal'] < team_home_record['vgoal']].shape[0]
                team_home_ties = team_home_record[team_home_record['hgoal'] == team_home_record['vgoal']].shape[0]

                #gets team away WLT records
                team_away_wins = team_visitor_record[team_visitor_record['hgoal'] < team_visitor_record['vgoal']].shape[0]
                team_away_losses = team_visitor_record[team_visitor_record['hgoal'] > team_visitor_record['vgoal']].shape[0]
                team_away_ties = team_visitor_record[team_visitor_record['hgoal'] == team_visitor_record['vgoal']].shape[0]

                #gets team WLT totals
                team_total_wins = team_home_wins + team_away_wins
                team_total_losses = team_home_losses + team_away_losses
                team_total_ties = team_home_ties + team_away_ties

                team_stats = {'Team': team, 'Points': team_season_points, 
                              'GS': team_total_goals, 'GA': team_total_goals_allowed, 
                              'GD': team_goal_differential, 'Wins': team_total_wins, 
                              'Losses': team_total_losses, 'Ties': team_total_ties}
                empty_list.append(team_stats)
                
             
            
            # print(season_stats_df)
            # print(empty_list)
            season_stats_df = pd.DataFrame(empty_list)
            season_stats_df = season_stats_df.sort_values(by= 'Points', ascending= False).reset_index(drop=True)
            print(season_stats_df)    
                
            
        else:
            print(f'Input: {season_input} dtype: {season_input.dtype} does not match season in list. Please try again.')   

main()