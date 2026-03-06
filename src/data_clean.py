"""
IPUMS CPS Data Loading and Cleaning Pipeline

Loads raw CPS fixed-width data, selects analysis features,
replaces IPUMS NIU codes, and saves train/test splits for modeling.
"""

import warnings
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")

# --- Path constants (relative to this file) ---

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CODEBOOK_DIR = PROJECT_ROOT / "data" / "codebook"
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

# --- Analysis constants ---

TARGET = "INCTOT"

IPUMS_NIU_CODES = {99, 999, 9999, 99999, 999999, 9999999, 99999999}

EXCLUDE_VARS = (
    # IDs
    {"SERIAL", "CPSID", "CPSIDP", "CPSIDV",
     "HRHHID", "HRHHID2", "PERNUM", "INDIVIDCC"}
    # Survey weights
    | {"ASECWTH", "ASECWT"}
    # Income sub-components (these sum to INCTOT, so including them is circular)
    | {"INCTOT", "INCWAGE", "INCBUS", "INCFARM", "INCSS",
       "INCWELFR", "INCRETIR", "INCSSI", "INCINT", "INCUNEMP",
       "INCWKCOM", "INCVET", "INCSURV", "INCDISAB", "INCDIVID",
       "INCRENT", "INCEDUC", "INCCHILD", "INCASIST", "INCOTHER",
       "INCRANN", "INCPENS", "INCLONGJ", "OINCBUS", "OINCFARM",
       "OINCWAGE", "INCSURV1", "INCSURV2", "INCDISA1", "INCDISA2",
       "INCRET1", "INCRET2", "INCPEN1", "INCPEN2", "INCRINT1",
       "INCRINT2", "INCCAPG", "HHINCOME", "FTOTVAL"}
    # Tax variables (derived directly from income)
    | {"ADJGINC", "EITCRED", "FEDTAX", "FEDTAXAC",
       "FICA", "MARGTAX", "STATETAX", "STATAXAC", "TAXINC",
       "CTCCRD", "ACTCCRD", "DEPSTAT"}
)


def parse_ddi_xml(xml_path):
    """Parse IPUMS DDI XML codebook to extract variable positions.

    Args:
        xml_path: Path to DDI XML file.
    Returns:
        Tuple of (colspecs, colnames) for pandas.read_fwf.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    ns = "ddi:codebook:2_5"

    colspecs = []
    colnames = []
    for var in root.iter(f"{{{ns}}}var"):
        name = var.get("name")
        loc = var.find(f"{{{ns}}}location")
        if loc is not None:
            start = int(loc.get("StartPos")) - 1
            end = int(loc.get("EndPos"))
            colspecs.append((start, end))
            colnames.append(name)
    return colspecs, colnames


def load_data(codebook_dir, raw_dir):
    """Load CPS fixed-width data using DDI XML codebook.

    Args:
        codebook_dir: Path to directory containing cps_00002.xml.
        raw_dir: Path to directory containing cps_00002.dat.
    Returns:
        DataFrame with all variables.
    """
    colspecs, colnames = parse_ddi_xml(codebook_dir / "cps_00002.xml")
    return pd.read_fwf(
        raw_dir / "cps_00002.dat",
        colspecs=colspecs,
        names=colnames,
        header=None,
    )


def select_features(df):
    """Select analysis features by removing excluded and quality-flag variables.

    Args:
        df: Raw DataFrame.
    Returns:
        List of feature column names.
    """
    return [
        col for col in df.columns
        if col not in EXCLUDE_VARS
        and not col.startswith("Q")
        and col != TARGET
    ]


def clean_data(df, features):
    """Filter valid INCTOT rows, replace IPUMS NIU codes, and impute NaN.

    Uses median imputation instead of dropna() because dropping across
    200+ columns would eliminate all rows.

    Args:
        df: Raw DataFrame.
        features: List of feature column names.
    Returns:
        Cleaned X (features DataFrame) and y (target Series).
    """
    df_clean = (
        df
        .loc[df[TARGET].between(1, 9999998), features + [TARGET]]
        .copy()
    )

    for col in features:
        max_val = df_clean[col].max()
        if max_val in IPUMS_NIU_CODES:
            df_clean[col] = df_clean[col].replace(max_val, np.nan)

    imputer = SimpleImputer(strategy="median")
    X = pd.DataFrame(
        imputer.fit_transform(df_clean[features]),
        columns=features,
    )
    y = df_clean[TARGET].reset_index(drop=True)
    return X, y


def main():
    """Load, clean, split, and save data for downstream modeling."""
    print("Loading data...")
    df = load_data(CODEBOOK_DIR, RAW_DIR)
    print(f"  Raw data shape: {df.shape}")

    features = select_features(df)
    print(f"  Selected {len(features)} features")

    print("Cleaning data...")
    X, y = clean_data(df, features)
    print(f"  Clean data shape: {X.shape}")
    print(f"  Target (INCTOT) mean: ${y.mean():,.0f}, median: ${y.median():,.0f}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42,
    )
    print(f"  Train: {X_train.shape[0]:,} rows / Test: {X_test.shape[0]:,} rows")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    X_train.to_csv(PROCESSED_DIR / "X_train.csv", index=False)
    X_test.to_csv(PROCESSED_DIR / "X_test.csv", index=False)
    y_train.to_csv(PROCESSED_DIR / "y_train.csv", index=False)
    y_test.to_csv(PROCESSED_DIR / "y_test.csv", index=False)
    print(f"\n  Saved train/test splits to {PROCESSED_DIR.relative_to(PROJECT_ROOT)}/")


if __name__ == "__main__":
    main()
