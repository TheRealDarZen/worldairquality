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

def neural_network_model(df):

    X = df[['Population', 'CO2', 'GDP', 'Vehicles', 'VPC', 'Area']]
    y = df['Pollution']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = Sequential()
    model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')

    # Training the model
    history = model.fit(X_train, y_train, epochs=100, batch_size=10, validation_split=0.1, verbose=1)


    # Making predictions
    y_pred = model.predict(X_test)

    # Evaluating the model
    mae = mean_absolute_error(y_test, y_pred)
    print("Neural Network - Mean Absolute Error:", mae)
    mse = mean_squared_error(y_test, y_pred)
    print("Neural Network - Mean Squared Error:", mse)

    # Calculating residuals
    residuals = y_test - y_pred.flatten()

    # Plotting residuals
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.xlabel('Predicted Pollution')
    plt.ylabel('Residuals')
    plt.title('Neural Network Residual Plot')
    plt.axhline(y=0, color='r', linestyle='--')  # Adding a horizontal line at y=0
    plt.savefig('NeuralNetworkResidualPlot.png')
    plt.show()

    # Plot training & validation loss values
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
