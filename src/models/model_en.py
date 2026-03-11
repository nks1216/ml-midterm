"""
model_en.py
Train an ElasticNet model to predict individual income.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


def load_data():
    """
    Load preprocessed training and test datasets.
    Returns:
        X_train, X_test: Feature matrices
        y_train, y_test: Target vectors (INCTOT)
    """
    X_train = pd.read_csv(PROCESSED_DIR / "X_train.csv")
    X_test = pd.read_csv(PROCESSED_DIR / "X_test.csv")
    y_train = pd.read_csv(PROCESSED_DIR / "y_train.csv").squeeze("columns")
    y_test = pd.read_csv(PROCESSED_DIR / "y_test.csv").squeeze("columns")

    print(f"  Train: {len(X_train):,} rows / Test: {len(X_test):,} rows")
    print(f"  Features: {X_train.shape[1]}")

    return X_train, X_test, y_train, y_test


def build_pipeline():
    """
    Build an ElasticNet regression pipeline with standard scaling.
    Returns:
        sklearn Pipeline with StandardScaler and ElasticNet.
    """
    return Pipeline(
        [
            ("scaler", StandardScaler()),
            ("model", ElasticNet(max_iter=10000)),
        ]
    )


def evaluate(model, X_test, y_test):
    """
    Evaluate model using R², MSE, and MAE.
    Args:
        model: Trained pipeline
        X_test: Test features
        y_test: True test labels
    Returns:
        r2, mse, mae: Evaluation metrics
    """
    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    mae = mean_absolute_error(y_test, preds)

    print(f"  Test R² score: {r2:.4f}")
    print(f"  Test MSE: {mse:,.2f}")
    print(f"  Test MAE: {mae:,.2f}")

    return r2, mse, mae


def save_results(r2, mse, mae, out_path="reports/results/results_en.txt"):
    """
    Save evaluation metrics to a text file.
    Args:
        r2, mse, mae: Evaluation metrics
        out_path: Output file path
    """
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write("ElasticNet Results\n")
        f.write("=========================\n\n")
        f.write(f"R² score: {r2:.4f}\n")
        f.write(f"MSE: {mse:,.2f}\n")
        f.write(f"MAE: {mae:,.2f}\n")

    print(f"\nResults saved to {out_path}")


def plot_feature_importance(
    model, feature_names, top_k=20, out_path="reports/figures/en_feature_importance.png"
):
    """
    Plot top-k feature importances based on ElasticNet coefficients.
    Args:
        model: Trained pipeline
        feature_names: List of feature names
        top_k: Number of top features to display
        out_path: Output file path
    """
    coefficients = model.named_steps["model"].coef_
    importance = (
        pd.Series(np.abs(coefficients), index=feature_names)
        .nlargest(top_k)
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    importance.plot(kind="barh", ax=ax, color="steelblue")
    ax.set_title("ElasticNet — Top 20 Feature Importances")
    ax.set_xlabel("Absolute Coefficient Value")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

    print(f"Feature importance plot saved to {out_path}")


def plot_actual_vs_predicted(
    model, X_test, y_test, out_path="reports/figures/en_actual_vs_predicted.png"
):
    """
    Plot actual vs predicted income values on a log scale.
    Args:
        model: Trained pipeline
        X_test: Test features
        y_test: True test labels
        out_path: Output file path
    """
    preds = model.predict(X_test)
    r2 = r2_score(y_test, preds)

    # clip to positive values only (log scale requires > 0)
    mask = (y_test > 0) & (preds > 0)
    y_plot = y_test[mask] / 1000
    p_plot = preds[mask] / 1000

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(y_plot, p_plot, alpha=0.2, color="steelblue", s=10)

    lims = [1e0, max(y_plot.max(), p_plot.max()) * 1.5]
    ax.plot(lims, lims, "r--", label="Perfect fit")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_xlabel("Actual INCTOT ($k, log scale)")
    ax.set_ylabel("Predicted INCTOT ($k, log scale)")
    ax.set_title(f"ElasticNet — Actual vs Predicted (R² = {r2:.3f})")
    ax.legend()
    plt.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path)
    plt.close()

    print(f"Actual vs Predicted plot saved to {out_path}")


def main():
    """Main execution: load data, train model, evaluate, save results and plots."""
    X_train, X_test, y_train, y_test = load_data()

    model = build_pipeline()
    model.fit(X_train, y_train)

    r2, mse, mae = evaluate(model, X_test, y_test)

    save_results(r2=r2, mse=mse, mae=mae, out_path="reports/results/results_en.txt")

    plot_feature_importance(model, X_train.columns)
    plot_actual_vs_predicted(model, X_test, y_test)


if __name__ == "__main__":
    main()
