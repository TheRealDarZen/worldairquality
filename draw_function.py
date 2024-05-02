import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from upload_and_preprocess_data import get_preprocessed_data

# Get preprocessed data
co2_df, population_df = get_preprocessed_data()

# Merge data
merged_df = pd.merge(co2_df, population_df, left_on='country_code', right_on='CCA3', how='inner')

# Plotting
country_to_plot = 'AFG'
years_to_plot = ['1990', '2000', '2010', '2015']

# Filtering data
country_data = merged_df[merged_df['country_code'] == country_to_plot]

# Creating a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the data for the country
x_values = []
y_values = []
z_values = []

for year in years_to_plot:
    population_column = f'{year} Population'  # Construct the population column name
    x_values.append(country_data[population_column].values[0])  # Append population value
    y_values.append(country_data[year].values[0])  # Append CO2 emissions value
    z_values.append(int(year))  # Append year as integer

# Connect data points
ax.plot(x_values, y_values, z_values, label=f'{country_to_plot} Data', marker='o')

ax.set_xlabel('Population')
ax.set_ylabel('CO2 Emissions (metric tons per capita)')
ax.set_zlabel('Year')
ax.set_title(f'{country_to_plot}')

plt.show()
