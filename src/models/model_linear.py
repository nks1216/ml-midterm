"""
model_linear.py
Train a Linear Regression model to predict individual income.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
RESULTS_DIR = PROJECT_ROOT / "reports" / "results"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"


def load_data():
    """
    Load preprocessed training and test datasets.

    Returns:
        X_train, X_test: Feature matrices
        y_train, y_test: Target vectors
    """
    X_train = pd.read_csv(PROCESSED_DIR / "X_train.csv")
    X_test = pd.read_csv(PROCESSED_DIR / "X_test.csv")
    y_train = pd.read_csv(PROCESSED_DIR / "y_train.csv").squeeze("columns")
    y_test = pd.read_csv(PROCESSED_DIR / "y_test.csv").squeeze("columns")

    print(f"Train: {len(X_train):,} rows / Test: {len(X_test):,} rows")
    print(f"Features: {X_train.shape[1]}")

    return X_train, X_test, y_train, y_test


def build_pipeline():
    """
    Build a Linear Regression pipeline with standard scaling.

    Returns:
        sklearn Pipeline with StandardScaler and LinearRegression.
    """
    return Pipeline(
        [
            ("scaler", StandardScaler()),
            ("model", LinearRegression()),
        ]
    )


def get_feature_importance(model, feature_names: pd.Index) -> pd.DataFrame:
    """
    Create a feature importance table using absolute standardized coefficients.

    Args:
        model: Trained pipeline
        feature_names: Column names from X_train

    Returns:
        DataFrame with feature, coefficient, and absolute coefficient
    """
    coefficients = model.named_steps["model"].coef_

    importance_df = (
        pd.DataFrame(
            {
                "feature": feature_names,
                "coefficient": coefficients,
                "abs_coefficient": np.abs(coefficients),
            }
        )
        .sort_values("abs_coefficient", ascending=False)
        .reset_index(drop=True)
    )

    return importance_df


def evaluate(model, X_test, y_test):
    """
    Evaluate model using R², MSE, RMSE, and MAE.

    Args:
        model: Trained pipeline
        X_test: Test features
        y_test: True test labels

    Returns:
        r2, mse, rmse, mae, y_pred
    """
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse**0.5
    mae = mean_absolute_error(y_test, y_pred)

    print("\nLinear Regression Results")
    print("=========================")
    print(f"R² score: {r2:.4f}")
    print(f"MSE: {mse:,.2f}")
    print(f"RMSE: {rmse:,.4f}")
    print(f"MAE: {mae:,.4f}")

    return r2, mse, rmse, mae, y_pred


def save_results(
    results_dir: Path,
    mse: float,
    rmse: float,
    mae: float,
    r2: float,
    importance_df: pd.DataFrame,
) -> None:
    """
    Save model evaluation metrics and top 5 feature importances to a text file.

    Args:
        results_dir: Directory where results file will be saved
        mse: Mean squared error
        rmse: Root mean squared error
        mae: Mean absolute error
        r2: R-squared
        importance_df: Feature importance DataFrame
    """
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
        results_text += (
            f"{i:>2}. {row['feature']:<20} {row['abs_coefficient']:.6f}\n"
        )

    with open(results_dir / "results_lr.txt", "w", encoding="utf-8") as file:
        file.write(results_text)

    print(f"\nResults saved to {results_dir / 'results_lr.txt'}")


def plot_feature_importance(
    figures_dir: Path,
    importance_df: pd.DataFrame,
    top_k: int = 20,
) -> None:
    """
    Plot top-k feature importances based on absolute standardized coefficients.

    Args:
        figures_dir: Directory where figure will be saved
        importance_df: Feature importance DataFrame
        top_k: Number of top features to display
    """
    figures_dir.mkdir(parents=True, exist_ok=True)

    top_features = (
        importance_df.head(top_k)
        .sort_values("abs_coefficient", ascending=True)
    )

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.barh(top_features["feature"], top_features["abs_coefficient"])
    ax.set_title(
        "Linear Regression — Top 20 Feature Importances",
        fontsize=14,
        weight="bold",
    )
    ax.set_xlabel("Absolute Standardized Coefficient")
    ax.set_ylabel("")
    ax.grid(True, axis="x", linestyle="--", alpha=0.5)

    fig.tight_layout()
    fig.savefig(
        figures_dir / "lr_feature_importance.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close(fig)

    print(
        f"Feature importance plot saved to "
        f"{figures_dir / 'lr_feature_importance.png'}"
    )


def plot_actual_vs_predicted(
    figures_dir: Path,
    y_test: pd.Series,
    y_pred: np.ndarray,
    r2: float,
) -> None:
    """
    Save actual vs predicted plot on log-log scale.

    Args:
        figures_dir: Directory where figure will be saved
        y_test: True test labels
        y_pred: Predicted test labels
        r2: R-squared
    """
    figures_dir.mkdir(parents=True, exist_ok=True)

    actual_k = y_test.to_numpy() / 1000
    pred_k = y_pred / 1000

    mask = (actual_k > 0) & (pred_k > 0)
    n_dropped = (~mask).sum()

    actual_k = actual_k[mask]
    pred_k = pred_k[mask]

    lim_low = 1
    lim_high = max(actual_k.max(), pred_k.max()) * 1.05

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.scatter(actual_k, pred_k, alpha=0.15, s=12)
    ax.plot(
        [lim_low, lim_high],
        [lim_low, lim_high],
        "r--",
        linewidth=1.5,
        label="Perfect fit",
    )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(lim_low, lim_high)
    ax.set_ylim(lim_low, lim_high)

    ax.set_xlabel("Actual INCTOT ($k, log scale)")
    ax.set_ylabel("Predicted INCTOT ($k, log scale)")
    ax.set_title(f"Linear Regression — Actual vs Predicted (R² = {r2:.3f})")
    ax.legend()
    ax.grid(True, which="major", linestyle="--", alpha=0.5)

    fig.tight_layout()
    fig.savefig(
        figures_dir / "lr_actual_vs_predicted.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close(fig)

    print(
        f"Actual vs predicted plot saved to "
        f"{figures_dir / 'lr_actual_vs_predicted.png'}"
    )

    if n_dropped > 0:
        print(
            f"Note: {n_dropped} observations were excluded from the log-scale plot "
            "because actual or predicted income was non-positive."
        )


def main():
    """Main execution: load data, train model, evaluate, save results and plots."""
    X_train, X_test, y_train, y_test = load_data()

    model = build_pipeline()
    model.fit(X_train, y_train)

    r2, mse, rmse, mae, y_pred = evaluate(model, X_test, y_test)

    importance_df = get_feature_importance(model, X_train.columns)

    print("\nTop 5 Features by Absolute Standardized Coefficient:")
    print("---------------------------------------------------")
    for i, (_, row) in enumerate(importance_df.head(5).iterrows(), start=1):
        print(f"{i:>2}. {row['feature']:<20} {row['abs_coefficient']:.6f}")

    save_results(
        results_dir=RESULTS_DIR,
        mse=mse,
        rmse=rmse,
        mae=mae,
        r2=r2,
        importance_df=importance_df,
    )

    plot_feature_importance(FIGURES_DIR, importance_df, top_k=20)
    plot_actual_vs_predicted(FIGURES_DIR, y_test, y_pred, r2)

    print("\nSaved files:")
    print(f"- {RESULTS_DIR / 'results_lr.txt'}")
    print(f"- {FIGURES_DIR / 'lr_feature_importance.png'}")
    print(f"- {FIGURES_DIR / 'lr_actual_vs_predicted.png'}")


if __name__ == "__main__":
    main()
