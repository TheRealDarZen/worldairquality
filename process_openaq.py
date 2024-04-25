import pandas as pd

def avg_by_country(data):
    country_map = {}
    # Unit : µg / m³

    last_country_label = "Belgium"
    curr_value = 0
    curr_num = 0
    for line in data:
        unit = data['Unit']
        if last_country_label == line['Country Label']:
            if unit == 'ppm':
                curr_value += max(line['Value'] * (55 / 24.55 * 1000), 0)
            else:
                curr_value += max(line['Value'], 0)
            curr_num += 1
        else:
            mean = curr_value/curr_num
            country_map[last_country_label] = mean
            curr_value = line['Value']
            curr_num = 1

    mean = curr_value / curr_num
    country_map[last_country_label] = mean

    return country_map
