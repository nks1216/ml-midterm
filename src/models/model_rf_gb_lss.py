"""
IPUMS CPS Feature Importance Modeling (Random Forest, Gradient Boosting, Lasso)

Reads preprocessed train/test splits from data/processed/ and runs three
scikit-learn models to identify variables influencing INCTOT.

Prerequisite: run src/data_clean.py first to generate the CSV splits.
"""

import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import (
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import Lasso
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

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


def _extract_importances(model, feature_names):
    """Extract feature importance scores from a fitted model.

    Handles tree-based models (feature_importances_) and linear models
    (absolute coef_). For pipelines, accesses the final estimator.

    Args:
        model: A fitted sklearn model or Pipeline.
        feature_names: List of feature column names.
    Returns:
        Series of importance scores sorted descending.
    """
    estimator = model[-1] if hasattr(model, "__getitem__") else model

    if hasattr(estimator, "feature_importances_"):
        scores = estimator.feature_importances_
    else:
        scores = np.abs(estimator.coef_)

    return (
        pd.Series(scores, index=feature_names)
        .sort_values(ascending=False)
    )


def fit_model(model, X_train, y_train, feature_names):
    """Fit a scikit-learn model and return sorted feature importances.

    Args:
        model: An unfitted sklearn estimator or Pipeline.
        X_train: Training features.
        y_train: Training target.
        feature_names: List of feature column names.
    Returns:
        Series of importance scores sorted descending.
    """
    model.fit(X_train, y_train)
    return _extract_importances(model, feature_names)


def print_top_features(importances, model_name, n=20):
    """Print top N features for a given model.

    Args:
        importances: Series of feature importances.
        model_name: Display name of the model.
        n: Number of top features to show.
    """
    print(f"\n{'=' * 60}")
    print(f"  {model_name} - Top {n} Features")
    print(f"{'=' * 60}")
    for rank, (name, score) in enumerate(importances.head(n).items(), 1):
        print(f"  {rank:>2}. {name:<20s} {score:.6f}")


def build_consensus_ranking(results, n=20):
    """Combine rankings from multiple models into a consensus score.

    Averages each feature's rank across all models (higher = more important).

    Args:
        results: Dict mapping model name to importance Series.
        n: Number of top features to display.
    Returns:
        Series of consensus scores sorted descending.
    """
    rankings = pd.DataFrame({
        name: imp.rank(ascending=True)
        for name, imp in results.items()
    })
    consensus = rankings.mean(axis=1).sort_values(ascending=False)

    print(f"\n{'=' * 60}")
    print(f"  Consensus Ranking - Top {n} Features")
    print(f"{'=' * 60}")
    for rank, (name, score) in enumerate(consensus.head(n).items(), 1):
        print(f"  {rank:>2}. {name:<20s} {score:.1f}")

    return consensus


def main():
    """Run feature importance analysis on preprocessed data."""
    print("Loading preprocessed data...")
    X_train, X_test, y_train, y_test = load_splits(PROCESSED_DIR)
    print(f"  Train: {X_train.shape[0]:,} rows / Test: {X_test.shape[0]:,} rows")
    print(f"  Features: {X_train.shape[1]}")

    feature_names = list(X_train.columns)

    models = {
        "Random Forest": RandomForestRegressor(
            n_estimators=200,
            max_depth=15,
            n_jobs=-1,
            random_state=42,
        ),
        "Gradient Boosting": GradientBoostingRegressor(
            n_estimators=200,
            max_depth=5,
            learning_rate=0.1,
            subsample=0.8,
            random_state=42,
        ),
        "Lasso (|coefficients|)": make_pipeline(
            StandardScaler(),
            Lasso(alpha=100, max_iter=10000, random_state=42),
        ),
    }

    results = {}
    for name, model in models.items():
        print(f"\nTraining {name}...")
        results[name] = fit_model(model, X_train, y_train, feature_names)
        print_top_features(results[name], name)

    build_consensus_ranking(results)


if __name__ == "__main__":
    main()
