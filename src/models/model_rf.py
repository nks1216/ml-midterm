"""
IPUMS CPS Feature Importance Modeling (Random Forest)

Reads preprocessed train/test splits from data/processed/ and runs a
Random Forest model to identify variables influencing INCTOT.
Produces a three-panel diagnostic figure saved to reports/figures/rf_results.png.

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


def plot_results(importances, y_test, y_pred, r2_score, mse=None, mae=None, n=20, save_dir=OUTPUTS_DIR):
    """Generate and save a three-panel diagnostic figure.

    Panel 1 — Feature Importance: top N features ranked by mean impurity decrease.
    Panel 2 — Actual vs Predicted: scatter of true vs predicted INCTOT values.
    Panel 3 — Residual Plot: prediction error across predicted values.

    Args:
        importances: Series of feature importances sorted descending.
        y_test: True target values (test set).
        y_pred: Predicted target values (test set).
        r2_score: Test R² score.
        mse: Mean Squared Error (optional, shown in figure subtitle).
        mae: Mean Absolute Error (optional, shown in figure subtitle).
        n: Number of top features to display in panel 1.
        save_dir: Directory to save the output figure.
    """
    sns.set_theme(style="whitegrid", palette="muted", font_scale=1.0)
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    subtitle = f"R² = {r2_score:.4f}"
    if mse is not None:
        subtitle += f"  |  RMSE = ${mse ** 0.5:,.0f}"
    if mae is not None:
        subtitle += f"  |  MAE = ${mae:,.0f}"
    fig.suptitle(f"Random Forest — INCTOT Diagnostic\n{subtitle}", fontsize=13, fontweight="bold", y=1.02)

    # --- Panel 1: Feature Importance ---
    top = importances.head(n).sort_values()
    sns.barplot(x=top.values, y=top.index, ax=axes[0], color="steelblue")
    axes[0].set_title(f"Top {n} Feature Importances")
    axes[0].set_xlabel("Mean Impurity Decrease")
    axes[0].set_ylabel("")

    # --- Panel 2: Actual vs Predicted (log scale) ---
    # Clip to 1 to avoid log(0); values already filtered >= 1 in data_clean.py
    y_test_k = np.clip(y_test / 1_000, 0.1, None)
    y_pred_k = np.clip(y_pred / 1_000, 0.1, None)
    lim_low = min(y_test_k.min(), y_pred_k.min()) * 0.9
    lim_high = max(y_test_k.max(), y_pred_k.max()) * 1.1
    sns.scatterplot(x=y_test_k, y=y_pred_k, ax=axes[1], alpha=0.15, s=10, color="steelblue")
    axes[1].plot([lim_low, lim_high], [lim_low, lim_high],
                 color="tomato", linewidth=1.2, linestyle="--", label="Perfect fit")
    axes[1].set_xscale("log")
    axes[1].set_yscale("log")
    axes[1].set_xlim(lim_low, lim_high)
    axes[1].set_ylim(lim_low, lim_high)
    axes[1].set_title(f"Actual vs Predicted  (R² = {r2_score:.3f})")
    axes[1].set_xlabel("Actual INCTOT ($k, log scale)")
    axes[1].set_ylabel("Predicted INCTOT ($k, log scale)")
    axes[1].legend(fontsize=9)

    # --- Panel 3: Residuals (log-scale x-axis) ---
    residuals = y_test_k - y_pred_k
    sns.scatterplot(x=y_pred_k, y=residuals, ax=axes[2], alpha=0.15, s=10, color="steelblue")
    axes[2].axhline(0, color="tomato", linewidth=1.2, linestyle="--")
    axes[2].set_xscale("log")
    axes[2].set_title("Residual Plot")
    axes[2].set_xlabel("Predicted INCTOT ($k, log scale)")
    axes[2].set_ylabel("Residual ($k)")

    plt.tight_layout()
    save_dir.mkdir(parents=True, exist_ok=True)
    out_path = save_dir / "rf_results.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\n  Figure saved → {out_path.relative_to(PROJECT_ROOT)}")


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
    plot_results(importances, y_test, np.array(y_pred), score, mse=mse, mae=mae)


if __name__ == "__main__":
    main()
