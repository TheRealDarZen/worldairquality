import pandas as pd
import os
import kaggle
import seaborn as sns
from preprocess_data import preprocess_data

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

#Details
file_names = ["openaq.csv", "world_population.csv"]
dataset_paths = ["mexwell/world-air-quality", "iamsouravbanerjee/world-population-dataset"]

#Data dowlnoad using API
for file_name, dataset_path in zip(file_names, dataset_paths):
    if not os.path.isfile(file_name):
        print(f"Started downloading {file_name} from kaggle.com...")
        kaggle.api.dataset_download_files(dataset_path, path=".", unzip=True)
        print("Download completed successfully.")
    else:
        print(f"File {file_name} already exists.")

#Preprocess data
data_openaq = preprocess_data("openaq.csv", ';')
data_world_population = preprocess_data("world_population.csv", ',')

print(data_openaq.head(10))
print(data_world_population.head(10))



