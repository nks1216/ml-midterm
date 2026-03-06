## Dataset Description

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
