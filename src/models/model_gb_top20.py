"""
model_gb_top20.py
Train a Gradient Boosting model to predict individual income (Top 20 features only).
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt


def load_data():
    """
    Load preprocessed training and test datasets.
    Returns:
        X_train, X_test: Feature matrices (Top 20 features only)
        y_train, y_test: Target vectors (INCTOT)
    """

    # Load full feature matrices
    X_train = pd.read_csv("data/processed/X_train.csv")
    X_test = pd.read_csv("data/processed/X_test.csv")

    y_train = pd.read_csv("data/processed/y_train.csv").iloc[:, 0]
    y_test = pd.read_csv("data/processed/y_test.csv").iloc[:, 0]

    # === Top 20 features selected across EN, RF, GB ===
    top_20_features = [
        "RETCONT", "OCC2010", "EDUC", "SEX", "AGE",
        "PAIDGH", "FIRMSIZE", "RELATE", "CBSASZ", "MARST",
        "UHRSWORKT", "UHRSWORK1", "IND", "FAMSIZE",
        "PENSION", "EMPSTAT", "WKSTAT", "HIMCAIDLY",
        "NUMEMPS", "CLASSWKR"
    ]

    # Filter to top 20 features only
    X_train = X_train[top_20_features]
    X_test = X_test[top_20_features]

    print(f"  Train: {len(X_train):,} rows / Test: {len(X_test):,} rows")
    print(f"  Features used: {len(top_20_features)} (Top 20 selected)")

    return X_train, X_test, y_train, y_test


from sklearn.model_selection import GridSearchCV

def train_gradient_boosting(X_train, y_train):
    """
    Train Gradient Boosting with hyperparameter tuning using GridSearchCV.
    Returns:
        Best estimator found by grid search
    """

    # Base model
    gbr = GradientBoostingRegressor(random_state=42)

    # Hyperparameter search space
    param_grid = {
        'n_estimators': [100, 200, 300, 400, 500],
        'learning_rate': [0.01, 0.03, 0.05, 0.1],
        'max_depth': [2, 3, 4]
    }

    # Grid search
    grid_search = GridSearchCV(
        estimator=gbr,
        param_grid=param_grid,
        cv=3,
        scoring='r2',
        n_jobs=-1,
        verbose=2
    )

    # Fit grid search
    grid_search.fit(X_train, y_train)

    print("\nBest parameters found:", grid_search.best_params_)
    print("Best CV R²:", grid_search.best_score_)

    # Return best model
    return grid_search.best_estimator_



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


def save_results(r2, mse, mae, feature_names, importances, top_k=20, out_path="results_gb_top20.txt"):
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
    model, X_test, y_test, out_path="reports/figures/gb_actual_vs_predicted_top20.png"
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
    out_path="reports/figures/gb_feature_importance_top20.png"
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

    # Save results to text file (TOP 20 version)
    save_results(
        r2=r2,
        mse=mse,
        mae=mae,
        feature_names=X_train.columns,
        importances=model.feature_importances_,
        out_path="reports/results/results_gb_top20.txt"
    )

    # Save actual vs predicted plot (TOP 20 version)
    plot_gb_actual_vs_predicted(
        model, X_test, y_test,
        out_path="reports/figures/gb_actual_vs_predicted_top20.png"
    )

    # Save feature importance plot (TOP 20 version)
    plot_gb_feature_importance(
        model, X_train.columns,
        out_path="reports/figures/gb_feature_importance_top20.png"
    )


# Run main() only when executed directly (not when imported)
if __name__ == "__main__":
    main()

