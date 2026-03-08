# Predicting Individual Income Using Machine Learning Models

## 1. Project Overview

This project uses CPS microdata to predict total individual income and to identify the key socioeconomic factors associated with income variation. Understanding the determinants of household income has important policy implications: accurate income prediction can support targeted social programs, inform tax and welfare design, and shed light on patterns of inequality and economic mobility.

To address this problem, we build a complete machine learning pipeline that includes data cleaning, feature engineering, model training, and model evaluation. Several models with different inductive biases are implemented—(1) Linear Regression, (2) Elastic Net, (3) Random Forest, and (4) Gradient Boosting—to compare their predictive performance on tabular socioeconomic data. We also explore ensemble methods such as bagging, boosting, and stacking to further refine prediction accuracy. The goal is to identify 
the most effective modeling approach and provide a clear, reproducible workflow.

## 2. Dataset Description

### 2.1. Data Source

This project uses microdata from the **IPUMS Current Population Survey (CPS)**, maintained by the University of Minnesota. IPUMS CPS provides U.S. Census Bureau's Current Population Survey — a monthly survey of approximately 60,000 households that serves as the primary source for U.S. labor force statistics.

- **Extract ID**: `cps_00001`
- **File format**: Fixed-width ASCII (`.dat`), parsed via DDI XML codebook (`.xml`)
- **Total variables in extract**: 313
- **Selected variables for analysis**: 43 features + 1 target
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


## 3. Modeling Approach

### 3.1. Linear Regression
Baseline model for interpretability and comparison.

### 3.2. Elastic Net (New Model)
Regularized linear model combining L1 and L2 penalties to improve stability and handle correlated predictors.

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
Boosting-based model that sequentially corrects prediction errors.

## 4. Results and Model Comparison

#### MSE, MAE, and R² 

| Model             | MSE           | MAE    | R²    | 
|-------------------|---------------|--------|-------|
| Linear Regression | 72,636        |34,199  |0.2914 |
| Elastic Net       | 5,390,603,768 |33,895  |0.2760 |
| Random Forest     | 3,245,000,000 |32,400  |0.3310 |     
| Gradient Boosting | 4,795,937,263 |30,158  |0.3559 | 

#### Top 5 Feature Importances 

| Model | Rank | Feature | Importance | Description |
|-------|------|----------|-------------|-------------|
| **Linear Regression** | 1 |  |  |  |
|                       | 2 |  |  |  |
|                       | 3 |  |  |  |
|                       | 4 |  |  |  |
|                       | 5 |  |  |  |
| **Elastic Net**       | 1 | RETCONT | 15792.15 | Retirement contributions |
|                       | 2 | EDUC    | 9165.76  | Educational attainment |
|                       | 3 | OCC2010 | 7074.13  | Occupation (2010 classification) |
|                       | 4 | SEX     | 6974.37  | Respondent's sex |
|                       | 5 | AGE     | 4752.53  | Respondent's age |
| **Random Forest**     | 1 | RETCONT   | 0.2553 | Retirement-related income |
|                       | 2 | OCC2010   | 0.1168 | Occupation code (2010 classification) |
|                       | 3 | AGE       | 0.0695 | Respondent’s age |
|                       | 4 | EDUC      | 0.0568 | Educational attainment |
|                       | 5 | IND       | 0.0493 | Industry |
| **Gradient Boosting** | 1 | RETCONT   | 0.4620 | Retirement-related income |
|                       | 2 | OCC2010   | 0.1456 | Occupation code (2010 classification) |
|                       | 3 | EDUC      | 0.1340 | Educational attainment |
|                       | 4 | SEX       | 0.0396 | Respondent’s sex |
|                       | 5 | UHRSWORKT | 0.0283 | Hours usually worked per week |


#### Actual vs Predicted 
| Model | Actual vs. Predicted |
|-------|----------------------|
| **Linear Regression** | <!-- INSERT: reports/figures/rf_results.png (Panel 2) --> |
| **Elastic Net** | <!-- INSERT: reports/figures/gb_results.png (Panel 2) --> |
| **Random Forest** | <img width="437" height="412" alt="image" src="https://github.com/user-attachments/assets/5b972691-2066-462a-802d-3bf358cc24c0" /> |
| **Gradient Boosting** |![Gradient Boosting](reports/figures/gb_actual_vs_predicted.png)
 |



#### Ensemble Methods (Bagging, Boosting, Stacking)
If time permits, apply ensemble techniques to refine predictions and compare their performance against individual models.

## 5. Repository Structure

## 6. Reproducibility
### 6.1. Setting up the Virtual Environment
- Create a virtual environment:
`python3 -m venv venv`

- Activate the virtual environment:
`source venv/bin/activate`

- Install all required packages:
`pip install -r requirements.txt`
### 6.2. Clone the repository  
```
git clone <repo-url>
cd ml-midterm
pip install -r requirements.txt
```
### 6.3. Download the data 
Via Google Drive(https://drive.google.com/drive/folders/1ly0tgwf_HWVYg3F5HhfzuLXzHCyhsloz?usp=sharing) and save it in the below folders.  
- data/raw/cps_00001.dat
- data/codebook/cps_00001.xml
### 4. Run the code  
python src/data_clean.py
python src/models/model_lr.py
python src/models/model_en.py
python src/models/model_rf.py
python src/models/model_gb.py
## 7. Future Improvements
