import pandas as pd 
import numpy as np
spain_clean_df = pd.read_csv("results/spain_clean.csv")

# 3 points for a win, 1 point for a Tie, 0 points for a loss

if spain_clean_df['hgoal'] > spain_clean_df['vgoal']:
    spain_clean_df.assign(hpoint= 3, vpoint= 0)

elif spain_clean_df['hgoal'] < spain_clean_df['vgoal']:
    spain_clean_df.assign(hpoint= 0, vpoint= 3)

else:
    spain_clean_df.assign(hpoint= 1, vpoint= 1)

