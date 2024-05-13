from upload_and_preprocess_data import get_preprocessed_data
import pandas as pd


def fill_missing_population(country: str):
    # Read the world population data from the CSV file
    _, population_df, _, _ = get_preprocessed_data()

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
    _, _, pm25_df, _ = get_preprocessed_data()

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


def fill_missing_co2(country: str):
    co2_df, _, _, _ = get_preprocessed_data()

    country_data = co2_df[co2_df['country_code'] == country]

    years_av = list(range(1990, 2020))

    co2 = []

    for year in years_av:
        co2.append(country_data[f'{year}'].values[0])

    return co2

def get_processed_data():
    co2_df, population_df, pm25_df, gdp_df = get_preprocessed_data()

    # All countries and years considered
    countries = population_df['Country/Territory'].values
    country_symbols = population_df['CCA3'].values
    years = list(range(1990, 2018))

    # Creating a dictionary with data for each country (Year, Population, Pollution)
    country_years_populations_pollutions_co2 = []

    for index, country in enumerate(countries):
        country_symbol = country_symbols[index]
        if (pm25_df[pm25_df['Code'] == country_symbol].empty
                or co2_df[co2_df['country_code'] == country_symbol].empty
                or country not in gdp_df.index):
            continue

        population = fill_missing_population(country_symbol)[:-3] # 2020-3=2017
        pollution = fill_missing_pm25(country_symbol)
        co2 = fill_missing_co2(country_symbol)[:-2] # 2020-3=2017
        gdp = gdp_df[gdp_df.index == country]['GDP'].values[0]

        data_for_country = {'Country': country, 'Code': country_symbol, 'Year': years, 'Population': population, 'Pollution': pollution, 'CO2': co2, 'GDP': gdp}
        country_years_populations_pollutions_co2.append(data_for_country)

    # Creating a dataframe with the data from the dictionary above
    dataframes = []

    for cell in country_years_populations_pollutions_co2:
        country_cloned = [cell['Country']] * len(years)
        code_cloned = [cell['Code']] * len(years)
        gdp_cloned = [cell['GDP']] * len(years)
        data = {
            'Country': country_cloned,
            'Code': code_cloned,
            'Year': cell['Year'],
            'Population': cell['Population'],
            'Pollution': cell['Pollution'],
            'CO2': cell['CO2'],
            'GDP': gdp_cloned
        }
        df = pd.DataFrame(data)
        dataframes.append(df)

    combined_dataframe = pd.concat(dataframes, ignore_index=True)

    return country_years_populations_pollutions_co2, combined_dataframe


if __name__ == "__main__":
    print(get_processed_data()[1])