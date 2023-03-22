import pandas as pd
spain_clean_df = pd.read_csv("results/spain_clean.csv")

def main():

    season_list = spain_clean_df['Season'].unique()
    print(season_list.dtype)
    print(f'Seasons available: {season_list.min()} to {season_list.max()}')

    while (True):
        season_input = input("What Season would you like stats on? (Q to Quit)")
        
        if season_input.upper() == 'Q':
            break
        if int(season_input) in season_list :
            season_records = spain_clean_df[spain_clean_df['Season'] == int(season_input)]
            print(season_records)
            
            
            
            continue
        else:
            print(f'Input: {season_input} dtype: {season_input.dtype} does not match season in list. Please try again.')   

main()