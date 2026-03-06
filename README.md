# ml-midterm
Midterm project for ECO395M

# 1. Project Overview

This project aims to predict total household income using microdata from the IPUMS CPS. We build a complete machine learning pipeline that includes data cleaning, feature engineering, model training, and model evaluation. Several models with different inductive biases are implemented—(1) Linear Regression, (3) Random Forest, (3) Gradient Boosting, and (4) Elastic Net —to compare their predictive performance on tabular socioeconomic data.

After evaluating individual models, we explore ensemble methods such as bagging, boosting, and stacking to further refine prediction accuracy. The goal of the project is to identify the most effective modeling approach for income prediction and to provide a clear, reproducible workflow.

# 2. Dataset Description

# 3. Modeling Approach

# 4. Results Summary

# 5. Repository Structure

# 6. Reproducibility
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
- data/raw/cps_00002.dat
- data/codebook/cps_00002.xml
  
6.4. Run the code  
```
python src/data_clean.py          # Step 1: data cleaning
python src/models/model_rf_gb_lss.py  # Step 2: running models
```
# 7. Future Improvements
