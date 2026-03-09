"""
model_gb.py
Train a Gradient Boosting model to predict individual income.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt


def load_data():
    """
    Load preprocessed training and test datasets.
    Returns:
        X_train, X_test: Feature matrices
        y_train, y_test: Target vectors (INCTOT)
    """

    # Load X and y separately
    X_train = pd.read_csv("data/processed/X_train.csv")
    X_test = pd.read_csv("data/processed/X_test.csv")

    y_train = pd.read_csv("data/processed/y_train.csv").iloc[:, 0]
    y_test = pd.read_csv("data/processed/y_test.csv").iloc[:, 0]

    print(f"  Train: {len(X_train):,} rows / Test: {len(X_test):,} rows")
    print(f"  Features: {X_train.shape[1]}")

    return X_train, X_test, y_train, y_test


def train_gradient_boosting(X_train, y_train):
    """
    Train a Gradient Boosting Regressor using predefined hyperparameters.
    Args:
        X_train: Training features
        y_train: Training target
    Returns:
        Trained GradientBoostingRegressor model
    """

    # Initialize model with reasonable baseline hyperparameters
    model = GradientBoostingRegressor(
        n_estimators=300,      # Number of boosting stages
        learning_rate=0.05,    # Shrinks contribution of each tree
        max_depth=3,           # Depth of individual regression trees
        random_state=42
    )

    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test):
    """
    Evaluate model performance using R², MSE, and MAE.
    Args:
        model: Trained model
        X_test: Test features
        y_test: True test labels
    Returns:
        r2, mse, mae: Evaluation metrics
    """

    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    mae = mean_absolute_error(y_test, preds)

    # Print evaluation results
    print(f"  Test R² score: {r2:.4f}")
    print(f"  Test MSE: {mse:,.2f}")
    print(f"  Test MAE: {mae:,.2f}")

    return r2, mse, mae


def print_feature_importance(model, feature_names, top_k=20):
    """
    Print top-k most important features based on model.feature_importances_.
    Args:
        model: Trained Gradient Boosting model
        feature_names: List of feature names
        top_k: Number of features to display
    """

    print("\n" + "="*60)
    print("  Gradient Boosting - Top 20 Features")
    print("="*60)

    importances = model.feature_importances_
    idx = np.argsort(importances)[::-1][:top_k]

    # Print ranked feature importance
    for rank, i in enumerate(idx, start=1):
        print(f"{rank:3d}. {feature_names[i]:20s} {importances[i]:.6f}")


def save_results(r2, mse, mae, feature_names, importances, top_k=20, out_path="results_gb.txt"):
    """Save model evaluation metrics and top-k feature importances to a text file."""

    idx = np.argsort(importances)[::-1][:top_k]

    with open(out_path, "w") as f:
        f.write("Gradient Boosting Results\n")
        f.write("=========================\n\n")
        f.write(f"R² score: {r2:.4f}\n")
        f.write(f"MSE: {mse:,.2f}\n")
        f.write(f"MAE: {mae:,.2f}\n\n")

        f.write("Top 20 Feature Importances:\n")
        f.write("---------------------------\n")
        for rank, i in enumerate(idx, start=1):
            f.write(f"{rank:3d}. {feature_names[i]:20s} {importances[i]:.6f}\n")

    print(f"\nResults saved to {out_path}")


def plot_gb_actual_vs_predicted(
    model, X_test, y_test, out_path="reports/figures/gb_actual_vs_predicted.png"
):
    """
    Plot actual vs predicted income values for Gradient Boosting (log scale),
    matching the Random Forest visualization style.
    """
    preds = model.predict(X_test)

    # Clip negative predictions to zero before log transform
    preds = np.where(preds < 0, 0, preds)

    # Log-scale transformation
    actual = np.log1p(y_test)
    predicted = np.log1p(preds)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Scatter plot 
    ax.scatter(actual, predicted, alpha=0.3, s=10, color="steelblue")

    # Perfect prediction line (with legend)
    min_val = min(actual.min(), predicted.min())
    max_val = max(actual.max(), predicted.max())
    ax.plot([min_val, max_val], [min_val, max_val], "r--", label="Perfect fit")

    # Add grid 
    ax.grid(True, linestyle="--", alpha=0.5)

    # Axis labels
    ax.set_xlabel("Actual INCTOT ($k, log scale)")
    ax.set_ylabel("Predicted INCTOT ($k, log scale)")

    # Title with R² 
    r2 = r2_score(y_test, preds)
    ax.set_title(f"Actual vs Predicted (R² = {r2:.3f})")

    # Show legend
    ax.legend()

    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

    print(f"Gradient Boosting plot saved to {out_path}")


def plot_gb_feature_importance(
    model, feature_names, top_k=20,
    out_path="reports/figures/gb_feature_importance.png"
):
    """
    Plot top-k feature importances for Gradient Boosting model.
    Matches the style of en_feature_importance.png.
    """
    importances = model.feature_importances_
    idx = np.argsort(importances)[::-1][:top_k]

    top_features = feature_names[idx]
    top_values = importances[idx]

    plt.figure(figsize=(10, 8))
    plt.barh(top_features, top_values, color="steelblue")
    plt.gca().invert_yaxis()  # Highest importance at top

    plt.xlabel("Feature Importance")
    plt.title("Gradient Boosting — Top 20 Feature Importances")

    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

    print(f"Feature importance plot saved to {out_path}")


def main():
    """Main execution function: load data, train model, evaluate, save results."""

    X_train, X_test, y_train, y_test = load_data()

    model = train_gradient_boosting(X_train, y_train)

    # Get evaluation results
    r2, mse, mae = evaluate(model, X_test, y_test)

    # Print feature importance
    print_feature_importance(model, X_train.columns)

    # Save results to text file
    save_results(
        r2=r2,
        mse=mse,
        mae=mae,
        feature_names=X_train.columns,
        importances=model.feature_importances_,
        out_path="reports/results/results_gb.txt"
    )

    # Save results to png file
    plot_gb_actual_vs_predicted(model, X_test, y_test)

    # Save feature importance plot
    plot_gb_feature_importance(model, X_train.columns)


# Run main() only when executed directly (not when imported)
if __name__ == "__main__":
    main()

