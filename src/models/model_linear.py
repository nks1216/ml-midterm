from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def main():
    """Train and evaluate a baseline linear regression model."""
    base_path = Path(__file__).resolve().parents[2]
    data_path = base_path / "data" / "processed"

    X_train = pd.read_csv(data_path / "X_train.csv")
    X_test = pd.read_csv(data_path / "X_test.csv")
    y_train = pd.read_csv(data_path / "y_train.csv").squeeze()
    y_test = pd.read_csv(data_path / "y_test.csv").squeeze()

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Linear Regression Results")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R^2: {r2:.4f}")

    results_dir = base_path / "reports" / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    results_text = (
        "Linear Regression Results\n"
        "=========================\n\n"
        f"MSE: {mse:.2f}\n"
        f"RMSE: {rmse:.4f}\n"
        f"MAE: {mae:.4f}\n"
        f"R^2: {r2:.4f}\n"
    )

    with open(results_dir / "results_lr.txt", "w", encoding="utf-8") as file:
        file.write(results_text)


if __name__ == "__main__":
    main()