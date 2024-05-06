import sys

import fill_missing_data_and_draw_function as fmddf

if __name__ == "__main__":
    while True:
        print('Enter <country code> <start year> <end year> (1990-2017): ')
        line = sys.stdin.readline()
        parts = line.strip().split()
        country_code = parts[0]
        start_year = int(parts[1])
        end_year = int(parts[2])
        if len(country_code) != 3 or not (1990 <= start_year <= end_year <= 2017):
            print('Incorrect data.')
        else:
            break

    fmddf.draw_3d_function(country_code, start_year, end_year)
