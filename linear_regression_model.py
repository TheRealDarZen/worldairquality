import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from process_data import get_processed_data
import matplotlib.pyplot as plt

def model(df):

    # Selecting features and target variable
    X = df[['Population', 'CO2', 'GDP', 'Vehicles']]
    y = df['Pollution']

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Creating and training the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Making predictions
    y_pred = model.predict(X_test)

    # Evaluating the model
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)

    # Coefficients and intercept
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)

    # Calculating residuals
    residuals = y_test - y_pred

    # Plotting residuals
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.xlabel('Predicted Pollution')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    plt.axhline(y=0, color='r', linestyle='--')  # Adding a horizontal line at y=0
    plt.show()


if __name__ == "__main__":
    model(get_processed_data()[1])
