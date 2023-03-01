import argparse
import json
import logging
from pathlib import Path
import pandas as pd
import numpy as np


# Clean data for La Liga Data
#
# Usage: 
# $ python spain_clean.py data/spain.csv results/spain_clean.csv
#
# where:
#   data/spain.csv              = path to the input file
#   results/spain_clean.csv     = path to the output file
#
# test input file provided: data/spain.csv

def get_file_names() -> tuple:
    """Get the input and output file names from the arguments passed in
    @return a tuple containing (input_file_name, output_file_name)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Name of the original data file.")
    parser.add_argument("output_file", help="Name of the file for cleaned data.")
    args = parser.parse_args()
    return args.input_file, args.output_file


def validate_columns(df: pd.DataFrame) -> None:
    """Validates that the data in the input file has the expected columns. \
    Exits with an error if the expected columns are not present.
    @param df - The DataFrame object with the data from the input file.
    """
    EXPECTED_COLUMNS = ['Date', 'Season', 'home', 'visitor', 'HT', 'FT', 'hgoal', 'vgoal',
       'tier', 'round', 'group', 'notes']
    if not all(item in list(df.columns) for item in EXPECTED_COLUMNS):
       logging.error('Input file does not have the expected columns.')
       exit(1)
    return None


# def build_genre_column(df: pd.DataFrame) -> pd.DataFrame:
#     """Creates a new column in the DataFrame called Genre that is based on the\
#     ItemCollection column.
#     @param df - the original DataFrame
#     @return a DataFrame with a new column added
#     """
#     json_path = Path('data/genre.json')
#     with open(json_path, 'r') as json_file:
#         genre_data = json.load(json_file)
#         genre_conditions = [
#             (df['ItemCollection'].isin(genre_data['Fiction'])),
#             (df['ItemCollection'].isin(genre_data['Non-Fiction'])),
#             (df['ItemCollection'].isin(genre_data['Unknown']))
#         ]
#         genre_values = ['Fiction', 'Non-Fiction', 'Unknown']
#         df['Genre'] = np.select(genre_conditions, genre_values)
#         return df


# TODO: define a function to create the audience column here
def build_audience_column():
    pass


def main() -> None:
    """Main cleaning logic
    """
    logging.info('Getting file names from arguments.')
    input_file, output_file = get_file_names()
    logging.info(f'Input file is: {input_file}')
    logging.info(f'Output file is: {output_file}')
 
    logging.info('Loading data from input file.')
    input_path = Path(input_file)
    if not input_path.exists():
        logging.error(f'Input file not found: {input_file}')
        exit(1)
    spain_df = pd.read_csv(input_path)

    logging.info('Validating columns in input file.')
    validate_columns(spain_df)


    # 1. TODO: Remove games with phase2 in round column.
    # logging.info('Step 1: Removing games with phase2 in "round" column.')
    # spain_df = spain_df[spain_df['round'] != 'phase2']

    # 2. TODO: Remove unneeded columns (tier, round, notes, ht)
    # logging.info('Step 2: Removing unneeded columns.')
    # spain_df.drop(['tier', 'round', 'group', 'notes', 'HT'], axis=1, inplace=True)


    # 3. TODO: Update column names
    # logging.info('Step 3: Improving column readability.')
    # spain_df.rename(columns={
    #         'FT': 'score',
    #         'hgoal': 'hgoal',
    #         'vgoal': 'vgoal'
    #     }, inplace=True)


    # 4. TODO: Add hpoints and vpoints columns
    
 
    logging.info('Saving output file.')
    output_path = Path(output_file)
    if output_path.suffix == '.csv.gz':
        spain_df.to_csv(output_path, index=False, compression="gzip")
    else:
        spain_df.to_csv(output_path, index=False)
    
    return None


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
    main()