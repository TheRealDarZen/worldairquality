import sys

from process_data import get_processed_data
from upload_and_preprocess_data import get_preprocessed_data

from random_forest_model import random_forest_model
from linear_regression_model import linear_regression_model
from simple_neural_network_model import neural_network_model
from svm_model import svr_model

import draw_functions as fmddf

if __name__ == "__main__":
    data_df = get_processed_data()[1]
    neural_network_model(data_df, True)
    linear_regression_model(data_df, True)
    random_forest_model(data_df, True)
    svr_model(data_df, True)
