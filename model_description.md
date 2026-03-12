## Model Description

### 1. How the Model Works

This project uses a **Random Forest Regressor** to predict `INCTOT` (total personal income) from 47 demographic, employment, and household features extracted from the IPUMS CPS dataset.

A Random Forest is an ensemble of decision trees. Each tree independently learns a set of splitting rules from a random subset of the training data and a random subset of features. The final prediction is the **average across all trees**, which reduces variance and prevents overfitting compared to a single tree.

#### Decision Tree — Simplified Example

The diagram below illustrates how a single tree might split the data to predict `INCTOT`. At each node, the tree asks a yes/no question about one feature and routes each observation left or right. The predicted income at each leaf is the average `INCTOT` of all training observations that ended up in that node.

```
                        ┌─────────────────────────┐
                        │   RETCONT < threshold?   │   ← Most important split
                        └────────────┬────────────┘
                                     │
              ┌──────────────────────┴──────────────────────┐
             Yes                                            No
              │                                              │
   ┌──────────────────┐                        ┌────────────────────────┐
   │  OCC2010 < 500?  │                        │    AGE < 45?           │
   └────────┬─────────┘                        └──────────┬─────────────┘
            │                                             │
     ┌──────┴──────┐                              ┌───────┴───────┐
    Yes            No                            Yes              No
     │              │                             │                │
┌─────────┐   ┌──────────┐                 ┌──────────┐    ┌──────────────┐
│  EDUC   │   │  EDUC    │                 │Predicted │    │  Predicted   │
│ < 111?  │   │ >= 111?  │                 │ ~$62,000 │    │  ~$105,000   │
└────┬────┘   └────┬─────┘                 └──────────┘    └──────────────┘
     │              │
┌────┴────┐   ┌─────┴────┐
│Predicted│   │Predicted │
│ ~$28,000│   │ ~$75,000 │
└─────────┘   └──────────┘
```

The final `INCTOT` prediction for any individual is the mean of all trees' predictions:

$$\hat{y} = \frac{1}{B} \sum_{b=1}^{B} T_b(\mathbf{x})$$

where:

- $\hat{y}$ — predicted `INCTOT` for a given individual
- $B$ — total number of trees in the forest (= 300 after tuning)
- $T_b(\mathbf{x})$ — prediction from the $b$-th decision tree
- $\mathbf{x}$ — input feature vector (47 variables for one individual)

---

> **Note — Numerical vs. Categorical Variables**
>
> Random Forest treats all input variables as numeric and makes splits using a single threshold: *"Is feature $X$ less than value $t$?"* This works naturally for **numerical variables** like `AGE` or `UHRSWORK1`, where larger values carry inherent order and magnitude.
>
> For **categorical variables** encoded as integers — such as `OCC2010` (occupation codes), `IND` (industry codes), or `REGION` — the model still applies threshold splits (e.g., `OCC2010 < 3000`). This can inadvertently imply an ordering between categories that does not exist in reality. The alternative — One-Hot Encoding each categorical variable — would dramatically increase the number of features and make feature importance scores harder to interpret. Since the primary goal of this project is to identify *which variables* matter (not *which categories* within a variable), integer encoding is retained as a practical trade-off.

---

### 2. Hyperparameter Tuning

Hyperparameters were optimized using **`GridSearchCV`** with **5-fold cross-validation**. The grid search evaluates every combination of the candidate values below, trains and validates each on 5 different folds of the training data, and selects the combination with the highest mean cross-validated $R^2$.

#### Search Space

| Parameter | Candidates | Description |
|-----------|------------|-------------|
| `n_estimators` | 100, 200, 300 | Number of decision trees in the ensemble |
| `max_depth` | 10, 15, 20 | Maximum depth of each tree |

This yields $3 \times 3 = 9$ combinations, each evaluated across 5 folds, for a total of **45 model fits**.

#### Tuning Results

| Metric | Value |
|--------|-------|
| Best `n_estimators` | 300 |
| Best `max_depth` | 10 |
| Best CV $R^2$ (mean of 5 folds) | 0.3471 |
| Test $R^2$ (held-out 20%) | 0.3328 |

The small gap between CV $R^2$ and Test $R^2$ (~0.01) indicates that the model generalizes well and is not overfitting to the training data.

---

### 3. Results

#### Model Comparison — Actual vs. Predicted

| Model | Actual vs. Predicted |
|-------|----------------------|
| **Random Forest** | <!-- INSERT: reports/figures/rf_actual_vs_predicted.png --> |
| **Gradient Boosting** | <!-- INSERT: reports/figures/gb_actual_vs_predicted.png --> |
| **XGBoost** | <!-- INSERT: reports/figures/xgb_actual_vs_predicted.png --> |
| **Lasso Regression** | <!-- INSERT: reports/figures/lasso_actual_vs_predicted.png --> |

---

#### Feature Importances

<!-- INSERT: reports/figures/rf_feature_importance.png -->

Feature importance is measured by **Mean Impurity Decrease (MID)**: for each feature, the model tracks how much each split on that feature reduces the variance of `INCTOT` across all trees, averaged and normalized so all scores sum to 1.0.

| Rank | Variable | Importance | Interpretation |
|------|----------|-----------|----------------|
| 1 | `RETCONT` | ~0.25 | Retirement contributions — strongest single predictor of income |
| 2 | `OCC2010` | ~0.12 | Occupation code — captures wage differences across job types |
| 3 | `AGE` | ~0.07 | Age — income tends to rise through mid-career and plateau |
| 4 | `EDUC` | ~0.06 | Educational attainment — strong positive correlation with earnings |
| 5 | `IND` | ~0.05 | Industry — reflects structural wage differences across sectors |
| 6 | `STATEFIP` | ~0.04 | State — captures cost-of-living and local labor market variation |

The remaining features each contribute less than 4%, suggesting income is largely driven by a small number of employment and human capital factors.

---

#### Actual vs. Predicted (Log Scale)

<!-- INSERT: reports/figures/rf_actual_vs_predicted.png -->

Each point represents one individual in the test set. The x-axis shows their true `INCTOT`; the y-axis shows the model's predicted value. Both axes are on a **log scale** starting at $10^0$ ($1k).

- **Red dashed line** — Perfect prediction line ($\hat{y} = y$). Points on this line are predicted exactly.
- **Points above the line** — Model overpredicts income for these individuals.
- **Points below the line** — Model underpredicts income for these individuals.
- **$R^2 = 0.333$** — The model explains approximately 33% of the variance in `INCTOT`. The remaining 67% reflects factors not captured in the 47 features (e.g., negotiated salary, unreported income, job tenure).

---

#### Evaluation Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| $R^2$ | 0.3328 | Model explains ~33% of income variance |
| MSE | 4,968,256,712 | Mean squared prediction error (in $²) |
| RMSE | $70,486 | Root MSE — typical prediction error magnitude |
| MAE | $31,029 | On average, predictions are off by ~$31k |
