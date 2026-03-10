from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def save_results(results_dir: Path, mse: float, rmse: float, mae: float, r2: float) -> None:
    """Save model evaluation metrics to a text file."""
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


def plot_actual_vs_predicted(figures_dir: Path, y_test: pd.Series, y_pred: np.ndarray, r2: float) -> None:
    """Save a cleaner actual vs predicted plot using only positive predictions."""
    figures_dir.mkdir(parents=True, exist_ok=True)

    actual_k = y_test / 1000
    pred_k = y_pred / 1000

    # Keep only positive predictions for log-scale plotting
    mask = pred_k > 0
    actual_k = actual_k[mask]
    pred_k = pred_k[mask]

    lim_low = min(actual_k.min(), pred_k.min()) * 0.9
    lim_high = max(actual_k.max(), pred_k.max()) * 1.1

    plt.figure(figsize=(8, 8))
    plt.scatter(actual_k, pred_k, alpha=0.15, s=10)
    plt.plot([lim_low, lim_high], [lim_low, lim_high], "--")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlim(lim_low, lim_high)
    plt.ylim(lim_low, lim_high)
    plt.xlabel("Actual INCTOT ($k, log scale)")
    plt.ylabel("Predicted INCTOT ($k, log scale)")
    plt.title(f"Linear Regression — Actual vs Predicted (R² = {r2:.3f})")
    plt.tight_layout()
    plt.savefig(figures_dir / "lr_actual_vs_predicted.png", dpi=150, bbox_inches="tight")
    plt.close()


def plot_residuals(figures_dir: Path, y_test: pd.Series, y_pred: np.ndarray) -> None:
    """Save residual plot."""
    figures_dir.mkdir(parents=True, exist_ok=True)

    residuals = y_test - y_pred

    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, alpha=0.3, s=10)
    plt.axhline(0, linestyle="--")
    plt.xlabel("Predicted INCTOT")
    plt.ylabel("Residuals")
    plt.title("Linear Regression — Residual Plot")
    plt.tight_layout()
    plt.savefig(figures_dir / "lr_residual_plot.png", dpi=150, bbox_inches="tight")
    plt.close()


def main():
    """Train and evaluate a baseline linear regression model."""
    base_path = Path(__file__).resolve().parents[2]
    data_path = base_path / "data" / "processed"
    results_dir = base_path / "reports" / "results"
    figures_dir = base_path / "reports" / "figures"

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

    save_results(results_dir, mse, rmse, mae, r2)
    plot_actual_vs_predicted(figures_dir, y_test, y_pred, r2)
    plot_residuals(figures_dir, y_test, y_pred)

    print("\nSaved files:")
    print(f"- {results_dir / 'results_lr.txt'}")
    print(f"- {figures_dir / 'lr_actual_vs_predicted.png'}")
    print(f"- {figures_dir / 'lr_residual_plot.png'}")


if __name__ == "__main__":
    main()