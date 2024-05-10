import sys
from upload_and_preprocess_data import get_preprocessed_data

import draw_functions as fmddf

if __name__ == "__main__":
    print(get_preprocessed_data()[0])
    print('Enter country name: ')
    country = sys.stdin.readline().strip()

    fmddf.draw_3d_function_for_country(country)
