import pandas as pd 
import numpy as np
spain_clean_df = pd.read_csv("results/spain_clean.csv")

barca_home_records = spain_clean_df[spain_clean_df['home' == 'FC Barcelona']]

print(barca_home_records.head())

