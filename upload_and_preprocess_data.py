import pandas as pd
import os
import kaggle
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

#Details
file_name = "openaq.csv"
dataset_path = "mexwell/world-air-quality"

#Data dowlnoad using API
if not os.path.isfile(file_name):
    print(f"Started downloading {file_name} from kaggle.com...")
    kaggle.api.dataset_download_files(dataset_path, path=".", unzip=True)
    print("Download completed successfully.")
else:
    print(f"File {file_name} already exists.")

#Preprocess data
data = pd.read_csv(file_name, delimiter=';', index_col=[0])
data.head()
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
#data = data.fillna(data.mean(axis=0))
print(data.head(10))



