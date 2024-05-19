import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from process_data import get_processed_data
from grid_search import best_parameters
from sklearn.metrics import r2_score


def create_model(activation_func='relu'):
    model = Sequential()
    model.add(Dense(64, activation=activation_func))
    model.add(Dense(32, activation=activation_func))
    model.add(Dense(16, activation=activation_func))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')

    return model
def neural_network_model(df, draw_plot=False):
    # Extracting data
    X = df[['Population', 'CO2', 'GDP', 'Vehicles', 'VPC', 'Area']]
    y = df['Pollution']

    # Creating training and test databases
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Creating a model
    model = create_model()

    history = model.fit(X_train, y_train, epochs=500, batch_size=32, validation_split=0.1, verbose=0)

    '''parameters_grid = {
        'epochs': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'batch_size': [8, 16, 32, 64, 128, 256, 512]
    }

    best_model = best_parameters(model, parameters_grid, X_train, y_train)'''

    y_pred = model.predict(X_test)

    # Printing results
    mae = mean_absolute_error(y_test, y_pred)
    print("Neural Network - Mean Absolute Error:", mae)
    mse = mean_squared_error(y_test, y_pred)
    print("Neural Network - Mean Squared Error:", mse)
    r2 = r2_score(y_test, y_pred)
    print("Neural Network - R2 Score:", r2)

    residuals = y_test - y_pred.flatten()

    # Drawing plots
    if draw_plot:
        plt.figure(figsize=(10, 6))
        plt.scatter(y_pred, residuals, alpha=0.5)
        plt.xlabel('Predicted Pollution')
        plt.ylabel('Residuals')
        plt.title('Neural Network Residual Plot')
        plt.axhline(y=0, color='r', linestyle='--')
        plt.savefig('NeuralNetworkResidualPlot.png')
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('Model loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc='upper left')
        plt.savefig('NeuralNetworkTrainingLoss.png')
        plt.show()


if __name__ == "__main__":
    neural_network_model(get_processed_data()[1])
