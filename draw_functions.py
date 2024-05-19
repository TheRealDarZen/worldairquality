import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from process_data import get_processed_data
from scipy import stats
import numpy as np
import matplotlib.tri as mtri

def draw_plots(df):

    # 1990
    data_1990 = df[df['Year'] == 1990]
    draw_2d_plot(data_1990['Population'], data_1990['Pollution'],
                 'PopulationPollution1990', 'Population', 'Pollution')
    draw_2d_plot(data_1990['CO2'], data_1990['Pollution'],
                 'CO2Pollution1990', 'CO2 (metric tons per capita)', 'Pollution')
    draw_2d_plot(data_1990['Area'], data_1990['Pollution'],
                 'AreaPollution1990', 'Area (km^2)', 'Pollution')
    draw_2d_plot(data_1990['VPC'], data_1990['Pollution'],
                 'VPCPollution1990', 'Vehicles per capita', 'Pollution')
    # 2000
    data_2000 = df[df['Year'] == 2000]
    draw_2d_plot(data_2000['Population'], data_2000['Pollution'],
                 'PopulationPollution2000', 'Population', 'Pollution')
    draw_2d_plot(data_2000['CO2'], data_2000['Pollution'],
                 'CO2Pollution2000', 'CO2 (metric tons per capita)', 'Pollution')
    draw_2d_plot(data_2000['Area'], data_2000['Pollution'],
                 'AreaPollution2000', 'Area (km^2)', 'Pollution')
    draw_2d_plot(data_2000['VPC'], data_2000['Pollution'],
                 'VPCPollution2000', 'Vehicles per capita', 'Pollution')
    # 2010
    data_2010 = df[df['Year'] == 2010]
    draw_2d_plot(data_2010['Population'], data_2010['Pollution'],
                 'PopulationPollution2010', 'Population', 'Pollution')
    draw_2d_plot(data_2010['CO2'], data_2010['Pollution'],
                 'CO2Pollution2010', 'CO2 (metric tons per capita)', 'Pollution')
    draw_2d_plot(data_2010['Area'], data_2010['Pollution'],
                 'AreaPollution2010', 'Area (km^2)', 'Pollution')
    draw_2d_plot(data_2010['VPC'], data_2010['Pollution'],
                 'VPCPollution2010', 'Vehicles per capita', 'Pollution')
    # 2015
    data_2015 = df[df['Year'] == 2015]
    draw_2d_plot(data_2015['Population'], data_2015['Pollution'],
                 'PopulationPollution2015', 'Population', 'Pollution')
    draw_2d_plot(data_2015['CO2'], data_2015['Pollution'],
                 'CO2Pollution2015', 'CO2 (metric tons per capita)', 'Pollution')
    draw_2d_plot(data_2015['Area'], data_2015['Pollution'],
                 'AreaPollution2015', 'Area (km^2)', 'Pollution')
    draw_2d_plot(data_2015['VPC'], data_2015['Pollution'],
                 'VPCPollution2015', 'Vehicles per capita', 'Pollution')
    # Other
    gdp_avg_pollution_function(df)
    vehicles_avg_pollution_function(df)


def draw_2d_plot(dataX, dataY, name: str, Xname: str, Yname: str):

    z = np.polyfit(dataX, dataY, 1)
    trendline = np.poly1d(z)

    fig, ax = plt.subplots()
    ax.scatter(dataX, dataY, marker='.')
    ax.plot(dataX, trendline(dataX), color='red')

    ax.set_xlabel(Xname)
    ax.set_ylabel(Yname)
    ax.set_title(f'{Xname} vs {Yname}')
    ax.grid(True)

    x_min, x_max = np.percentile(dataX, [2.5, 95.0])
    y_min, y_max = np.percentile(dataY, [2.5, 95.0])
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    plt.savefig(f'{name}.png')
    #plt.show()


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
    ax.set_ylabel('Pollution (micrograms per cubic meter)')
    ax.set_zlabel('Year')
    ax.set_title(f'{country_data['Country'].values[0]}')

    plt.savefig('PopulationPollutionYear.png')

    plt.show()


def gdp_avg_pollution_function(df):
    data_df = df

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

    fig, ax = plt.subplots()
    ax.scatter(gdp_arr, avg_pollution_arr, marker='.')
    ax.plot(gdp_arr, trendline(gdp_arr), color='red')

    ax.set_xlabel('GDP')
    ax.set_ylabel('Average pollution')
    ax.set_title('GDP vs Average pollution')
    ax.grid(True)

    x_min, x_max = np.percentile(gdp_arr, [2.5, 95.0])
    y_min, y_max = np.percentile(avg_pollution_arr, [2.5, 95.0])
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    plt.grid(True)

    plt.savefig('GDPAvgPollution.png')

    #plt.show()


def vehicles_avg_pollution_function(df):
    data_df = df

    vehicles_arr = []
    avg_pollution_arr = []
    countries = list(set(data_df['Country'].values))

    for country in countries:
        country_data = data_df[data_df['Country'] == country]
        vehicles = country_data['GDP'].values[0]
        avg_pollution = sum(country_data['Pollution'].values) / len(country_data['Pollution'])

        vehicles_arr.append(vehicles)
        avg_pollution_arr.append(avg_pollution)

    z = np.polyfit(vehicles_arr, avg_pollution_arr, 1)
    trendline = np.poly1d(z)

    fig, ax = plt.subplots()
    ax.scatter(vehicles_arr, avg_pollution_arr, marker='.')
    ax.plot(vehicles_arr, trendline(vehicles_arr), color='red')

    ax.set_xlabel('Vehicles')
    ax.set_ylabel('Average pollution')
    ax.set_title('Vehicles vs Average pollution')
    ax.grid(True)

    x_min, x_max = np.percentile(vehicles_arr, [2.5, 95.0])
    y_min, y_max = np.percentile(avg_pollution_arr, [2.5, 95.0])
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    plt.grid(True)

    plt.savefig('VehiclesAvgPollution.png')

    # plt.show()


if __name__ == "__main__":
    data_df = get_processed_data()[1]
    draw_population_pollution_year_function('Ukraine', data_df)
    #get_processed_data()
    #population_pollution_function(1990)
    #draw_population_pollution_year_plane(data_df)
    #co2_pollution_function(2015)
    #gdp_avg_pollution_function()
    draw_plots(data_df)