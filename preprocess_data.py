import pandas as pd

def preprocess_data(file_name, delimeter):
    data = pd.read_csv(file_name, delimiter=delimeter, index_col=[0])

    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

    return data