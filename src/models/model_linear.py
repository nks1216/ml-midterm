from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


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


def save_feature_importance_table(
    results_dir: Path,
    feature_names: pd.Index,
    coefficients: np.ndarray
) -> pd.DataFrame:
    """
    Save standardized coefficient-based feature importance table.
    For linear regression, after standardizing X, absolute coefficient size
    is a reasonable way to compare relative importance across features.
    """
    results_dir.mkdir(parents=True, exist_ok=True)

    importance_df = pd.DataFrame({
        "feature": feature_names,
        "coefficient": coefficients,
        "abs_coefficient": np.abs(coefficients)
    }).sort_values("abs_coefficient", ascending=False)

    importance_df.to_csv(results_dir / "lr_feature_importance.csv", index=False)
    importance_df.head(5).to_csv(results_dir / "lr_top5_features.csv", index=False)

    return importance_df


def plot_actual_vs_predicted(
    figures_dir: Path,
    y_test: pd.Series,
    y_pred: np.ndarray,
    r2: float
) -> None:
    """
    Save actual vs predicted plot.
    Axes are forced to start above zero for a cleaner presentation.
    """
    figures_dir.mkdir(parents=True, exist_ok=True)

    actual_k = y_test.to_numpy() / 1000
    pred_k = y_pred / 1000

    # Keep only positive values for presentation
    mask = (actual_k > 0) & (pred_k > 0)
    actual_k = actual_k[mask]
    pred_k = pred_k[mask]

    # Use positive lower bound so plot never starts at/below zero
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


def plot_residuals(
    figures_dir: Path,
    y_test: pd.Series,
    y_pred: np.ndarray
) -> None:
    """
    Save residual plot.
    Residuals should cross zero, so we keep the horizontal zero line.
    """
    figures_dir.mkdir(parents=True, exist_ok=True)

    residuals = y_test.to_numpy() - y_pred

    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, alpha=0.3, s=10)
    plt.axhline(0, linestyle="--")
    plt.xlabel("Predicted INCTOT")
    plt.ylabel("Residuals")
    plt.title("Linear Regression — Residual Plot")
    plt.tight_layout()
    plt.savefig(figures_dir / "lr_residual_plot.png", dpi=150, bbox_inches="tight")
    plt.close()


def plot_feature_importance_top24(
    figures_dir: Path,
    importance_df: pd.DataFrame
) -> None:
    """
    Plot top 24 features ranked by absolute standardized coefficient.
    """
    figures_dir.mkdir(parents=True, exist_ok=True)

    top24 = importance_df.head(24).copy()
    top24 = top24.sort_values("abs_coefficient", ascending=True)

    plt.figure(figsize=(10, 9))
    plt.barh(top24["feature"], top24["abs_coefficient"])
    plt.xlabel("Absolute Standardized Coefficient")
    plt.ylabel("Feature")
    plt.title("Linear Regression — Top 24 Feature Importances")
    plt.tight_layout()
    plt.savefig(figures_dir / "lr_feature_importance_top24.png", dpi=150, bbox_inches="tight")
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

    # Standardize predictors so coefficients are comparable across variables
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

    print("Linear Regression Results")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R^2: {r2:.4f}")

    save_results(results_dir, mse, rmse, mae, r2)

    importance_df = save_feature_importance_table(
        results_dir=results_dir,
        feature_names=feature_names,
        coefficients=model.coef_
    )

    plot_actual_vs_predicted(figures_dir, y_test, y_pred, r2)
    plot_residuals(figures_dir, y_test, y_pred)
    plot_feature_importance_top24(figures_dir, importance_df)

    print("\nTop 5 features by absolute standardized coefficient:")
    print(importance_df.head(5)[["feature", "coefficient", "abs_coefficient"]])

    print("\nSaved files:")
    print(f"- {results_dir / 'results_lr.txt'}")
    print(f"- {results_dir / 'lr_feature_importance.csv'}")
    print(f"- {results_dir / 'lr_top5_features.csv'}")
    print(f"- {figures_dir / 'lr_actual_vs_predicted.png'}")
    print(f"- {figures_dir / 'lr_residual_plot.png'}")
    print(f"- {figures_dir / 'lr_feature_importance_top24.png'}")


if __name__ == "__main__":
    main()