# Python analysis script

The original user-supplied Python file is included here:

- [`Perseverance_TIRS_data_exploration.py`](Perseverance_TIRS_data_exploration.py) — a VS Code / Jupyter-style `# %%` cell-based exploration of sols **1741 and 1750**.

## How to run

From the **repository root**:

```bash
python -m pip install -r requirements.txt
cd notebooks
python Perseverance_TIRS_data_exploration.py
```

The code reads two calibrated CSVs using **relative paths** starting `../data/raw/`, so the working directory must be `notebooks/`. Obtain the exact CSV filenames listed in the root README from NASA PDS and place them under `data/raw/`. Keep the corresponding XML labels for metadata and quality interpretation.

The script uses NumPy, pandas, and Matplotlib and creates various exploratory figures. It was syntax-checked with Python, **but not executed end-to-end** in this package because the full CSV datasets were not supplied in this turn. The six images in `figures/` are the author's supplied exports, not independently regenerated here.

## Scientific/reproducibility cautions

- The first hourly Sol 1741 plot predates the four-flag quality mask; **do not treat it as the final screened result**.
- The provisional `QUALITY_OK` mask combines `ROVER_LOW_TILT`, `ROVER_STILL`, `TIRS_GROUND_FOOTPRINT_NOT_IN_SHADOW` and `SUN_OUTSIDE_TIRS_FOV` (all equal to 1).
- Ten-minute LMST summaries exclude bins with fewer than 300 retained observations.
- Some printed summary table rows contain **manually entered strings**, not expressions that compute them automatically.
- There is a duplicated/mis-indented loop in the uncertainty analysis and inconsistent LTST boundary treatment. See [review notes](../docs/CODE_REVIEW_NOTES.md).
- Check any original XML quality requirements and channel viewing geometry before claiming data is fully reliable.
- Avoid running the script from the repository root unchanged: its input paths would fail there.

The original script is preserved **unchanged** to preserve attribution and reviewability. Improvements should be made through transparent, new commits after checking the results.
