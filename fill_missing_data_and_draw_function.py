import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from process_data import get_processed_data


def draw_3d_function_for_country(country: str):
    # Get preprocessed data
    data_dict, data_df = get_processed_data()

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
    draw_3d_function_for_country('Algeria')
    #get_processed_data()