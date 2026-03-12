# Predicting Personal Income Using Machine Learning Models

## 1. Project Overview

This project uses CPS microdata to predict total personal income and to identify the key socioeconomic factors associated with personal income variation. Understanding the determinants of personal income has important policy implications: accurate prediction supports labor market analysis, informs targeted workforce programs, and sheds light on patterns of inequality and economic mobility at the individual level, making this prediction problem practically relevant for real‑world economic decision‑making.

To address this problem, we build a complete machine learning pipeline that includes data cleaning, feature engineering, model training, and model evaluation. Several models with different inductive biases are implemented—(1) Linear Regression, (2) Elastic Net, (3) Random Forest, and (4) Gradient Boosting—to compare their predictive performance on tabular socioeconomic data. We also conduct a brief reduced-feature analysis using the top 20 consensus predictors to examine whether a more compact Gradient Boosting model can retain most of the predictive signal. Finally, we explore ensemble methods such as bagging, boosting, and stacking to further refine prediction accuracy. The goal is to identify the most effective modeling approach and provide a clear, reproducible workflow.


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

**1. Demographics** (11 variables)

| # | Variable | Description | Example Values |
|---|----------|-------------|----------------|
| 1 | `AGE` | Age | 0–90+ (continuous) |
| 2 | `SEX` | Sex | 1 = Male, 2 = Female |
| 3 | `RACE` | Race | 100 = White, 200 = Black, 651 = Asian, ... (29 codes) |
| 4 | `MARST` | Marital status | 1 = Married (spouse present), 3 = Separated, 4 = Divorced, 6 = Never married, ... |
| 5 | `VETSTAT` | Veteran status | 0 = NIU, 1 = No service, 2 = Yes |
| 6 | `RELATE` | Relationship to household head | 0101 = Head, 0201 = Spouse, 0301 = Child, ... (20 codes) |
| 7 | `POPSTAT` | Adult civilian, armed forces, or child | 1 = Adult civilian, 2 = Armed Forces, 3 = Child |
| 8 | `HISPAN` | Hispanic origin | 000 = Not Hispanic, 100 = Mexican, 200 = Puerto Rican, ... (17 codes) |
| 9 | `NATIVITY` | Foreign-born or native | 1 = Both parents native, 4 = Both parents foreign, 5 = Foreign born, ... |
| 10 | `CITIZEN` | Citizenship status | 1 = Born in U.S., 4 = Naturalized, 5 = Not a citizen, ... |
| 11 | `BPL` | Birthplace | FIPS state codes for U.S.; country codes for foreign-born (173 codes) |

**2. Education** (2 variables)

| # | Variable | Description | Example Values |
|---|----------|-------------|----------------|
| 12 | `EDUC` | Educational attainment recode | 073 = HS diploma, 111 = Bachelor's, 123 = Master's, 125 = Doctorate, ... (36 codes) |
| 13 | `SCHLCOLL` | School or college attendance | 0 = NIU, 3 = College full-time, 5 = Does not attend, ... |

**3. Family** (2 variables)

| # | Variable | Description | Example Values |
|---|----------|-------------|----------------|
| 14 | `FAMSIZE` | Number of family members | 1, 2, 3, ... 29+ (continuous) |
| 15 | `FAMKIND` | Kind of family unit | 1 = Husband/wife, 2 = Male ref. person, 3 = Female ref. person |

**4. Geography** (4 variables)

| # | Variable | Description | Example Values |
|---|----------|-------------|----------------|
| 16 | `REGION` | Census region | 11 = New England, 12 = Mid Atlantic, 31 = South Atlantic, 42 = Pacific, ... (10 codes) |
| 17 | `STATEFIP` | State (FIPS code) | 01 = Alabama, 06 = California, 36 = New York, 48 = Texas, ... (75 codes) |
| 18 | `METRO` | Metropolitan status | 1 = Not in metro, 2 = In central city, 3 = Not in central city, ... |
| 19 | `CBSASZ` | Metro area size | 00 = Non-metro, 01 = 100k–250k, 04 = 1M–2.5M, 06 = 5M+, ... |

**5. Employment** (15 variables)

| # | Variable | Description | Example Values |
|---|----------|-------------|----------------|
| 20 | `EMPSTAT` | Employment status | 10 = At work, 20 = Unemployed, 30 = Not in labor force, ... (14 codes) |
| 21 | `LABFORCE` | Labor force status | 0 = NIU, 1 = Not in LF, 2 = In labor force |
| 22 | `CLASSWKR` | Class of worker | 22 = Private for-profit, 25 = Federal govt, 27 = State govt, ... (15 codes) |
| 23 | `OCC2010` | Occupation (2010 basis) | 0010 = Chief executives, 2100 = Lawyers, 4720 = Cashiers, ... (479 codes) |
| 24 | `IND` | Industry | Continuous industry codes |
| 25 | `UHRSWORKT` | Hours usually worked per week (all jobs) | 1–99 (continuous); 997 = Varies |
| 26 | `UHRSWORK1` | Hours usually worked per week (main job) | 0–99 (continuous); 997 = Varies |
| 27 | `WKSTAT` | Full/part-time status | 10 = Full-time, 20 = Part-time (economic), 40 = Part-time (non-economic), ... (15 codes) |
| 28 | `NUMEMPS` | Number of employers last year | Continuous |
| 29 | `FIRMSIZE` | Number of employees at firm | 1 = Under 10, 2 = 10–24, 7 = 100–499, 8 = 500–999, ... (10 codes) |
| 30 | `PENSION` | Pension plan at work | 0 = NIU, 1 = No plan, 2 = Plan but not included, 3 = Included |
| 31 | `PAIDHOUR` | Paid by the hour | 0 = NIU, 1 = No, 2 = Yes |
| 32 | `UNION` | Union membership | 0 = NIU, 1 = No coverage, 2 = Union member, 3 = Covered but not member |
| 33 | `SRCEARN` | Source of earnings from longest job | 0 = NIU, 1 = Wage/salary, 2 = Self-employed, 3 = Farm self-employed |
| 34 | `RETCONT` | Retirement contributions | Continuous (dollar amount) |

**6. Housing** (4 variables)

| # | Variable | Description | Example Values |
|---|----------|-------------|----------------|
| 35 | `OWNERSHP` | Ownership of dwelling | 10 = Owned, 21 = No cash rent, 22 = With cash rent |
| 36 | `UNITSSTR` | Units in structure | 01 = Mobile home, 11 = One unit, 12 = 10+ units, ... (7 codes) |
| 37 | `PUBHOUS` | Living in public housing | 0 = NIU, 1 = No, 2 = Yes |
| 38 | `RENTSUB` | Government rent subsidy | 0 = NIU, 1 = No, 2 = Yes |

**7. Government Benefits** (2 variables)

| # | Variable | Description | Example Values |
|---|----------|-------------|----------------|
| 39 | `FOODSTMP` | Food stamp recipiency | 0 = NIU, 1 = No, 2 = Yes |
| 40 | `HEATSUB` | Received energy subsidy | 0 = NIU, 1 = No, 2 = Yes |

**8. Health Insurance** (6 variables)

| # | Variable | Description | Example Values |
|---|----------|-------------|----------------|
| 41 | `ANYCOVLY` | Any health insurance coverage last year | 01 = No, 02 = Yes |
| 42 | `PHINSUR` | Private health insurance last year | 0 = NIU, 1 = No, 2 = Yes |
| 43 | `GRPCOVLY` | Employment-based group health last year | 0 = NIU, 1 = No, 2 = Yes |
| 44 | `HIMCAIDLY` | Covered by Medicaid last year | 1 = No, 2 = Yes |
| 45 | `HIMCARELY` | Covered by Medicare last year | 0 = NIU, 1 = No, 2 = Yes |
| 46 | `PAIDGH` | Employer paid for group health plan | 00 = NIU, 10 = No, 21 = Paid part, 22 = Paid all |

**9. Migration** (1 variable)

| # | Variable | Description | Example Values |
|---|----------|-------------|----------------|
| 47 | `MIGRATE1` | Migration status (1 year) | 1 = Same house, 3 = Within county, 5 = Between states, 6 = Abroad, ... |

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

- The dataset **does not include wealth, assets, or detailed job characteristics**, all of which are important determinants of income but unavailable in CPS microdata.


## 3. Modeling Approach and Individual Model Results

### 3.1. Linear Regression

Baseline model for interpretability and comparison.

### 3.2. Elastic Net (New Model)

This model serves as our required "new technique" not covered in class.

Elastic Net combines L1 and L2 penalties, allowing it to handle correlated predictors more effectively than Lasso or Ridge alone. It provides a more stable coefficient structure and performs feature shrinkage, which is useful for high‑dimensional socioeconomic data.

### 3.3. Random Forest

Each tree independently learns a set of splitting rules from a random subset of the training data and a random subset of features. The final prediction is the **average across all 200 trees**, which reduces variance and prevents overfitting compared to a single tree.

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

This single tree is repeated **200 times**, each time trained on a different random bootstrap sample of the data and a random subset of features. The final `INCTOT` prediction for any individual is the mean of all 200 trees' predictions:

$$\hat{y} = \frac{1}{B} \sum_{b=1}^{B} T_b(\mathbf{x}), \quad B = 200$$

#### Model Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| `n_estimators` | 200 | Number of decision trees |
| `max_depth` | 15 | Maximum depth of each tree |

---

> **Note — Numerical vs. Categorical Variables**
>
> Random Forest treats all input variables as numeric and makes splits using a single threshold: *"Is feature $X$ less than value $t$?"* This works naturally for **numerical variables** like `AGE` or `UHRSWORK1`, where larger values carry inherent order and magnitude.
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

To improve model performance, we performed hyperparameter tuning using `GridSearchCV` with 3‑fold cross‑validation on the training set (81,864 observations and 47 features). Because income is highly skewed, predictions were evaluated on a **log‑transformed** scale to reduce the influence of extreme outliers.

*Search Space*

| Hyperparameter | Value Tested              |
|----------------|---------------------------|
| n_estimators   | 100, 200, 300, 400, 500   | 
| learning_rate  | 0.01, 0.03, 0.05, 0.1     |
| max_depth      | 2, 3, 4                   |

*Optimal Hyperparameter*

| Hyperparameter | Best Value   |
|----------------|--------------|
| n_estimators   | 200          |
| learning_rate  | 0.1          |
| max_depth      | 4            |

These values balance model complexity and generalization by allowing deeper interactions while maintaining stable learning dynamics.

**Model Performance**

Using the tuned hyperparameters, the model achieved:

- Test MSE: 4.72B
- Test MAE: 29,766
- Test R²: 0.3666

**Comparison with Baseline Gradient Boosting**

|Parameter/Metric|Baseline GB|**Tuned GB**|Description               |
|----------------|-----------|------------|--------------------------|
|n_estimators    |300        |200         |fewer but sufficient trees|
|learning_rate   |0.05       |0.1         |faster learning           |
|max_depth       |3          |4           |deeper interactions       |
|Test MSE        |4.80B      |4.72B       |lower error               |
|Test MAE        |30,158     |29,766      |lower error               |
|Test R²         |0.3559     |0.3666      |higher R²                 | 

Top 5 Feature Importance (Baseline GB vs. Tuned GB)

- Both models identify **RETCONT**, **OCC2010**, **EDUC**, and **SEX** as dominant predictors.

- The tuned model places **AGE** in the top 5 instead of **UHRSWORKT**, reflecting deeper interactions captured by the increased tree depth (`max_depth=4`).

The tuned model provides higher explanatory power and lower average error, indicating that hyperparameter optimization meaningfully improves predictive performance. 

Baseline Gradient Boosting results are included for comparison, but the final model used in this project is the tuned version described above.

**Comparison with Random Forest**

| Metric | Random Forest  | **Tuned GB**  |Description  |
|--------|----------------|---------------|-------------|
| MSE    | 3.25B          | 4.72B         |higher error |
| MAE    | 32,400         | 29,766        |lower error  |
| R²     | 0.3310         | 0.3666        |higher R²    |

Gradient Boosting exhibits a higher MSE than Random Forest, indicating that it makes larger errors on a small number of very high‑income observations. However, it achieves a lower MAE, meaning that its typical prediction errors are smaller. In addition, Gradient Boosting attains a higher R², suggesting that it explains more of the overall variation in income. This pattern reflects a common trade‑off in boosting models: they reduce average errors and improve explanatory power but remain sensitive to extreme outliers due to their sequential learning structure.

## 4. Comparative Evaluation of Models

#### MSE, MAE, and R² 

| Model             | MSE           | MAE    | R²    | 
|-------------------|---------------|--------|-------|
| Linear Regression | 5,276,020,877 |34,199  |0.2914 |
| Elastic Net       | 5,390,603,768 |33,895  |0.2760 |
| Random Forest     | 3,245,000,000 |32,400  |0.3310 |     
| Gradient Boosting | 4,716,257,047 |29,766  |0.3666 | 

Across the four models, Linear Regression and Elastic Net perform the weakest, showing low R² values and failing to capture the nonlinear structure of income. Although Elastic Net is an extension of Linear Regression with regularization, both remain linear models and therefore struggle to model complex interactions and nonlinear patterns in the data. 

In contrast, Random Forest and Gradient Boosting—both nonlinear tree‑based methods—achieve substantially better predictive performance. Random Forest reduces both MSE and MAE relative to the linear models, while Tuned Gradient Boosting achieves the lowest MAE and the highest R² overall. Its MSE remains higher than that of Random Forest, reflecting greater sensitivity to extreme high‑income outliers, a common characteristic of boosting methods.


#### Top 5 Feature Importances 

| Model | Rank | Feature | Importance | Description |
|-------|------|----------|-------------|-------------|
| **Linear Regression** | 1 | N/A | N/A | Raw coefficients are not directly comparable without standardization | 
|                       | 2 | N/A | N/A | N/A |
|                       | 3 | N/A | N/A | N/A |
|                       | 4 | N/A | N/A | N/A |
|                       | 5 | N/A | N/A | N/A |
| **Elastic Net**       | 1 | RETCONT | 15792.15 | Retirement contributions |
|                       | 2 | EDUC    | 9165.76  | Educational attainment |
|                       | 3 | OCC2010 | 7074.13  | Occupation (2010 classification) |
|                       | 4 | SEX     | 6974.37  | Respondent's sex |
|                       | 5 | AGE     | 4752.53  | Respondent's age |
| **Random Forest**     | 1 | RETCONT   | 0.2553 | Retirement-related income |
|                       | 2 | OCC2010   | 0.1168 | Occupation (2010 classification) |
|                       | 3 | AGE       | 0.0695 | Respondent’s age |
|                       | 4 | EDUC      | 0.0568 | Educational attainment |
|                       | 5 | IND       | 0.0493 | Industry |
| **Gradient Boosting** | 1 | RETCONT   | 0.4377 | Retirement-related income |
|                       | 2 | OCC2010   | 0.1436 | Occupation (2010 classification) |
|                       | 3 | EDUC      | 0.1162 | Educational attainment |
|                       | 4 | SEX       | 0.0340 | Respondent’s sex |
|                       | 5 | AGE       | 0.0332 | Respondent's age |


#### Actual vs Predicted 
| Model | Actual vs. Predicted |
|-------|----------------------|
| **Linear Regression** | ![Linear Regression](reports/figures/lr_actual_vs_predicted.png) |
| **Elastic Net** | ![Elastic Net](reports/figures/en_actual_vs_predicted.png) |
| **Random Forest** | <img width="437" height="412" alt="image" src="https://github.com/user-attachments/assets/5b972691-2066-462a-802d-3bf358cc24c0" /> |
| **Gradient Boosting** |![Gradient Boosting](reports/figures/gb_actual_vs_predicted.png)


## 5. Reduced Feature Analysis (Gradient Boosting)

Because Gradient Boosting emerged as the best-performing model in the full-feature comparison, we focus our reduced-specification analysis on this model to assess whether a more compact and interpretable feature set can preserve most of its predictive power.

**Feature Selection Rationale**

To evaluate whether a smaller and more interpretable feature set can achieve comparable performance, we constructed a reduced Gradient Boosting model using the 20 features that consistently appeared among the top predictors across Elastic Net, Random Forest, and Gradient Boosting. These variables represent the most stable and influential determinants of income in our dataset and allow us to test the robustness of the Gradient Boosting results while simplifying the feature space.

**Selected Top 20 Features:**

RETCONT, OCC2010, EDUC, SEX, AGE, PAIDGH, FIRMSIZE, RELATE, CBSASZ, MARST, UHRSWORKT, UHRSWORK1, IND, FAMSIZE, PENSION, EMPSTAT, WKSTAT, HIMCAIDLY, NUMEMPS, CLASSWKR.

**Performance Comparison: Full vs. Reduced Gradient Boosting**

| Metrics | Full GB       | **Reduced GB**   | Description                     | 
|---------|---------------|------------------|---------------------------------|
|         | (47 features) |**(20 features)** |                                 |
| MSE     | 4,716,257,047 | 4,741,541,933    | slightly higher error           |
| MAE     | 29,766        | 29,904           | slightly higher error           |
| R²      | 0.3666        | 0.3632           | slightly lower explanatory power|

Using only the top 20 consensus features, the reduced Gradient Boosting model performs very similarly to the full 47‑feature specification, though it exhibits slightly higher MSE and MAE and a small decrease in R². These modest differences indicate that while the reduced model sacrifices a small amount of predictive accuracy, a large share of the predictive signal is still concentrated in a relatively small subset of variables. This suggests that the selected features capture the core determinants of income while offering a more compact and interpretable feature space. This also serves as a simple robustness check, showing that the Gradient Boosting model remains stable even when the feature space is substantially reduced.

To illustrate this further, the optimal hyperparameters for each specification are shown below:

*Optimal Hyperparameters:*
- Full GB: learning_rate = 0.1, max_depth = 4, n_estimators = 200 
- Reduced GB: learning_rate = 0.1, max_depth = 3, n_estimators = 400

Interestingly, the optimal hyperparameters also shift when the feature space is reduced, indicating that the model adapts its preferred complexity to the available predictors. This further reinforces the robustness of the Gradient Boosting approach, as performance remains stable despite changes in both dimensionality and tuning configuration.

**Brief Description of Selected Features:**  
RETCONT (retirement contributions), OCC2010 (occupation code), EDUC (education level), SEX (sex), AGE (age), PAIDGH (employer-paid group health), FIRMSIZE (firm size), RELATE (relationship to household head), CBSASZ (metro area size), MARST (marital status), UHRSWORKT (usual weekly hours, all jobs), UHRSWORK1 (usual weekly hours, main job), IND (industry), FAMSIZE (family size), PENSION (pension coverage), EMPSTAT (employment status), WKSTAT (work status), HIMCAIDLY (Medicaid coverage), NUMEMPS (number of employers), 
CLASSWKR (class of worker).


## 6. Ensemble Extensions (Bagging, Boosting, Stacking)
If time permits, apply ensemble techniques to refine predictions and compare their performance against individual models.


## 7. Reproducibility

### 7.1. Setting up the Virtual Environment

- Create a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install all required packages: `pip install -r requirements.txt`

### 7.2. Clone the repository  
```
git clone <repo-url>
cd ml-midterm
pip install -r requirements.txt
```

### 7.3. Download the data 
Via Google Drive (https://drive.google.com/drive/folders/1ly0tgwf_HWVYg3F5HhfzuLXzHCyhsloz?usp=sharing) and save it in the below folders.  
- data/raw/cps_00001.dat
- data/codebook/cps_00001.xml

### 7.4 Run the code
```bash
python3 src/data_clean.py
python3 src/models/model_linear.py
python3 src/models/model_en.py
python3 src/models/model_rf.py
python3 src/models/model_gb.py
python3 src/models/model_gb_top20.py
```
For convenience, individual model scripts are provided.

## 8. Limitations and Future Improvements

**Modeling Limitations**

- **Linear models underfit** because they cannot capture nonlinear interactions among socioeconomic variables.

- **Tree‑based models cannot extrapolate** beyond the range of observed incomes, causing predictions for unusually high values to flatten out.

- **Gradient Boosting is sensitive** to outliers and hyperparameter choices, requiring careful tuning and validation.

- **All models are predictive rather than causal**, meaning the results cannot be interpreted as estimating the causal effect of any feature on income.

## 9. Collaboration and Workflow

- All team members worked through GitHub Issues and feature branches, following a branch‑per‑issue workflow.
- Each member opened pull requests for their work and merged them after review and testing.
- The repository contains more than 30 commits across multiple contributors.
- All code and documentation were merged into the main branch before submission.