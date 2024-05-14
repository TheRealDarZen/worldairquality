import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from process_data import get_processed_data
from scipy import stats
import numpy as np
import matplotlib.tri as mtri


def draw_population_pollution_year_plane(data_df):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    '''years = list(range(1990, 2018))

    for country in countries:
        country_data = data_df[data_df['Country'] == country]
        population = country_data['Population']
        pollution = country_data['Pollution']

        ax.scatter(population, pollution, years, marker='.')'''


    population = data_df['Population']
    pollution = data_df['Pollution']
    years = data_df['Year']
    surf = ax.plot_trisurf(population, pollution, years, cmap='viridis')




    ax.set_xlabel('Population')
    ax.set_ylabel('PM2.5')
    ax.set_zlabel('Year')

    plt.show()


def draw_population_pollution_year_function(country: str, data_df):
    # Filtering data
    country_data = data_df[data_df['Country'] == country]

    # Creating a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plotting the data for the country
    population = country_data['Population']
    pollution = country_data['Pollution']
    years = list(range(1990, 2018))

    # Connect data points
    ax.plot(population, pollution, years, marker='.')

    ax.set_xlabel('Population')
    ax.set_ylabel('PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)')
    ax.set_zlabel('Year')
    ax.set_title(f'{country_data['Country'].values[0]}')

    plt.show()


def population_pollution_function(year):
    _, data_df = get_processed_data()

    year_data = data_df[data_df['Year'] == year]

    population = year_data['Population']
    pollution = year_data['Pollution']

    z = np.polyfit(population, pollution, 1)
    trendline = np.poly1d(z)

    plt.scatter(population, pollution, marker='.')
    plt.plot(population, trendline(population), color='red')

    plt.xlabel('Population')
    plt.ylabel('Pollution')
    plt.title('Population vs Pollution')

    plt.grid(True)
    plt.show()


def co2_pollution_function(year):
    _, data_df = get_processed_data()

    year_data = data_df[data_df['Year'] == year]

    co2 = year_data['CO2']
    pollution = year_data['Pollution']

    z = np.polyfit(co2, pollution, 1)
    trendline = np.poly1d(z)

    plt.scatter(co2, pollution, marker='.')
    plt.plot(co2, trendline(co2), color='red')

    plt.xlabel('CO2')
    plt.ylabel('Pollution')
    plt.title('CO2 vs Pollution')

    plt.grid(True)
    plt.show()


def gdp_avg_pollution_function():
    _, data_df = get_processed_data()

    gdp_arr = []
    avg_pollution_arr = []
    countries = list(set(data_df['Country'].values))

    for country in countries:
        country_data = data_df[data_df['Country'] == country]
        gdp = country_data['GDP'].values[0]
        avg_pollution = sum(country_data['Pollution'].values) / len(country_data['Pollution'])

        gdp_arr.append(gdp)
        avg_pollution_arr.append(avg_pollution)

    z = np.polyfit(gdp_arr, avg_pollution_arr, 1)
    trendline = np.poly1d(z)

    plt.scatter(gdp_arr, avg_pollution_arr, marker='.')
    plt.plot(gdp_arr, trendline(gdp_arr), color='red')

    plt.xlabel('GDP')
    plt.ylabel('Avg Pollution')
    plt.title('GDP vs Avg Pollution')

    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    #draw_population_pollution_year_function('Algeria', get_processed_data()[1])
    #get_processed_data()
    #population_pollution_function(1990)
    #draw_population_pollution_year_plane(get_processed_data()[1])
    #co2_pollution_function(2015)
    gdp_avg_pollution_function()