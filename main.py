import sys

import fill_missing_data_and_draw_function as fmddf

if __name__ == "__main__":
    print('Enter country name: ')
    country = sys.stdin.readline().strip()

    fmddf.draw_3d_function_for_country(country)
