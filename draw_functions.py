import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from process_data import get_processed_data
from scipy import stats
import numpy as np


def draw_3d_function_for_country(country: str):
    # Get preprocessed data
    _, data_df = get_processed_data()

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


if __name__ == "__main__":
    #draw_3d_function_for_country('Algeria')
    #get_processed_data()
    population_pollution_function(1990)