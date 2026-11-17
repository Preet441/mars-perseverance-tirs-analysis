# NASA MEDA–TIRS data source

This project uses **Mars 2020 Perseverance MEDA–TIRS calibrated (`CAL_TIRS`) CSV products**, with corresponding XML metadata, primarily for **Sols 1741 and 1750**.

- Official PDS MEDA archive: https://pdsatmospheres.nmsu.edu/data_and_services/atmospheres_data/PERSEVERANCE/meda.html
- MEDA archive bundle DOI (verify relevant product/version): https://doi.org/10.17189/1522849

Keep each CSV paired with its original XML label so that measurement definitions, units, and quality/context information remain available. The source products are **not currently included** here. The script's input filenames are listed below; verify them against the downloaded PDS product versions and XML labels.

Place local downloads under `data/raw/`; this folder is excluded by `.gitignore` so that large NASA source products do not get accidentally committed.

Important: **TIRS IR2-derived atmospheric temperature is not the same as direct MEDA ATS air-temperature measurements.** Ground brightness temperature is a radiometric quantity. Plot and summary terminology should retain these distinctions.

## Exact CSV file paths used by the published script

The user's supplied code refers to these CSV filenames under `data/raw/`:

- `WE__1741___________CAL_TIRS________________P01.csv`
- `WE__1750___________CAL_TIRS________________P01.csv`

Their matching XML labels must be consulted for the official product structure and quality metadata. These large source files are **not included** in this package.
