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


## 3. Modeling Approach and Individual Model Results

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

**Model Concept**

Gradient Boosting is an ensemble learning method that builds a sequence of weak learners—typically shallow decision trees—where each new tree is trained to correct the residual errors of the previous ones. By iteratively minimizing the loss function, the model captures nonlinear relationships and complex interactions between features. Unlike Random Forest, which averages many independent trees, Gradient Boosting improves sequentially and often achieves higher predictive accuracy, though it is more sensitive to hyperparameter choices.

**Hyperparameter Concepts**

- Number of boosting stages (n_estimators):  
    Controls how many sequential correction steps the model performs.

- Learning rate:  
    Determines how much each new tree contributes to the final prediction, preventing the model from overreacting to residual errors.

- Maximum depth:  
    Limits the complexity of each individual tree, keeping them as weak learners and reducing early overfitting.

**Hyperparameter Tuning and Analysis Method**

To improve model performance, we performed hyperparameter tuning using GridSearchCV. The search space included:

- n_estimators: [100, 200, 300, 400, 500] 
- learning_rate: [0.01, 0.03, 0.05, 0.1]
- max_depth: [2, 3, 4]

The tuning was conducted with 3‑fold cross‑validation on the training set (81,864 observations and 47 features). Because income is highly skewed, predictions were evaluated on a log-transformed scale to reduce the influence of extreme outliers.

Grid search identified the following optimal hyperparameters:

- n_estimators  = 200
- learning_rate = 0.1
- max_depth     = 4

These values balance model complexity and generalization by allowing deeper interactions while maintaining stable learning dynamics.

**Model Performance**

Using the tuned hyperparameters, the model achieved:

- Test MSE: 4.72B
- Test MAE: 29,766
- Test R²: 0.3666

**Comparsion with Baseline Gradient Boosting**

|Parameter/Metric|Baseline GB|**Tuned GB**|Description               |
|----------------|-----------|------------|--------------------------|
|n_estimators    |300        |200         |fewer but sufficient trees|
|learning_rate   |0.05       |0.1         |faster learning           |
|max_depth       |3          |4           |deeper interactions       |
|Test MSE        |4.80B      |4.72B       |lower error               |
|Test MAE        |30,158     |29,766      |lower error               |
|Test R²         |0.3559     |0.3666      |higher R²                 | 

Top 5 Feature Importance (Baseline GB vs. Tuned GB)

- Both models identify RETCONT, OCC2010, EDUC, and SEX as dominant predictors.

- The tuned model places **AGE** in the top 5 instead of **UHRSWORKKT**, reflecting deeper interactions captured by the increased tree depth (`max_depth=4`).

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
| Linear Regression | 72,636        |34,199  |0.2914 |
| Elastic Net       | 5,390,603,768 |33,895  |0.2760 |
| Random Forest     | 3,245,000,000 |32,400  |0.3310 |     
| Gradient Boosting | 4,716,257,047 |29,766  |0.3666 | 

Across the four models, Linear Regression and Elastic Net perform the weakest, showing low R² values and failing to capture the nonlinear structure of income. Although Elastic Net is an extension of Linear Regression with regularization, both remain linear models and therefore struggle to model complex interactions and nonlinear patterns in the data. 

In contrast, Random Forest and Gradient Boosting—both nonlinear tree‑based methods—achieve substantially better predictive performance. Random Forest reduces both MSE and MAE relative to the linear models, while Tuned Gradient Boosting achieves the lowest MAE and the highest R² overall. Its MSE remains higher than that of Random Forest, reflecting greater sensitivity to extreme high‑income outliers, a common characteristic of boosting methods.


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
| **Linear Regression** | <!-- INSERT: reports/figures/rf_results.png (Panel 2) --> |
| **Elastic Net** | <!-- INSERT: reports/figures/gb_results.png (Panel 2) --> |
| **Random Forest** | <img width="437" height="412" alt="image" src="https://github.com/user-attachments/assets/5b972691-2066-462a-802d-3bf358cc24c0" /> |
| **Gradient Boosting** |![Gradient Boosting](reports/figures/gb_actual_vs_predicted.png)



### Reduced Methods (Gradient Boosting*)

* If time permits, add other 3 models

**Feature Selection Rationale**

To evaluate whether a smaller and more interpretable feature set can achieve comparable performance, we constructed a reduced Gradient Boosting model using the 20 features that consistently appeared among the top predictors across Elastic Net, Random Forest, and Gradient Boosting. These variables represent the most stable and influential determinants of income in our dataset and allow us to test the robustness of the Gradient Boosting results while simplifying the feature space.

**Selected Top 20 Features:**

RETCONT, OCC2010, EDUC, SEX, AGE, PAIDGH, FIRMSIZE, RELATE, CBSASZ, MARST,
UHRSWORKT, UHRSWORK1, IND, FAMSIZE, PENSION, EMPSTAT, WKSTAT, HIMCAIDLY,
NUMEMPS, CLASSWKR.

**Reduced Model Summary**

Using only the top 20 consensus features, the reduced Gradient Boosting model achieves performance very close to the full 47‑feature model (R²: 0.3632 vs. 0.3666). Although the reduced model shows a slight decrease in predictive accuracy, the difference is minimal, indicating that most of the predictive signal is concentrated in a relatively small subset of variables. This confirms that the selected features capture the core determinants of income while substantially simplifying the feature space.


### Ensemble Methods (Bagging, Boosting, Stacking)
If time permits, apply ensemble techniques to refine predictions and compare their performance against individual models.


## 5. Reproducibility

### 5.1. Setting up the Virtual Environment

- Create a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install all required packages: `pip install -r requirements.txt`

### 5.2. Clone the repository  
```
git clone <repo-url>
cd ml-midterm
pip install -r requirements.txt
```

### 5.3. Download the data 
Via Google Drive (https://drive.google.com/drive/folders/1ly0tgwf_HWVYg3F5HhfzuLXzHCyhsloz?usp=sharing) and save it in the below folders.  
- data/raw/cps_00001.dat
- data/codebook/cps_00001.xml

### 5.4 Run the code
```  
python3 src/data_clean.py
python3 src/models/model_lr.py
python3 src/models/model_en.py
python3 src/models/model_rf.py
python3 src/models/model_gb.py
python3 src/models/model_gb_top20.py
```
## 6. Limitations and Future Improvements
