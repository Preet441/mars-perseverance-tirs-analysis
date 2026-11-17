# Review notes — original Python exploration script

**Status:** The original Python script has been copied without modifications and passed a Python syntax check. The original NASA calibrated CSV/XML files were not available for a fresh end-to-end execution during this repository preparation. **No claims of numerical verification or full reproduction are made.**

## Input files and execution

- Script: `notebooks/Perseverance_TIRS_data_exploration.py`.
- Uses the explicit relative input paths `../data/raw/WE__1741___________CAL_TIRS________________P01.csv` and `../data/raw/WE__1750___________CAL_TIRS________________P01.csv`.
- Run from `notebooks/`. A working directory elsewhere will cause file-not-found errors.
- The script requires `numpy`, `pandas`, and `matplotlib`, declared in `requirements.txt` (versions unpinned).

## Screening and aggregation in the code

- First-pass mask `QUALITY_OK` requires the values of `ROVER_LOW_TILT`, `ROVER_STILL`, `TIRS_GROUND_FOOTPRINT_NOT_IN_SHADOW`, and `SUN_OUTSIDE_TIRS_FOV` all to equal `1`.
- `BIN_10MIN = (LMST_HOURS * 6).astype(int)` is used for the 144 bins in one sol. Bins with fewer than `300` observations are blanked out, preserving the gaps in the screened comparison plots.
- This is a **provisional observation-condition screen**, not a validated complete TIRS quality-mask based on the full PDS instrument documentation. The code should document rationale and missing-data handling before it is described as fully reliable.

## Items to fix or verify before claiming fully reproducible scientific results

1. **Hard-coded table values:** The `comparison_table` near the end contains literal result strings, so rerunning it **does not recalculate those summary values from the input datasets**. The separate midday calculations above need to be cross-checked with the displayed tables; the final two supplied PNG tables are not automatically exported by the script.
2. **Section 14 control flow:** A second `for sol, data` loop is nested inside the previous loop, while `mask`, `binned`, and related statements are positioned inconsistently after that nested loop. As written, the results can reflect the final assigned `data` rather than the intended iteration. Make a corrected version after checking the intended loop logic.
3. **Inclusive versus exclusive time window:** The midday summary uses `.between(12:30, 13:30)` (inclusive), while the uncertainty section uses `>= 12:30` and `< 13:30`. Standardize to a clearly documented convention.
4. **Units:** The intermediate `ten1750` summary contains raw `GROUND_TEMP` (Kelvin) in an early section; the later final plotting summary uses `GROUND_TEMP_C` (Celsius). They should be named clearly to avoid interpreting the intermediate result as °C.
5. **Peak times:** Peak bins are based on **LMST**, but their reported timestamps use a median of corresponding **LTST** readings. Verify the precise interpretation of each timestamp and the figure-table consistency.
6. **Noise and data quality:** The IR2 atmospheric-temperature series may be affected by observation/retrieval geometry and uncertainties. The plotted noise by itself cannot tell whether short-term variability is purely instrumental or physical.
7. **Figure generation:** The code saves `Mars_Temperature_Comparison.png` to the working directory, not to the numbered `figures/` names; the repository includes supplied exports separately. A deterministic publication workflow is still an improvement opportunity.
8. **Dataset provenance:** Verify the exact PDS product labels/versions, associated XML files, and any additional quality criteria for each calibrated channel.

## AI assistance and credit

The author provided the original analysis and figures. ChatGPT assisted in preparing repository documentation and this static code review. This preparation did **not** independently validate the numerical outcomes. Suggested scientific corrections should be reviewed before modifying the analysis itself.
