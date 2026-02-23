"""
Shared configuration for all project charts.
Loads all datasets, defines the color palette, and builds the merged country table.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy.stats import pearsonr
import warnings
warnings.filterwarnings('ignore')

# ── Path to data (same folder as this script) ─────────────────────────────────
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep

# ── Color palette ──────────────────────────────────────────────────────────────
C1    = '#405e4d'   # Dark green  → titles, median lines
C2    = '#63595c'   # Stone grey  → axis labels, annotations
C3    = '#646881'   # Slate       → 2023 color
C4    = '#62bec1'   # Teal        → 2024 color
C5    = '#5ad2f4'   # Sky blue    → 2025 color
BG    = '#f9f9fb'   # Off-white   → figure background
GA    = '#4ade80'   # Green       → Group A (Technological vanguard)
GB    = '#fbbf24'   # Amber       → Group B (Structural lag)
GC    = '#f87171'   # Red         → Group C (Traditional Resilience)
GD    = C1            # Dark green  → Group D (Digital Frontier)
WHITE = 'white'

YEARS = ['2023', '2024', '2025']
YEAR_COLORS = [C3, C4, C5]

# ── Helper functions ───────────────────────────────────────────────────────────
def load_csv(filename):
    """Load a semicolon-separated CSV from DATA_PATH."""
    return pd.read_csv(DATA_PATH + filename, sep=";", encoding='utf-8-sig')

def to_float(df, cols):
    """Convert columns from European decimal format (comma) to float."""
    for c in cols:
        df[c] = pd.to_numeric(
            df[c].astype(str).str.replace(',', '.'), errors='coerce'
        )
    return df

# ── Load all datasets ──────────────────────────────────────────────────────────
df_ia     = to_float(load_csv("database_ia.csv"),                    YEARS)
df_emp    = to_float(load_csv("database_employees.csv"),             YEARS)
df_nace   = to_float(load_csv("database_ia_nace.csv"),               YEARS)
df_ia_eu  = to_float(load_csv("database_ia_europe.csv"),             YEARS)
df_emp_eu = to_float(load_csv("database_employees_europe.csv"),      YEARS)
df_age_eu = to_float(load_csv("database_employees_age_europe.csv"),  YEARS)
df_age    = to_float(load_csv("database_employees_age.csv"),         YEARS)
df_age.columns = ['COUNTRY', 'AGE', '2023', '2024', '2025']

# ── EU-27 aggregate single values per year ─────────────────────────────────────
ai_eu = [float(str(df_ia_eu.iloc[0][y]).replace(',', '.'))  for y in YEARS]
un_eu = [float(str(df_emp_eu.iloc[0][y]).replace(',', '.')) for y in YEARS]

# ── NACE sector name mapping (abbreviations for chart readability) ─────────────
nace_map = {
    "Water supply; sewerage, waste management and remediation activities": "Water and Waste Mgmt",
    "Wholesale and retail trade; repair of motor vehicles and motorcycles": "Wholesale and Retail",
    "Electricity, gas, steam and air conditioning supply":                  "Energy and Supply",
    "Professional, scientific and technical activities":                    "Professional and Tech",
    "Administrative ans supoprt service activities":                        "Admin and Support",
    "Accommodation and food service activities":                            "Hospitality and Food",
    "Information and communication":                                        "Information and Comm.",
    "Real estate activities":                                               "Real Estate",
    "Transportation and storage":                                           "Transport and Storage",
    "Manufacturing":                                                        "Manufacturing",
    "Construction":                                                         "Construction"
}
df_nace['NACE'] = df_nace['NACE'].replace(nace_map)
df_nace = df_nace.sort_values('2025', ascending=True)

# ── Merged country dataset (AI adoption + Unemployment) ───────────────────────
merged = pd.merge(
    df_ia[['COUNTRY', '2023', '2024', '2025']],
    df_emp[['COUNTRY', '2023', '2024', '2025']],
    on='COUNTRY', suffixes=('_ai', '_unemp')
).dropna()
merged.columns = ['COUNTRY', 'ai23', 'ai24', 'ai25', 'un23', 'un24', 'un25']

# ── Quadrant classification using 2025 medians as EU-27 benchmarks ────────────
AI25_MED = merged['ai25'].median()   
UN25_MED = merged['un25'].median()   

def classify_quadrant(row):
    """Assign a strategic group based on the country's position relative to EU medians."""
    if   row['ai25'] >= AI25_MED and row['un25'] >= UN25_MED: return 'A'  # High AI, High Unemp
    elif row['ai25'] <  AI25_MED and row['un25'] >= UN25_MED: return 'B'  # Low AI,  High Unemp
    elif row['ai25'] <  AI25_MED and row['un25'] <  UN25_MED: return 'C'  # Low AI,  Low Unemp
    else:                                                       return 'D'  # High AI, Low Unemp

merged['group'] = merged.apply(classify_quadrant, axis=1)

GROUP_COLORS = {'A': GA, 'B': GB, 'C': GC, 'D': GD}
GROUP_NAMES  = {
    'A': 'Technological Vanguard',
    'B': 'Structural Lag',
    'C': 'Traditional Resilience',
    'D': 'Digital Frontier'
}

# ── Youth unemployment per country (2025) for scatter analysis ─────────────────
youth_c = (df_age[df_age['AGE'].str.contains('Less')][['COUNTRY', '2025']]
           .rename(columns={'2025': 'youth25'}))
merged2 = pd.merge(merged, youth_c, on='COUNTRY')
