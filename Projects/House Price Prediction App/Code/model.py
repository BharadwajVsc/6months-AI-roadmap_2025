import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
    ElasticNet,
    SGDRegressor,
    HuberRegressor,
)
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
import lightgbm as lgb
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import pickle

df = pd.read_csv(
    r"D:\fsds\projects\datasets\house price prediction app\USA_Housing.csv"
)

X = df.drop(["Price", "Address"], axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "LinearRegression": LinearRegression(),
    "RobustRegression": HuberRegressor(),
    "RidgeRegression": Ridge(),
    "LassoRegression": Lasso(),
    "ElasticNet": ElasticNet(),
    "PolynomialRegression": Pipeline(
        [("poly", PolynomialFeatures(degree=4)), ("linear", LinearRegression())]
    ),
    "SGDRegressor": SGDRegressor(),
    "ANN": MLPRegressor(hidden_layer_sizes=(100,), max_iter=1000),
    "RandomForest": RandomForestRegressor(),
    "SVM": SVR(),
    "LGBM": lgb.LGBMRegressor(),
    "XGBoost": XGBRegressor(),
    "KNN": KNeighborsRegressor(),
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results.append({"Model": name, "MAE": mae, "MSE": mse, "R2": r2})
    with open(f"{name}.pkl", "wb") as f:
        pickle.dump(model, f)

results_df = pd.DataFrame(results)
results_df.to_csv("model_evaluation_results.csv", index=False)

print(
    "Model training and evaluation completed. Results saved to 'model_evaluation_results.csv'."
)
