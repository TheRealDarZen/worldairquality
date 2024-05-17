from sklearn.model_selection import GridSearchCV


def best_parameters(model, parameters, X, y, cv=5, scoring='neg_mean_squared_error'):
    grid_search = GridSearchCV(estimator=model, param_grid=parameters, cv=cv,
                               scoring=scoring,n_jobs=-1)
    grid_search.fit(X, y)
    return grid_search.best_estimator_
