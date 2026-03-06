"""
IPUMS CPS Feature Importance Modeling (Random Forest)

Reads preprocessed train/test splits from data/processed/ and runs a
Random Forest model to identify variables influencing INCTOT.

Prerequisite: run src/data_clean.py first to generate the CSV splits.
"""

import warnings
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

warnings.filterwarnings("ignore")

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


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


def main():
    """Run Random Forest feature importance analysis."""
    print("Loading preprocessed data...")
    X_train, X_test, y_train, y_test = load_splits(PROCESSED_DIR)
    print(f"  Train: {X_train.shape[0]:,} rows / Test: {X_test.shape[0]:,} rows")
    print(f"  Features: {X_train.shape[1]}")

    feature_names = list(X_train.columns)

    print("\nTraining Random Forest...")
    model, importances = fit_random_forest(X_train, y_train, feature_names)

    score = model.score(X_test, y_test)
    print(f"  Test R² score: {score:.4f}")

    print_top_features(importances)


if __name__ == "__main__":
    main()
