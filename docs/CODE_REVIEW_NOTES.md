# Review notes — original Jupyter notebook

**File:** [`notebooks/01_initial_data_exploration.ipynb`](../notebooks/01_initial_data_exploration.ipynb)

The author supplied an **original 44-cell notebook** containing code, explanatory Markdown and saved output cells. The notebook has been **preserved unchanged** in this project package. Its JSON/Jupyter structure passed validation, and each Python code cell passed a static **syntax compilation check**. The original NASA CSV/XML inputs were **not available for an end-to-end execution in this packaging session**. The saved notebook outputs do **not** constitute an independent rerun or scientific validation.

## Data sources and working directory

The notebook reads the following CSVs using paths relative to the `notebooks/` working directory:

- `../data/raw/WE__1741___________CAL_TIRS________________P01.csv`
- `../data/raw/WE__1750___________CAL_TIRS________________P01.csv`

Consult [`data/README.md`](../data/README.md) for the corresponding PDS4 XML labels and official NASA sources. For best results, open the notebook in VS Code/Jupyter and verify the kernel's current working directory before running cells.

## Existing preprocessing and screening

The code applies `QUALITY_OK`, requiring `ROVER_LOW_TILT`, `ROVER_STILL`, `TIRS_GROUND_FOOTPRINT_NOT_IN_SHADOW`, and `SUN_OUTSIDE_TIRS_FOV` all to equal **1**. It groups by `BIN_10MIN = (LMST_HOURS * 6).astype(int)` and blanks ten-minute LMST bins with fewer than **300 retained observations**. These are **preliminary author-selected conditions**, not proof of complete channel validity against the official instrument specifications.

## Items requiring review before claiming full reproducibility

1. **Manual results table.** The end-of-notebook `comparison_table` uses literal strings for peak values and other reported measurements. Re-executing it does **not** recompute those figures from source CSVs. Midday means are calculated separately earlier in the notebook, and saved outputs show the reported values, but the complete final summary is not programmatically regenerated.
2. **Nested-loop control flow in the uncertainty section.** The section beginning `## 14. Measurement Uncertainty and Variability` contains a second `for sol, data` loop inside the previous loop; subsequent statements are not scoped as intended. Its six-bin table is printed for Sol 1750 during both iterations. The additional Sol 1741 calculation underneath is separate. This needs careful correction before trusting the affected uncertainty/variability workflow.
3. **Midday time-window endpoint.** One LTST selection uses `.between(12:30,13:30)` (both endpoints included by default); another uses `>= 12:30` and `< 13:30`. State and apply one consistent interval convention.
4. **Early Sol 1750 Kelvin/Celsius handling.** An intermediate Sol 1750 ten-minute summary groups raw `GROUND_TEMP` in Kelvin, whereas the later cross-sol figure uses `GROUND_TEMP_C`. Clearly distinguish the units when reusing those intermediate results.
5. **Peak time interpretation.** Peak bins are selected in **LMST**; the stated **LTST** peak time is the median LTST among readings in that bin. A peak-bin timestamp is not the exact instant when an instantaneous maximum occurred.
6. **Figure exports.** The notebook saves a specifically named `Mars_Temperature_Comparison.png` in its working directory; the six published images are selected standalone exports and summary screenshots, not all generated to their numbered paths in a single automated run.
7. **Quality assurance.** Full PDS/TIRS flag and viewing-geometry requirements, channel-specific validity, data gaps, uncertainty and possible source-calibration versions need confirmation against matching XML and RDR SIS documents.
8. **Scientific conclusions.** The noisy IR2-derived atmospheric-temperature series cannot be causally attributed to instruments or atmospheric fluctuations from these plots alone. Direct ATS air-temperature readings and TIRS IR2 retrievals should be kept conceptually distinct.

## Attribution and change policy

Original notebook supplied by the project author; ChatGPT assisted with project documentation and static code review. The notebook's cells and outputs have not been silently edited. Proposed fixes should be verified against official source data, then committed as traceable future revisions.
