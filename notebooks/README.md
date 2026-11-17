# Original Jupyter analysis notebook

**[Open 01_initial_data_exploration.ipynb](01_initial_data_exploration.ipynb)**

This is the **original notebook supplied by the author**, kept without changes to its cells or saved outputs. It includes 44 cells: 29 code and 15 Markdown. GitHub can show the notebook directly in the browser without execution.

The work moves from inspection of Sol 1741, through initial hourly temperature plots and preliminary quality screening, to comparisons of sols 1741 and 1750 and calculation of reported midday averages.

## Run locally

1. Obtain the NASA PDS `CAL_TIRS` CSV products and companion XML labels described in [`data/README.md`](../data/README.md).
2. Place the CSVs under the repository's `data/raw/` folder using the **exact filenames** in the notebook.
3. Install the packages in [`requirements.txt`](../requirements.txt) in your Python/Anaconda environment.
4. Open the `.ipynb` file in VS Code with the Jupyter extension or a local Jupyter environment. Ensure that the notebook **runs with its working directory set to `notebooks/`**, because the code reads from `../data/raw/`.
5. Run cells from top to bottom and examine any errors before drawing conclusions. Some charts and tables have separate export steps, and some table values are hardcoded.

The notebook has been checked for **valid Jupyter format and Python cell syntax**, but **not executed against the original CSV/XML inputs** as part of this packaging. The saved outputs are historical notebook results, not fresh independent verification.

## Scientific notes

- The first hourly temperature visualization is not fully quality screened.
- The main comparative summaries use four provisional boolean flags and require at least 300 retained observations per 10-minute LMST bin.
- The notebook contains an incorrectly nested loop in the uncertainty section, different inclusion rules at one LTST window boundary, and a manually populated final summary table. See [`CODE_REVIEW_NOTES.md`](../docs/CODE_REVIEW_NOTES.md).
- The notebook is **not a complete instrument calibration or validated atmospheric retrieval**. Please respect PDS XML metadata and measurement uncertainties.
