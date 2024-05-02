import pandas as pd
import os
import kaggle
import seaborn as sns
from preprocess_data import preprocess_data

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

#Details
file_names = ["openaq.csv", "world_population.csv", "AQI and Lat Long of Countries.csv",
              "CO2_emission.csv", "PM25-air-pollution.csv"]
dataset_paths = ["mexwell/world-air-quality", "iamsouravbanerjee/world-population-dataset",
                 "adityaramachandran27/world-air-quality-index-by-city-and-coordinates",
                 "koustavghosh149/co2-emission-around-the-world", "programmerrdai/outdoor-air-pollution"]

#Data dowlnoad using API
def download():
    for file_name, dataset_path in zip(file_names, dataset_paths):
        if not os.path.isfile(file_name):
            print(f"Started downloading {file_name} from kaggle.com...")
            kaggle.api.dataset_download_files(dataset_path, path=".", unzip=True)
            print("Download completed successfully.")
        else:
            print(f"File {file_name} already exists.")

#Preprocess data
def get_preprocessed_data():
    data_co2 = preprocess_data("CO2_emission.csv", ',')
    data_world_population = preprocess_data("world_population.csv", ',')

    return data_co2, data_world_population

if __name__ == "__main__":
    download()

