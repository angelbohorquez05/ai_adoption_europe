#  AI Adoption & Unemployment — EU-27 Statistical Analysis (2023–2025)

> **Descriptive statistical analysis of artificial intelligence adoption and its relationship with unemployment rates across all 27 European Union member states over the 2023–2025 period.**

---

## Overview

This project explores what has been called the **European Paradox**: AI adoption in the EU-27 grew from **8% to nearly 20%** between 2023 and 2025 while the overall unemployment rate remained virtually unchanged at around **6%**.

Rather than testing causal hypotheses, this study adopts a **purely descriptive approach**, using visualisations to reveal patterns, disparities, and structural profiles that aggregate statistics conceal.

---

## Repository Structure

```
eu-ai-unemployment/
│
├── data/
│   ├── database_ia.csv                    # AI adoption by country (2021–2025)
│   ├── database_employees.csv             # Unemployment rate by country (2023–2025)
│   ├── database_ia_europe.csv             # EU-27 aggregate AI adoption
│   ├── database_employees_europe.csv      # EU-27 aggregate unemployment
│   ├── database_employees_age.csv         # Youth vs adult unemployment by country
│   ├── database_employees_age_europe.csv  # EU-27 youth/adult unemployment
│   └── database_ia_nace.csv               # AI adoption by economic sector (NACE)
│
├── charts/
│   ├── config.py                          # Shared configuration, palette, data loading
│   ├── 01_global_trends.py                # Phase 1: The European Paradox
│   ├── 02_boxplot_dispersion.py           # Phase 2: Distribution across countries
│   ├── 03_country_comparison.py           # Phase 2: Country-level comparison
│   ├── 04_taxonomy_quadrants.py           # Phase 3: Strategic classification
│   ├── 05_group_profiles.py               # Phase 3: Within-group profiles
│   ├── 06_sector_evolution.py             # Phase 4: Sectoral hierarchy
│   ├── 07_youth_unemployment_gap.py       # Phase 4: Generational gap
│   └── 08_scatter_trajectories.py         # Phase 5: Country trajectories 2023–2025
│
├── outputs/
│   ├── AI_Unemployment_EU27.pptx          # Presentation (11 slides)
│   └── Speaker_Notes_AI_Unemployment.pdf  # Speaker notes with chart interpretations
│
├── requirements.txt
└── README.md
```

---

## Charts — Analysis Flow

The 8 charts follow a deliberate narrative progression across 5 phases:

### Phase 1 — The Paradox
| Chart | Description |
|-------|-------------|
| `01_global_trends.py` | Dual-axis line chart showing AI adoption rising steeply while EU-27 unemployment stays flat (2023–2025) |

### Phase 2 — Dispersion
| Chart | Description |
|-------|-------------|
| `02_boxplot_dispersion.py` | Boxplot with jitter revealing widening inequality across countries — Denmark at 42%, Romania at 5% |
| `03_country_comparison.py` | Stacked bar panels: AI adoption (top) and unemployment (bottom) sorted by AI adoption |

### Phase 3 — Strategic Taxonomy
| Chart | Description |
|-------|-------------|
| `04_taxonomy_quadrants.py` | Scatter plot with 4 shaded quadrants using EU-27 medians as thresholds |
| `05_group_profiles.py` | 2×2 grouped bar chart — one panel per strategic group, ordered to match the taxonomy |

### Phase 4 — Structural Factors
| Chart | Description |
|-------|-------------|
| `06_sector_evolution.py` | Horizontal grouped bars — AI adoption across 11 NACE sectors (2023–2025) |
| `07_youth_unemployment_gap.py` | Line chart with shaded area showing persistent youth vs adult unemployment gap |

### Phase 5 — Synthesis
| Chart | Description |
|-------|-------------|
| `08_scatter_trajectories.py` | 4 scatter panels (one per group) showing country trajectories with arrows and trend lines |

---

## Strategic Taxonomy

Countries are classified into 4 groups using EU-27 medians as benchmarks:
- **AI Adoption median (2025):** 19.6%
- **Unemployment median (2025):** 6.0%

| Group | Position | Label | Countries (n) |
|-------|----------|-------|---------------|
| **A** | High AI · High Unemployment | Technological Vanguard | 8 |
| **B** | Low AI · High Unemployment | Structural Lag | 6 |
| **C** | Low AI · Low Unemployment | Traditional Resilience | 7 |
| **D** | High AI · Low Unemployment | Digital Frontier | 6 |

---

##  Key Findings

1. **The paradox is real** — AI grew 150% while unemployment stayed at ~6%. Aggregate averages conceal very different country-level stories.

2. **Europe is fragmenting** — The gap between digital leaders (Denmark, Finland) and laggards (Romania, Bulgaria) is widening every year.

3. **Sector determines exposure** — Information & Communication leads at 62.5% AI adoption. Construction (10.8%) and Transport (11.1%) remain largely unaffected — physical work is still shielded.

4. **Youth bears the structural cost** — Youth unemployment is consistently ~3× higher than adult unemployment, and the gap is not closing.

5. **Group D shows the sustainable path** — Netherlands, Germany, Austria, Malta and Ireland demonstrate that high AI adoption and low unemployment can coexist when structural foundations are strong.

---

##  Setup & Usage

### Requirements

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
pandas
numpy
matplotlib
```

### Run a chart

All scripts are self-contained and read from the `data/` folder relative to their location. Run from the `charts/` directory:

```bash
cd charts/
python 01_global_trends.py
```

Or run all charts at once:

```bash
cd charts/
for f in 0*.py; do python "$f"; done
```

### Configuration

All shared settings (color palette, data loading, group definitions, medians) live in `config.py`. Import it at the top of each script:

```python
from config import *
```

---

##  Color Palette

| Variable | Hex | Usage |
|----------|-----|-------|
| `C1` | `#405e4d` | Dark green — titles, primary accent |
| `C2` | `#63595c` | Stone grey — axis labels, annotations |
| `C3` | `#9e9e9e` | Neutral grey — unemployment bars |
| `C4` | `#62bec1` | Teal — trend lines, highlights |
| `GA` | `#4ade80` | Group A (Technological Vanguard) |
| `GB` | `#fbbf24` | Group B (Structural Lag) |
| `GC` | `#f87171` | Group C (Traditional Resilience) |
| `GD` | `#405e4d` | Group D (Digital Frontier) |
| `BG` | `#f9f9fb` | Background |

---

##  Data Sources

All data from **Eurostat**:
- [AI adoption in enterprises](https://ec.europa.eu/eurostat) — ISOC_EB_AI
- [Unemployment by age group](https://ec.europa.eu/eurostat) — UNE_RT_A
- [AI adoption by NACE sector](https://ec.europa.eu/eurostat) — ISOC_EB_AI_NACE

Data covers EU-27 member states, years 2023–2025. Values use European decimal format (comma separator) which is converted automatically in `config.py`.


