# Predicting Household Income Using Machine Learning Models

## 1. Project Overview

This project uses CPS microdata to predict total household income and to identify the key socioeconomic factors associated with income variation. Understanding the determinants of household income has important policy implications: accurate income prediction can support targeted social programs, inform tax and welfare design, and shed light on patterns of inequality and economic mobility.

To address this problem, we build a complete machine learning pipeline that includes data cleaning, feature engineering, model training, and model evaluation. Several models with different inductive biases are implemented—(1) Linear Regression, (2) Elastic Net, (3) Random Forest, and (4) Gradient Boosting—to compare their predictive performance on tabular socioeconomic data. We also explore ensemble methods such as bagging, boosting, and stacking to further refine prediction accuracy. The goal is to identify 
the most effective modeling approach and provide a clear, reproducible workflow.

## 2. Dataset Description

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
