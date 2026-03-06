# ml-midterm
Midterm project for ECO395M

1. Project Overview

2. Dataset Description

3. Modeling Approach

4. Results Summary

5. Repository Structure

6. How to Reproduce
```
git clone <repo-url>
cd ml-midterm
pip install -r requirements.txt
```
Download the data through IPUMS, or receive the data and save it in the below folders  
- data/raw/cps_00002.dat
- data/codebook/cps_00002.xml
```
python src/data_clean.py          # Step 1: data cleaning
python src/models/model_rf_gb_lss.py  # Step 2: running models
```
8. Future Improvements
