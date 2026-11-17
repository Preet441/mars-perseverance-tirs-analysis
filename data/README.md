# NASA MEDA–TIRS input products

The analysis uses **Mars 2020 Perseverance MEDA–TIRS calibrated** (`CAL_TIRS`) CSV observations for **Sols 1741 and 1750**. Their PDS4 **XML labels** provide essential units, column descriptions and metadata.

**Official sources:**

- NASA PDS MEDA archive and documentation: https://pdsatmospheres.nmsu.edu/data_and_services/atmospheres_data/PERSEVERANCE/meda.html
- Dataset/bundle DOI: https://doi.org/10.17189/1522849
- Consult the **MEDA RDR Software Interface Specification (RDR SIS)**, accessed through the official PDS documentation, alongside the individual product XML labels.

## Files expected by the notebook

Keep the data locally under:

```text
data/
  README.md
  raw/
    WE__1741___________CAL_TIRS________________P01.csv
    WE__1741___________CAL_TIRS________________P01.xml
    WE__1750___________CAL_TIRS________________P01.csv
    WE__1750___________CAL_TIRS________________P01.xml
```

The XML filenames above are *expected matching product-label filenames*; confirm the exact names and version identifiers in the actual NASA download. The notebook reads the **CSVs only**, but understanding fields and quality flags requires the XML and supporting documentation. If your downloaded products have different filenames/versions, adjust the notebook's input paths after checking their compatibility.

**No original NASA CSV, XML or RDR SIS PDF files are included in this ZIP.** The public source links preserve provenance and avoid unnecessary duplication of large datasets and reference documents. The `data/raw/` folder is listed in `.gitignore` so copies of the raw datasets are not accidentally committed to GitHub.

For a transparent investigation, note the precise product filenames, calibration/version, units, screening flags, sampling coverage and provenance before interpreting outputs.
