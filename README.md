# Predicting Individual Income Using Machine Learning Models

## 1. Project Overview

This project uses CPS microdata to predict total individual income and to identify the key socioeconomic factors associated with income variation. Understanding the determinants of household income has important policy implications: accurate income prediction can support targeted social programs, inform tax and welfare design, and shed light on patterns of inequality and economic mobility.

To address this problem, we build a complete machine learning pipeline that includes data cleaning, feature engineering, model training, and model evaluation. Several models with different inductive biases are implemented—(1) Linear Regression, (2) Elastic Net, (3) Random Forest, and (4) Gradient Boosting—to compare their predictive performance on tabular socioeconomic data. We also explore ensemble methods such as bagging, boosting, and stacking to further refine prediction accuracy. The goal is to identify 
the most effective modeling approach and provide a clear, reproducible workflow.

## 2. Dataset Description

### 1. Data Source

This project uses microdata from the **IPUMS Current Population Survey (CPS)**, maintained by the University of Minnesota. IPUMS CPS provides harmonized extracts of the U.S. Census Bureau's Current Population Survey — a monthly survey of approximately 60,000 households that serves as the primary source for U.S. labor force statistics.

- **Extract ID**: `cps_00001`
- **File format**: Fixed-width ASCII (`.dat`), parsed via DDI XML codebook (`.xml`)
- **Total variables in extract**: 313
- **Selected variables for analysis**: 43 features + 1 target
- **Source**: [IPUMS CPS](https://cps.ipums.org/cps/)

---

### 2. Variables

#### Target Variable ($y$)

| Variable | Description | Range |
|----------|-------------|-------|
| `INCTOT` | Total personal income | Filtered to $1 \leq y \leq 9{,}999{,}998$ to exclude NIU and top-coded values |

#### Feature Variables ($X$)

43 features were selected from the 313-variable extract, grouped into 8 thematic categories.

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

### 3. Train / Test Split

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

## 3.1. Linear Regression
Baseline model for interpretability and comparison.

## 3.2. Elastic Net (New Model)
Regularized linear model combining L1 and L2 penalties to improve stability and handle correlated predictors.

## 3.3. Random Forest
Bagging-based tree ensemble capturing nonlinear relationships.

## 3.4. Gradient Boosting
Boosting-based model that sequentially corrects prediction errors.

## 4. Results and Model Comparison

## 4.1. Comparison basic model
Evaluate all individual models using RMSE, MAE, and R².

## 4.2. Ensemble Methods (Bagging, Boosting, Stacking)
If time permits, apply ensemble techniques to refine predictions and compare their performance against individual models.

## 5. Repository Structure

## 6. Reproducibility
6.1. Setting up the Virtual Environment

- Create a virtual environment:
`python3 -m venv venv`

- Activate the virtual environment:
`source venv/bin/activate`

- Install all required packages:
`pip install -r requirements.txt`

6.2. Clone the repository  
```
git clone <repo-url>
cd ml-midterm
pip install -r requirements.txt
```
6.3. Download the data 
Via Google Drive(https://drive.google.com/drive/folders/1ly0tgwf_HWVYg3F5HhfzuLXzHCyhsloz?usp=sharing) and save it in the below folders.  
- data/raw/cps_00001.dat
- data/codebook/cps_00001.xml
  
6.4. Run the code  
```
python src/data_clean.py          # Step 1: data cleaning
python src/models/model_rf_gb_lss.py  # Step 2: running models
```
## 7. Future Improvements
