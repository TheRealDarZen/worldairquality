import sys

from process_data import get_processed_data
from upload_and_preprocess_data import get_preprocessed_data


import draw_functions as fmddf

if __name__ == "__main__":
    data_df = get_processed_data()[1]
    print(data_df)
    print('Enter country name: ')
    country = sys.stdin.readline().strip()

    fmddf.draw_population_pollution_year_function(country, data_df)
