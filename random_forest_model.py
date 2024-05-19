import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
from process_data import get_processed_data
from grid_search import best_parameters
from sklearn.metrics import r2_score


def random_forest_model(df, draw_plot=False):
    # Extracting data
    X = df[['Population', 'CO2', 'GDP', 'Vehicles', 'VPC', 'Area']]
    y = df['Pollution']

    # Creating training and test databases
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    model = RandomForestRegressor(n_jobs=-1, random_state=42)

    # Creating a model and choosing best parameters
    parameters_grid = {
        'n_estimators': [100, 200, 300, 400, 500]
    }

    best_model = best_parameters(model, parameters_grid, X_train, y_train)

    y_pred = best_model.predict(X_test)

    # Printing results
    mae = mean_absolute_error(y_test, y_pred)
    print("Random Forest - Mean Absolute Error:", mae)
    mse = mean_squared_error(y_test, y_pred)
    print("Random Forest - Mean Squared Error:", mse)
    r2 = r2_score(y_test, y_pred)
    print("Random Forest - R2 Score:", r2)

    residuals = y_test - y_pred

    # Drawing a plot
    if draw_plot:
        plt.figure(figsize=(10, 6))
        plt.scatter(y_pred, residuals, alpha=0.5)
        plt.xlabel('Predicted Pollution')
        plt.ylabel('Residuals')
        plt.title('Random Forest Residual Plot')
        plt.axhline(y=0, color='r', linestyle='--')
        plt.savefig('RandomForestResidualPlot.png')
        plt.show()


if __name__ == "__main__":
    random_forest_model(get_processed_data()[1])
