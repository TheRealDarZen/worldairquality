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
                filled_population.append((filled_population[-1] + add_on_step))

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
            add_on_step = value_dif / steps

            for _ in range(steps):
                filled_pollution.append((filled_pollution[-1] + add_on_step))

    return filled_pollution


def get_processed_data():
    co2_df, population_df, pm25_df = get_preprocessed_data()

    # All countries and years considered
    countries = population_df['Country/Territory'].values
    country_symbols = population_df['CCA3'].values
    years = []
    for i in range(28): # 1990-2017
        years.append(i+1990)

    # Creating a dictionary with data for each country (Year, Population, Pollution)
    country_years_populations_pollutions = []

    for index, country in enumerate(countries):
        country_symbol = country_symbols[index]

        population = fill_missing_population(country_symbol)[:-3] # 2020-3=2017
        pollution = fill_missing_pm25(country_symbol)

        data_for_country = {'Country': country, 'Year': years, 'Population': population, 'Pollution': pollution}
        country_years_populations_pollutions.append(data_for_country)

    # Creating a dataframe with the data from the dictionary above
    dataframes = []

    for cell in country_years_populations_pollutions:
        country_cloned = [cell['Country']] * len(years)
        data = {
            'Country': country_cloned,
            'Year': cell['Year'],
            'Population': cell['Population'],
            'PM2.5 Pollution (µg/m³)': cell['Pollution']
        }
        df = pd.DataFrame(data)
        dataframes.append(df)

    combined_dataframe = pd.concat(dataframes, ignore_index=True)
    print(combined_dataframe)

    return country_years_populations_pollutions, combined_dataframe


def draw_3d_function(country: str, start_year: int, end_year: int):
    # Get preprocessed data
    co2_df, population_df, pm25_df = get_preprocessed_data()

    # Merge data
    merged_df = pd.merge(pm25_df, population_df, left_on='Code', right_on='CCA3', how='inner')

    # Plotting
    country_to_plot = country

    # Filtering data
    country_data = merged_df[merged_df['Code'] == country_to_plot]

    # Creating a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plotting the data for the country
    population_raw = fill_missing_population(country)
    population = []
    pollution_raw = fill_missing_pm25(country)
    pollution = []
    years = []

    # Fill arrays with data
    for i in range(end_year - start_year + 1):
        year = i + start_year
        population.append(population_raw[i])
        pollution.append(pollution_raw[i])
        years.append(year)

    # Connect data points
    ax.plot(population, pollution, years, marker='.')

    ax.set_xlabel('Population')
    ax.set_ylabel('PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)')
    ax.set_zlabel('Year')
    ax.set_title(f'{country_data['Country/Territory'].values[0]}')

    data = {
        'Year': years,
        'Population': population,
        'PM2.5 Pollution (µg/m³)': pollution
    }

    df = pd.DataFrame(data)

    print(df)

    plt.show()


def population_pollution_function(year):
    _, population_df, pm25_df = get_preprocessed_data()

    merged_df = pd.merge(pm25_df, population_df, left_on='Code', right_on='CCA3', how='inner')





if __name__ == "__main__":
    #draw_3d_function('AFG', 1990, 2017) # max. 2017 for now
    get_processed_data()