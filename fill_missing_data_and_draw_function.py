import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from upload_and_preprocess_data import get_preprocessed_data


def fill_missing_population(country: str):
    # Read the world population data from the CSV file
    _, population_df, _ = get_preprocessed_data()

    # Filter data for the specified country
    country_data = population_df[population_df['CCA3'] == country]

    # Specify the years to extract population data for
    years_av = [1990, 2000, 2010, 2015, 2020]

    # Extract population numbers for the specified years
    population = []
    for year in years_av:
        population_column = f'{year} Population'
        population.append(country_data[population_column].values[0])

    # Fill in missing years using arithmetic progression
    filled_population = [] # year = index + 1990
    for index, year in enumerate(years_av):
        if index == len(years_av) - 1:
            filled_population.append(population[index])
            break

        filled_population.append(population[index])
        next_year = years_av[index + 1]
        steps = next_year - year - 1
        if steps > 0:
            value_dif = population[index + 1] - population[index]
            add_on_step = int(value_dif / steps)

            for _ in range(steps):
                filled_population.append(filled_population[-1] + add_on_step)

    return filled_population

def fill_missing_pm25(country: str):
    _, _, pm25_df = get_preprocessed_data()

    country_data = pm25_df[pm25_df['Code'] == country]

    years_av = [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

    pollution = []

    for year in years_av:
        pollution.append(country_data['PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)'].values[country_data['Year'] == year][0])

    filled_pollution = [] # year = index + 1990
    for index, year in enumerate(years_av):
        if index == len(years_av) - 1:
            filled_pollution.append(pollution[index])
            break

        filled_pollution.append(pollution[index])
        next_year = years_av[index + 1]
        steps = next_year - year - 1
        if steps > 0:
            value_dif = pollution[index + 1] - pollution[index]
            add_on_step = int(value_dif / steps)

            for _ in range(steps):
                filled_pollution.append(filled_pollution[-1] + add_on_step)

    return filled_pollution


def draw_3d_function(country: str, start_year: int, end_year: int):
    # Get preprocessed data
    co2_df, population_df, pm25_df = get_preprocessed_data()

    # Merge data
    merged_df = pd.merge(co2_df, population_df, left_on='country_code', right_on='CCA3', how='inner')

    # Plotting
    country_to_plot = country

    # Filtering data
    country_data = merged_df[merged_df['country_code'] == country_to_plot]

    # Creating a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plotting the data for the country
    population_raw = fill_missing_population(country)
    population = []
    pollution = []
    years = []

    # Fill arrays with data
    for i in range(end_year - start_year + 1):
        year = i + start_year
        population.append(population_raw[i])
        pollution.append(country_data[f'{year}'].values[0])  # Append CO2 emissions value
        years.append(year)

    # Connect data points
    ax.plot(population, pollution, years, label=f'{country_data['Country/Territory']} Data', marker='.')

    ax.set_xlabel('Population')
    ax.set_ylabel('CO2 Emissions (metric tons per capita)')
    ax.set_zlabel('Year')
    ax.set_title(f'{country_to_plot}')

    plt.show()


if __name__ == "__main__":
    fill_missing_pm25('AFG')
    #draw_3d_function('AFG', 1990, 2019)