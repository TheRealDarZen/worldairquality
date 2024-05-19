import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
from process_data import get_processed_data
from grid_search import best_parameters

def svr_model(df, draw_plot=False):

    X = df[['Population', 'CO2', 'GDP', 'Vehicles', 'VPC', 'Area']]
    y = df['Pollution']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    parameters_grid = {
        'C': [0.1, 1, 10, 100, 1000],
        'kernel': ['rbf'],
        'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1, 10, 100],
        'epsilon': [0.01, 0.1, 0.5, 1, 5, 10]
    }

    model = SVR()
    best_model = best_parameters(model, parameters_grid, X_train, y_train)

    y_pred = best_model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("SVM - Mean Absolute Error:", mae)
    print("SVM - Mean Squared Error:", mse)
    print("SVM - R2 Score:", r2)

    residuals = y_test - y_pred

    if draw_plot:
        plt.figure(figsize=(10, 6))
        plt.scatter(y_pred, residuals, alpha=0.5)
        plt.xlabel('Predicted Pollution')
        plt.ylabel('Residuals')
        plt.title('SVR Residual Plot')
        plt.axhline(y=0, color='r', linestyle='--')
        plt.savefig('SVMResidualPlot.png')
        plt.show()

if __name__ == "__main__":
    svr_model(get_processed_data()[1], draw_plot=True)
