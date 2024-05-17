import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
from process_data import get_processed_data


def model(df):

    X = df[['Population', 'CO2', 'GDP', 'Vehicles', 'VPC', 'Area']]
    y = df['Pollution']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    model = LinearRegression(n_jobs=-1)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    print("Linear Regression - Mean Absolute Error:", mae)
    mse = mean_squared_error(y_test, y_pred)
    print("Linear Regression - Mean Squared Error:", mse)

    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)

    residuals = y_test - y_pred

    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.xlabel('Predicted Pollution')
    plt.ylabel('Residuals')
    plt.title('Linear Regression Residual Plot')
    plt.axhline(y=0, color='r', linestyle='--')  # Adding a horizontal line at y=0
    plt.savefig('LinearRegressionResidualPlot.png')
    plt.show()


if __name__ == "__main__":
    model(get_processed_data()[1])
