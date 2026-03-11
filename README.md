# Predicting Personal Income Using Machine Learning Models

## 1. Project Overview

This project uses CPS microdata to predict total personal income and to identify the key socioeconomic factors associated with personal income variation. Understanding the determinants of personal income has important policy implications: accurate prediction supports labor market analysis, informs targeted workforce programs, and sheds light on patterns of inequality and economic mobility at the individual level, making this prediction problem practically relevant for real‑world economic decision‑making.

To address this problem, we build a complete machine learning pipeline that includes data cleaning, feature engineering, model training, and model evaluation. Several models with different inductive biases are implemented—(1) Linear Regression, (2) Elastic Net, (3) Random Forest, and (4) Gradient Boosting—to compare their predictive performance on tabular socioeconomic data. The goal is to identify the most effective modeling approach and provide a clear, reproducible workflow.


## 2. Dataset Description

### 2.1. Data Source

This project uses microdata from the **IPUMS Current Population Survey (CPS)**, maintained by the University of Minnesota. IPUMS CPS provides U.S. Census Bureau's Current Population Survey — a monthly survey of approximately 60,000 households that serves as the primary source for U.S. labor force statistics.

- **Extract ID**: `cps_00001`
- **File format**: Fixed-width ASCII (`.dat`), parsed via DDI XML codebook (`.xml`)
- **Total variables in extract**: 313
- **Selected variables for analysis**: 47 features + 1 target
- **Source**: [IPUMS CPS](https://cps.ipums.org/cps/)

---

### 2.2 Variables

#### Target Variable ($y$)

| Variable | Description | Range |
|----------|-------------|-------|
| `INCTOT` | Total personal income | Filtered to $1 \leq y \leq 9{,}999{,}998$ to exclude NIU and top-coded values |

#### Feature Variables ($X$)

47 features were selected from the 313-variable extract, grouped into 8 categories.

| # | Category | Variable | Description |
|---|----------|----------|-------------|
| 1 | Demographics | `AGE` | Age |
| 2 | | `SEX` | Sex |
| 3 | | `RACE` | Race |
| 4 | | `MARST` | Marital status |
| 5 | | `VETSTAT` | Veteran status |
| 6 | | `RELATE` | Relationship to household head |
| 7 | | `POPSTAT` | Adult civilian, armed forces, or child |
| 8 | | `HISPAN` | Hispanic origin |
| 9 | | `NATIVITY` | Foreign-born or native |
| 10 | | `CITIZEN` | Citizenship status |
| 11 | | `BPL` | Birthplace |
| 12 | Education | `EDUC` | Educational attainment recode |
| 13 | | `SCHLCOLL` | School or college attendance |
| 14 | Family | `FAMSIZE` | Number of family members |
| 15 | | `FAMKIND` | Kind of family unit |
| 16 | Geography | `REGION` | Census region |
| 17 | | `STATEFIP` | State (FIPS code) |
| 18 | | `METRO` | Metropolitan status |
| 19 | | `CBSASZ` | Metro area size |
| 20 | Employment | `EMPSTAT` | Employment status |
| 21 | | `LABFORCE` | Labor force status |
| 22 | | `CLASSWKR` | Class of worker |
| 23 | | `OCC2010` | Occupation (2010 basis) |
| 24 | | `IND` | Industry |
| 25 | | `UHRSWORKT` | Hours usually worked per week (all jobs) |
| 26 | | `UHRSWORK1` | Hours usually worked per week (main job) |
| 27 | | `WKSTAT` | Full/part-time status |
| 28 | | `NUMEMPS` | Number of employers last year |
| 29 | | `FIRMSIZE` | Number of employees at firm |
| 30 | | `PENSION` | Pension plan at work |
| 31 | | `PAIDHOUR` | Paid by the hour |
| 32 | | `UNION` | Union membership |
| 33 | | `SRCEARN` | Source of earnings from longest job |
| 34 | | `RETCONT` | Retirement contributions |
| 35 | Housing | `OWNERSHP` | Ownership of dwelling |
| 36 | | `UNITSSTR` | Units in structure |
| 37 | | `PUBHOUS` | Living in public housing |
| 38 | | `RENTSUB` | Government rent subsidy |
| 39 | Gov. Benefits | `FOODSTMP` | Food stamp recipiency |
| 40 | | `HEATSUB` | Received energy subsidy |
| 41 | Health Insurance | `ANYCOVLY` | Any health insurance coverage last year |
| 42 | | `PHINSUR` | Private health insurance last year |
| 43 | | `GRPCOVLY` | Employment-based group health last year |
| 44 | | `HIMCAIDLY` | Covered by Medicaid last year |
| 45 | | `HIMCARELY` | Covered by Medicare last year |
| 46 | | `PAIDGH` | Employer paid for group health plan |
| 47 | Migration | `MIGRATE1` | Migration status (1 year) |

> **Note**: IPUMS "Not in Universe" (NIU) sentinel values (e.g., 99, 999, 9999, ...) are replaced with `NaN` during preprocessing and imputed using median imputation via `sklearn.impute.SimpleImputer`.

---

### 2.3. Train / Test Split

The dataset is split into training and test sets using `sklearn.model_selection.train_test_split`:

| Parameter | Value |
|-----------|-------|
| Split ratio | 80% train / 20% test |
| `random_state` | 42 |
| Stratification | None (continuous target) |

The split is performed **after** cleaning (NIU replacement and median imputation), and the resulting four files are saved to `data/processed/`:

```
data/processed/
├── X_train.csv
├── X_test.csv
├── y_train.csv
└── y_test.csv
```

### 2.4. Data Limitations

- **Self‑reported income** is subject to measurement error, which may introduce noise into the target variable.

- **Top‑coded high incomes** limit the model’s ability to learn extreme values and reduce variation in the upper tail.

- **Occupation and industry codes** are high‑dimensional and do not capture within‑category heterogeneity (e.g., experience, job role, firm type).

## 3. Modeling Approach and Individual Model Results

### 3.1. Linear Regression

**Model Concept**

Linear Regression serves as the baseline model for interpretability and comparison. It estimates a linear relationship between total personal income (`INCTOT`) and the selected socioeconomic predictors by fitting coefficients that minimize the sum of squared residuals. This provides a simple benchmark against which more flexible nonlinear models can be evaluated.

Formally, the model can be written as:

$$
y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + \varepsilon_i
$$

where:

- $y_i$ is total personal income for individual $i$
- $x_{ij}$ is predictor $j$ for individual $i$
- $\beta_j$ measures the marginal linear contribution of predictor $j$
- $\varepsilon_i$ is the error term

Because the predictors are measured on different scales, we standardized the input features before estimating the model. This allows coefficient magnitudes to be compared across predictors and lets us use the absolute value of the coefficients as a relative feature-importance measure within the Linear Regression specification.

**Why this model matters**

Linear Regression is transparent, easy to interpret, and computationally efficient. However, it assumes additive linear relationships and cannot naturally capture nonlinearities or complex interactions among predictors. For income data, this can lead to underfitting relative to more flexible tree-based models.

### 3.2. Elastic Net (New Model)

This model serves as our required "new technique" not covered in class.

Elastic Net combines L1 and L2 penalties, allowing it to handle correlated predictors more effectively than Lasso or Ridge alone. It provides a more stable coefficient structure and performs feature shrinkage, which is useful for high‑dimensional socioeconomic data.

### 3.3. Random Forest

Each tree independently learns a set of splitting rules from a random subset of the training data and a random subset of features. The final prediction is the **average across all N trees**, which reduces variance and prevents overfitting compared to a single tree.

#### Decision Tree — Simplified Example

At each node, the tree asks a yes/no question about one feature and routes each observation left or right. The predicted income at each leaf is the average `INCTOT` of all training observations that ended up in that node.

```
                        ┌─────────────────────────┐
                        │   RETCONT < threshold?   │ 
                        └────────────┬────────────┘
                                     │
              ┌──────────────────────┴──────────────────────┐
             Yes                                            No
              │                                              │
   ┌──────────────────┐                        ┌────────────────────────┐
   │  OCC2010 < 500?  │                        │       AGE < 45?        │
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

This single tree is repeated N times, each time trained on a different random bootstrap sample of the data and a random subset of features. The final `INCTOT` prediction for any individual is the mean of all trees' predictions:

$$\hat{y} = \frac{1}{B} \sum_{b=1}^{B} T_b(\mathbf{x}), \quad B = N$$  
where:  
- $\hat{y}$ — predicted `INCTOT` for a given individual
- $B$ — total number of trees in the forest (= 300 after tuning)
- $T_b(\mathbf{x})$ — prediction from the $b$-th decision tree
- $\mathbf{x}$ — input feature vector (47 variables for one individual)

#### Search Space

| Parameter | Candidates | Description |
|-----------|------------|-------------|
| `n_estimators` | 100, 200, 300 | Number of decision trees in the ensemble |
| `max_depth` | 10, 15, 20 | Maximum depth of each tree |

#### Tuning Results (w/ GridSearchCV cross validation)

| Metric | Value |
|--------|-------|
| Best `n_estimators` | 300 |
| Best `max_depth` | 10 |
| Best CV $R^2$ (mean of 5 folds) | 0.3471 |
| Test $R^2$ (held-out 20%) | 0.3328 |

---

> **Note — Numerical vs. Categorical Variables**
>
> Random Forest treats all input variables as numeric and makes splits using a single threshold: *"Is feature X less than value t?"* This works naturally for **numerical variables** like `AGE` or `UHRSWORK1`, where larger values carry inherent order and magnitude.
>
> For **categorical variables** encoded as integers — such as `OCC2010` (occupation codes), `IND` (industry codes), or `REGION` — the model still applies threshold splits (e.g., `OCC2010 < 3000`). This can imply an ordering between categories that does not exist in reality. Since the primary goal of this project is to identify *which variables* matter (not *which categories* within a variable), this would suffice. 

---

### 3.4. Gradient Boosting

**Model Concept**

Gradient Boosting builds an ensemble of shallow decision trees sequentially, where each new tree is trained to correct the residual errors of the previous ones. This iterative structure allows the model to capture nonlinear relationships and complex interactions. Unlike Random Forest—which averages many independent trees—Gradient Boosting improves stage‑by‑stage and is more sensitive to hyperparameter choices.

$$
\hat{y}(x) = F_M(x) = F_0(x) + \sum_{m=1}^{M} \nu \cdot h_m(x)
$$

Where:

- $F_0(x)$: initial prediction (typically the mean of the target variable)
- $h_m(x)$: the weak learner (shallow tree) fitted at stage $m$
- $\nu$: learning rate controlling the contribution of each tree
- $M$: number of boosting stages (equivalent to `n_estimators`)

**Model Configuration**

| Hyperparameter | Description                                            |
|----------------| -------------------------------------------------------|
| n_estimators   | Number of boosting stages; controls how many sequential correction steps the model performs.                       |
| learning_rate  | Scales each tree’s contribution to the final prediction, preventing the model from overreacting to residual errors.|
| max_depth      | Maximum depth of each individual tree; keeps trees as weak learners and reduces early overfitting.                 |

**Hyperparameter Tuning (GridSearchCV)**

We first performed hyperparameter tuning using `GridSearchCV` with 3‑fold cross‑validation on the training set (81,864 observations and 47 features). Because income is highly skewed, all predictions were evaluated on a **log‑transformed scale**.

For visualization consistency across models, we applied a **log10(1 + x)** transformation to both actual and predicted income values. This transformation reduces the influence of extreme outliers and produces clearer, more interpretable plots.

*Search Space*

| Hyperparameter | Value Tested              |
|----------------|---------------------------|
| n_estimators   | 100, 200, 300, 400, 500   | 
| learning_rate  | 0.01, 0.03, 0.05, 0.1     |
| max_depth      | 2, 3, 4                   |

**Hyperparameter Tuning (Optuna)**

We then applied `Optuna` to perform a more flexible, continuous search over the hyperparameter space. Unlike `GridSearchCV`, which evaluates a fixed grid, `Optuna` explores the space adaptively and focuses on promising regions. The same **log10(1 + x)** evaluation and visualization strategy was used to ensure comparability across tuning methods.

*Search Space*

| Hyperparameter | Value Tested         |
|----------------|----------------------|
| n_estimators   | 100–500              | 
| learning_rate  | 0.01–0.05 (log scale)|
| max_depth      | 2–4                  |

**Comparison within Gradient Boosting**

|Parameter/Metric |Baseline GB|Grid GB  |Optuna GB|
|-----------------|-----------|---------|---------|
|n_estimators     |300        |200      |475      |
|learning_rate    |0.05       |0.1      |0.0382   |
|max_depth        |3          |4        |4        |
|Test MSE         |4.80B      |4.72B    |4.73B    |
|Test MAE         |30,158     |29,766   |29,747   |
|Test R²          |0.3559     |0.3666   |0.3659   | 
|Computation Time |—          |~10 min  |~14 min  |

Both tuned models (Grid GB and Optuna GB) achieve lower prediction error and higher explanatory power than the baseline model, demonstrating that hyperparameter optimization meaningfully improves Gradient Boosting performance.

When comparing Grid GB and Optuna GB, neither model clearly dominates the other. Their performance differences are small, and the results depend heavily on the chosen hyperparameter search space. Expanding or narrowing the search ranges would likely shift the optimal configuration and the resulting metrics. Ultimately, there is a trade‑off between achieving the best possible performance and minimizing computation time.

**Top 5 Feature Importance within Gradient Boosting**

All Gradient Boosting models identify **RETCONT**, **OCC2010**, **EDUC**, and **SEX** as dominant predictors.

The tuned models (Grid GB and Optuna GB) include **AGE** in the top 5 instead of **UHRSWORKT**. 

**Comparison with Random Forest**

| Metric | Random Forest  | **Gradient Boosting**  |Description  |
|--------|----------------|------------------------|-------------|
| MSE    | 4.98B          | 4.73B                  |lower error  |
| MAE    | 31,322         | 29,747                 |lower error  |
| R²     | 0.3313         | 0.3651                 |higher R²    |

Gradient Boosting (Optuna) achieves lower MSE and MAE and a higher R² than Random Forest, indicating smaller prediction errors and stronger explanatory power.

For simplicity and clarity, only the Optuna‑based training code and final results are included in the repository, while the baseline model and the GridSearchCV setup are documented here as part of the model development process.

**Reduced Feature Analysis**

To evaluate whether a smaller and more interpretable feature set can achieve comparable performance, we constructed a reduced Gradient Boosting model using the 20 features that consistently appeared among the top predictors across Elastic Net, Random Forest, and Gradient Boosting. These variables represent the most stable and influential determinants of income in our dataset and allow us to test the robustness of the Gradient Boosting results while simplifying the feature space.

*Selected Top 20 Features with brief description*

`RETCONT` retirement contributions, `OCC2010` occupation code, `EDUC` education level, `SEX` sex, `AGE` age, `PAIDGH` employer-paid group health, `FIRMSIZE` firm size, `RELATE` relationship to household head, `CBSASZ` metro area size, `MARST` marital status, `UHRSWORKT` usual weekly hours, all jobs, `UHRSWORK1` usual weekly hours, main job, `IND` industry, `FAMSIZE` family size, `PENSION` pension coverage, `EMPSTAT` employment status, `WKSTAT` work status, `HIMCAIDLY` Medicaid coverage, `NUMEMPS` number of employers, 
`CLASSWKR` class of worker.

**Performance Comparison: Full vs. Reduced Gradient Boosting**

| Metrics         | Full GB       | **Reduced GB**   | Description           | 
|-----------------|---------------|------------------|-----------------------|
|                 | (47 features) |**(20 features)** |                       |
| MSE             | 4.73B         | 4,76B            | slightly higher error |
| MAE             | 29,747        | 29,989           | slightly higher error |
| R²              | 0.3651        | 0.3611           | slightly lower R²     |
|Computation Time |~14 min        |~5 min            | much shorter          |

Using only the top 20 consensus features, the reduced Gradient Boosting model performs very similarly to the full 47‑feature specification, though it exhibits slightly higher MSE and MAE and a small decrease in R². These modest differences indicate that while the reduced model sacrifices a small amount of predictive accuracy, a large share of the predictive signal is still concentrated in a relatively small subset of variables. This suggests that the selected features capture the core determinants of income while offering a more compact and interpretable feature space. This also serves as a simple robustness check, showing that the Gradient Boosting model remains stable even when the feature space is substantially reduced.

Considering that the reduced model preserves most of the predictive power while requiring only about one‑third of the computation time, this approach is appealing for applications where efficiency and interpretability matter.

*Optimal Hyperparameters:*
- Full GB: learning_rate = 0.0382, max_depth = 4, n_estimators = 475
- Reduced GB: learning_rate = 0.0431, max_depth = 4, n_estimators = 351

These results also show that the optimal hyperparameters shift when the feature space is reduced, indicating that the model adapts its preferred complexity to the available predictors.


## 4. Comparative Evaluation of Models

#### MSE, MAE, and R² 

| Model             | MSE           | MAE    | R²    | 
|-------------------|---------------|--------|-------|
| Linear Regression | 5,276,020,877 |34,199  |0.2914 |
| Elastic Net       | 5,390,603,768 |33,895  |0.2760 |
| Random Forest     | 4,968,256,712 |31,029  |0.3328 |     
| Gradient Boosting | 4,716,257,047 |29,766  |0.3666 | 

Across the four models, Linear Regression and Elastic Net perform the weakest, showing low R² values and failing to capture the nonlinear structure of income. Although Elastic Net is an extension of Linear Regression with regularization, both remain linear models and therefore struggle to model complex interactions and nonlinear patterns in the data. 

In contrast, Random Forest and Gradient Boosting—both nonlinear tree‑based methods—achieve substantially better predictive performance. Random Forest reduces both MSE and MAE relative to the linear models, while Tuned Gradient Boosting achieves the lowest MAE and the highest R² overall. Its MSE remains higher than that of Random Forest, reflecting greater sensitivity to extreme high‑income outliers, a common characteristic of boosting methods.


#### Top 5 Feature Importances 

| Model | Rank | Feature | Importance | Description |
|-------|------|----------|-------------|-------------|
| **Linear Regression** | 1 | LABFORCE | 29780.72 | Labor force status | 
|                       | 2 | RETCONT | 22199.51 | Retirement contributions |
|                       | 3 | CLASSWKR | 12805.38 | Class of worker |
|                       | 4 | EDUC | 12180.82 | Educational attainment |
|                       | 5 | SEX | 10913.70 | Respondent's sex |
| **Elastic Net**       | 1 | RETCONT | 15792.15 | Retirement contributions |
|                       | 2 | EDUC    | 9165.76  | Educational attainment |
|                       | 3 | OCC2010 | 7074.13  | Occupation (2010 classification) |
|                       | 4 | SEX     | 6974.37  | Respondent's sex |
|                       | 5 | AGE     | 4752.53  | Respondent's age |
| **Random Forest**     | 1 | RETCONT   | 0.3564 | Retirement-related income |
|                       | 2 | OCC2010   | 0.1392 | Occupation (2010 classification) |
|                       | 3 | EDUC      | 0.0686 | Educational attainment |
|                       | 4 | AGE       | 0.0539 | Respondent's age |
|                       | 5 | IND       | 0.0375 | Industry |
| **Gradient Boosting** | 1 | RETCONT   | 0.4377 | Retirement-related income |
|                       | 2 | OCC2010   | 0.1436 | Occupation (2010 classification) |
|                       | 3 | EDUC      | 0.1162 | Educational attainment |
|                       | 4 | SEX       | 0.0340 | Respondent’s sex |
|                       | 5 | AGE       | 0.0332 | Respondent's age |


#### Actual vs Predicted 
| Model | Actual vs. Predicted |
|-------|----------------------|
| **Linear Regression** | ![Linear Regression](reports/figures/lr_actual_vs_predicted.png)<br><sub>This plot compares actual and predicted income on a log scale. Points closer to the 45-degree line indicate more accurate predictions. The spread around the line, especially at higher income levels, suggests that the model captures the overall income trend but struggles to fully fit extreme values and nonlinear relationships.</sub> |
| **Elastic Net** | ![Elastic Net](reports/figures/en_actual_vs_predicted.png) |
| **Random Forest** | <img width="1175" height="1025" alt="rf_actual_vs_predicted" src="https://github.com/user-attachments/assets/461f436e-f277-47a3-b56f-2004d005084e" /> |
| **Gradient Boosting** |![Gradient Boosting](reports/figures/gb_actual_vs_predicted.png)



## 5. Reproducibility

### 5.1. Clone the repository  
```
git clone https://github.com/nks1216/ml-midterm.git
cd ml-midterm
```

### 5.2. Setting up the Virtual Environment

- Create a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install all required packages: `pip install -r requirements.txt`

### 5.3. Download the data 
Via Google Drive (https://drive.google.com/drive/folders/1ly0tgwf_HWVYg3F5HhfzuLXzHCyhsloz?usp=sharing) and save it in the below folders.  
- data/raw/cps_00001.dat
- data/codebook/cps_00001.xml

### 5.4 Run the code
```bash
python3 src/data_clean.py
python3 src/models/model_linear.py
python3 src/models/model_en.py
python3 src/models/model_rf.py
python3 src/models/model_gb.py
python3 src/models/model_gb_top20.py
```
For convenience, individual model scripts are provided.

## 6. Limitations and Future Improvements

**Modeling Limitations**

- **Linear models underfit** because they cannot capture nonlinear interactions among socioeconomic variables.

- **Tree‑based models cannot extrapolate** beyond the range of observed incomes, causing predictions for unusually high values to flatten out.

- **Gradient Boosting is sensitive** to outliers and hyperparameter choices, requiring careful tuning and validation.

- **All models are predictive rather than causal**, meaning the results cannot be interpreted as estimating the causal effect of any feature on income.

## 7. Collaboration and Workflow

- All team members worked through GitHub Issues and feature branches, following a branch‑per‑issue workflow.
- Each member opened pull requests for their work and merged them after review and testing.
- The repository contains more than 30 commits across multiple contributors.
- All code and documentation were merged into the main branch before submission.
