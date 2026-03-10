"""
IPUMS CPS Feature Importance Modeling (Random Forest)

Reads preprocessed train/test splits from data/processed/ and runs a
Random Forest model to identify variables influencing INCTOT.
Produces two diagnostic figures (rf_feature_importance.png, rf_actual_vs_predicted.png)
saved to reports/figures/
and a results summary text file saved to reports/results/results_rf.txt.

Prerequisite: run src/data_clean.py first to generate the CSV splits.
"""

import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

warnings.filterwarnings("ignore")

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUTS_DIR = PROJECT_ROOT / "reports" / "figures"


def load_splits(processed_dir):
    """Load train/test CSV splits saved by data_clean.py.

    Args:
        processed_dir: Path to directory containing CSV splits.
    Returns:
        Tuple of (X_train, X_test, y_train, y_test).
    """
    X_train = pd.read_csv(processed_dir / "X_train.csv")
    X_test = pd.read_csv(processed_dir / "X_test.csv")
    y_train = pd.read_csv(processed_dir / "y_train.csv").squeeze("columns")
    y_test = pd.read_csv(processed_dir / "y_test.csv").squeeze("columns")
    return X_train, X_test, y_train, y_test


def fit_random_forest(X_train, y_train, feature_names):
    """Fit a Random Forest and return sorted feature importances.

    Args:
        X_train: Training features.
        y_train: Training target.
        feature_names: List of feature column names.
    Returns:
        Tuple of (fitted model, Series of importances sorted descending).
    """
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=15,
        n_jobs=-1,
        random_state=42,
    )
    model.fit(X_train, y_train)

    importances = (
        pd.Series(model.feature_importances_, index=feature_names)
        .sort_values(ascending=False)
    )
    return model, importances


def print_top_features(importances, n=20):
    """Print top N features with their importance scores.

    Args:
        importances: Series of feature importances.
        n: Number of top features to show.
    """
    print(f"\n{'=' * 60}")
    print(f"  Random Forest - Top {n} Features")
    print(f"{'=' * 60}")
    for rank, (name, score) in enumerate(importances.head(n).items(), 1):
        print(f"  {rank:>2}. {name:<20s} {score:.6f}")


def plot_feature_importance(importances, n=20, save_dir=OUTPUTS_DIR):
    """Generate and save feature importance bar chart.

    Args:
        importances: Series of feature importances sorted descending.
        n: Number of top features to display.
        save_dir: Directory to save the output figure.
    """
    sns.set_theme(style="whitegrid", palette="muted", font_scale=1.0)
    fig, ax = plt.subplots(figsize=(8, 6))

    top = importances.head(n)
    sns.barplot(x=top.values, y=top.index, ax=ax, color="steelblue")
    ax.set_title(f"Random Forest — Top {n} Feature Importances", fontsize=13, fontweight="bold")
    ax.set_xlabel("Mean Impurity Decrease")
    ax.set_ylabel("")

    plt.tight_layout()
    save_dir.mkdir(parents=True, exist_ok=True)
    out_path = save_dir / "rf_feature_importance.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\n  Figure saved → {out_path.relative_to(PROJECT_ROOT)}")


def plot_actual_vs_predicted(y_test, y_pred, r2_score, mse=None, mae=None, save_dir=OUTPUTS_DIR):
    """Generate and save actual vs predicted scatter plot.

    Args:
        y_test: True target values (test set).
        y_pred: Predicted target values (test set).
        r2_score: Test R² score.
        mse: Mean Squared Error (optional, shown in subtitle).
        mae: Mean Absolute Error (optional, shown in subtitle).
        save_dir: Directory to save the output figure.
    """
    sns.set_theme(style="whitegrid", palette="muted", font_scale=1.0)
    fig, ax = plt.subplots(figsize=(8, 7))

    subtitle = f"R² = {r2_score:.4f}"
    ax.set_title(f"Actual vs Predicted\n{subtitle}", fontsize=13, fontweight="bold")

    # Clip to 1 ($1k) so log scale starts at 10^0
    y_test_k = np.clip(y_test / 1_000, 1.0, None)
    y_pred_k = np.clip(y_pred / 1_000, 1.0, None)
    lim_high = max(y_test_k.max(), y_pred_k.max()) * 1.1
    sns.scatterplot(x=y_test_k, y=y_pred_k, ax=ax, alpha=0.15, s=10, color="steelblue")
    ax.plot([1.0, lim_high], [1.0, lim_high],
            color="tomato", linewidth=1.2, linestyle="--", label="Perfect fit")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1.0, lim_high)
    ax.set_ylim(1.0, lim_high)
    ax.set_xlabel("Actual INCTOT ($k, log scale)")
    ax.set_ylabel("Predicted INCTOT ($k, log scale)")
    ax.legend(fontsize=9)

    plt.tight_layout()
    save_dir.mkdir(parents=True, exist_ok=True)
    out_path = save_dir / "rf_actual_vs_predicted.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Figure saved → {out_path.relative_to(PROJECT_ROOT)}")


RESULTS_DIR = PROJECT_ROOT / "reports" / "results"


def save_results_txt(importances, r2_score, mse, mae, n=20, save_dir=RESULTS_DIR):
    """Save model results to a text file in standardized format.

    Args:
        importances: Series of feature importances sorted descending.
        r2_score: Test R² score.
        mse: Mean Squared Error.
        mae: Mean Absolute Error.
        n: Number of top features to include.
        save_dir: Directory to save the output file.
    """
    save_dir.mkdir(parents=True, exist_ok=True)
    out_path = save_dir / "results_rf.txt"

    lines = [
        "Random Forest Results",
        "=========================",
        "",
        "Best Parameters:",
        "  n_estimators: 200",
        "  max_depth: 15",
        "",
        f"R² score: {r2_score:.4f}",
        f"MSE: {mse:,.2f}",
        f"MAE: {mae:,.2f}",
        "",
        f"Top {n} Feature Importances:",
        "---------------------------",
    ]
    for rank, (name, score) in enumerate(importances.head(n).items(), 1):
        lines.append(f"  {rank:>2}. {name:<20s} {score:.6f}")

    out_path.write_text("\n".join(lines) + "\n")
    print(f"  Results saved → {out_path.relative_to(PROJECT_ROOT)}")


def main():
    """Run Random Forest feature importance analysis."""
    print("Loading preprocessed data...")
    X_train, X_test, y_train, y_test = load_splits(PROCESSED_DIR)
    print(f"  Train: {X_train.shape[0]:,} rows / Test: {X_test.shape[0]:,} rows")
    print(f"  Features: {X_train.shape[1]}")

    feature_names = list(X_train.columns)

    print("\nTraining Random Forest...")
    model, importances = fit_random_forest(X_train, y_train, feature_names)

    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"\n{'=' * 60}")
    print(f"  Model Evaluation")
    print(f"{'=' * 60}")
    print(f"  R²  : {score:.4f}")
    print(f"  MSE : {mse:>15,.0f}  (${mse ** 0.5:,.0f} RMSE)")
    print(f"  MAE : {mae:>15,.0f}  (${mae:,.0f})")

    print_top_features(importances)

    print("\nGenerating diagnostic plots...")
    plot_feature_importance(importances)
    plot_actual_vs_predicted(y_test, np.array(y_pred), score, mse=mse, mae=mae)

    print("\nSaving results text file...")
    save_results_txt(importances, score, mse, mae)


if __name__ == "__main__":
    main()
