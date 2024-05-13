import pandas as pd
import os
import kaggle
import seaborn as sns
from preprocess_data import preprocess_data
import requests
from bs4 import BeautifulSoup
import csv

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

#Details
file_names = ["openaq.csv", "world_population.csv", "AQI and Lat Long of Countries.csv",
              "CO2_emission.csv", "PM25-air-pollution.csv"]
dataset_paths = ["mexwell/world-air-quality", "iamsouravbanerjee/world-population-dataset",
                 "adityaramachandran27/world-air-quality-index-by-city-and-coordinates",
                 "koustavghosh149/co2-emission-around-the-world", "programmerrdai/outdoor-air-pollution"]
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita"

#Data dowlnoad using API
def download():
    # Kaggle
    for file_name, dataset_path in zip(file_names, dataset_paths):
        if not os.path.isfile(file_name):
            print(f"Started downloading {file_name} from kaggle.com...")
            kaggle.api.dataset_download_files(dataset_path, path=".", unzip=True)
            print("Download completed successfully.")
        else:
            print(f"File {file_name} already exists.")

    # Wikipedia
    csv_file = "country_gdp_per_capita.csv"
    if not os.path.isfile(csv_file):
        print(f"Started downloading {csv_file} from wikipedia.com...")

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        gdp_table = soup.find("table", class_="wikitable")

        countries = []
        gdps = []

        for row in gdp_table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) > 0:
                countries.append(cells[0].text.strip())

                num4 = str_to_num(cells[4].text.strip())
                if num4:
                    if not 2020 <= num4 <= 2024:
                        gdps.append(num4)
                    else:
                        gdps.append(str_to_num(cells[3].text.strip()))
                else:
                    gdps.append(str_to_num(cells[5].text.strip()))

        data = zip(countries, gdps)

        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Country', 'GDP'])
            writer.writerows(data)

        print("Download completed successfully.")

    else:
        print(f"File {csv_file} already exists.")


def str_to_num(item: str) -> int or None:
    if item == '—':
        return None

    parts = item.split(',')
    if len(parts) == 1:
        return int(parts[0])
    return int(parts[0]) * 1000 + int(parts[1])


#Preprocess data
def get_preprocessed_data():
    data_co2 = preprocess_data("CO2_emission.csv", ',')
    data_world_population = preprocess_data("world_population.csv", ',')
    data_pm_25 = preprocess_data("PM25-air-pollution.csv", ',')
    data_gdp = preprocess_data("country_gdp_per_capita.csv", ',')

    return data_co2, data_world_population, data_pm_25, data_gdp

if __name__ == "__main__":
    download()

