import sys

import draw_functions as fmddf

if __name__ == "__main__":
    print('Enter country name: ')
    country = sys.stdin.readline().strip()

    fmddf.draw_3d_function_for_country(country)
