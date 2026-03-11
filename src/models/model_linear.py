from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


def save_results(
    results_dir: Path,
    mse: float,
    rmse: float,
    mae: float,
    r2: float,
    importance_df: pd.DataFrame
) -> None:
    """Save model evaluation metrics and top 5 feature importances to a text file."""
    results_dir.mkdir(parents=True, exist_ok=True)

    top5 = importance_df.head(5)

    results_text = (
        "Linear Regression Results\n"
        "=========================\n\n"
        "Predictor Scaling:\n"
        "  StandardScaler applied to X variables before estimation\n\n"
        f"R² score: {r2:.4f}\n"
        f"MSE: {mse:,.2f}\n"
        f"RMSE: {rmse:,.4f}\n"
        f"MAE: {mae:,.4f}\n\n"
        "Top 5 Features by Absolute Standardized Coefficient:\n"
        "---------------------------------------------------\n"
    )

    for i, (_, row) in enumerate(top5.iterrows(), start=1):
        results_text += f"{i:>2}. {row['feature']:<20} {row['abs_coefficient']:.6f}\n"

    with open(results_dir / "results_lr.txt", "w", encoding="utf-8") as file:
        file.write(results_text)


def get_feature_importance(feature_names: pd.Index, coefficients: np.ndarray) -> pd.DataFrame:
    """Create a feature importance table using absolute standardized coefficients."""
    importance_df = pd.DataFrame({
        "feature": feature_names,
        "coefficient": coefficients,
        "abs_coefficient": np.abs(coefficients)
    }).sort_values("abs_coefficient", ascending=False)

    return importance_df


def plot_actual_vs_predicted(
    figures_dir: Path,
    y_test: pd.Series,
    y_pred: np.ndarray,
    r2: float
) -> None:
    """Save actual vs predicted plot."""
    figures_dir.mkdir(parents=True, exist_ok=True)

    actual_k = y_test.to_numpy() / 1000
    pred_k = y_pred / 1000

    mask = (actual_k > 0) & (pred_k > 0)
    actual_k = actual_k[mask]
    pred_k = pred_k[mask]

    lim_low = max(min(actual_k.min(), pred_k.min()) * 0.95, 1)
    lim_high = max(actual_k.max(), pred_k.max()) * 1.05

    plt.figure(figsize=(8, 8))
    plt.scatter(actual_k, pred_k, alpha=0.15, s=10)
    plt.plot([lim_low, lim_high], [lim_low, lim_high], "--")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlim(lim_low, lim_high)
    plt.ylim(lim_low, lim_high)
    plt.xlabel("Actual INCTOT ($ thousands, log scale)")
    plt.ylabel("Predicted INCTOT ($ thousands, log scale)")
    plt.title(f"Linear Regression — Actual vs Predicted (R² = {r2:.3f})")
    plt.tight_layout()
    plt.savefig(figures_dir / "lr_actual_vs_predicted.png", dpi=150, bbox_inches="tight")
    plt.close()


def main():
    """Train and evaluate a linear regression model with standardized predictors."""
    base_path = Path(__file__).resolve().parents[2]
    data_path = base_path / "data" / "processed"
    results_dir = base_path / "reports" / "results"
    figures_dir = base_path / "reports" / "figures"

    X_train = pd.read_csv(data_path / "X_train.csv")
    X_test = pd.read_csv(data_path / "X_test.csv")
    y_train = pd.read_csv(data_path / "y_train.csv").squeeze()
    y_test = pd.read_csv(data_path / "y_test.csv").squeeze()

    feature_names = X_train.columns

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    importance_df = get_feature_importance(feature_names, model.coef_)

    print("Linear Regression Results")
    print("=========================")
    print(f"R² score: {r2:.4f}")
    print(f"MSE: {mse:,.2f}")
    print(f"RMSE: {rmse:,.4f}")
    print(f"MAE: {mae:,.4f}")

    print("\nTop 5 Features by Absolute Standardized Coefficient:")
    print("---------------------------------------------------")
    for i, (_, row) in enumerate(importance_df.head(5).iterrows(), start=1):
        print(f"{i:>2}. {row['feature']:<20} {row['abs_coefficient']:.6f}")

    save_results(results_dir, mse, rmse, mae, r2, importance_df)
    plot_actual_vs_predicted(figures_dir, y_test, y_pred, r2)

    print("\nSaved files:")
    print(f"- {results_dir / 'results_lr.txt'}")
    print(f"- {figures_dir / 'lr_actual_vs_predicted.png'}")


if __name__ == "__main__":
    main()