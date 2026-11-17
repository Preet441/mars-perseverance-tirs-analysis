# Methods, interpretation, and limitations

## Scope

This is an **exploratory comparison of two selected Martian sols** (1741 and 1750) from NASA Perseverance MEDA–TIRS calibrated observations. Two selected sols do not establish a mission-wide climate pattern or a causal explanation for differences.

## Supplied measurements

| Quantity | Sol 1741 | Sol 1750 |
|---|---:|---:|
| Peak 10-min upward SW irradiance | 76.67 W/m² | 73.36 W/m² |
| Peak SW time (LTST) | 12:52:46 | 12:50:59 |
| Peak 10-min ground brightness temperature | 6.53 °C | −1.32 °C |
| Peak ground-temperature time (LTST) | 12:52:46 | 13:00:58 |
| Midday mean upward SW | 76.14 W/m² | 72.56 W/m² |
| Midday mean upward LW | 157.06 W/m² | 137.54 W/m² |
| Midday mean ground brightness temperature | 6.18 °C | −1.66 °C |

Reported **Sol 1750 − Sol 1741** midday differences: SW **−3.58 W/m²**, LW **−19.52 W/m²**, ground brightness temperature **−7.84 °C**. The author's summary labels the window **12:30–13:30 LTST**. Values above are **transcribed from supplied screenshots**, not recomputed from original raw data in this repository.

## Why are there gaps?

The introductory first plot offers a rough full-day shape; the screened plots deliberately preserve gaps where data were excluded under **preliminary** quality screening. Do not fill gaps with interpolation or connect disjoint intervals and then present them as fully observed time series.

**Crucial reproducibility limitation:** the precise XML- and flag-driven exclusion rules have not yet been uploaded. This repository therefore does not certify that all retained points passed a final quality check.

## Why is the atmospheric temperature noisier?

The atmospheric-temperature panel depicts the **TIRS IR2-derived estimate**, not a direct reading from MEDA's separate Air Temperature Sensor (ATS). Different retrieval sensitivity and observing geometry may matter, as may instrumental uncertainty and actual variation. The graphs cannot distinguish these causes. Ten-minute averaging may leave meaningful short-period variation; do not arbitrarily smooth it away to create a visually cleaner result.

## Physical quantity caution

- **Ground brightness temperature** is inferred radiometrically; it is not necessarily equivalent to a ground-contact thermistor measurement.
- **Upward shortwave** measurements are related to reflected sunlight (W/m²); they are not themselves an albedo measurement.
- **Upward longwave** is thermal infrared irradiance (W/m²), not direct temperature in °C.
- Always retain uncertainty / quality indicators where they are available, and distinguish observations from interpretations.

## Time references and averaging

Figure x-axes display **LMST (Local Mean Solar Time)**, whereas the author's supplied peak times and midday table use **LTST (Local True Solar Time)**. These are different time systems. A rigorous replication needs the exact conversion/selection code and clear averaging windows.

## Not yet verified

- Source CSV/XML exact filenames, versions and calibration labels.
- Quality and geometry masks, plus missing-value treatment.
- Whether mean quantities use identical retained coverage windows across sols.
- Time-base conversions and all tabulated numerical values against actual source data.
- Propagation and treatment of uncertainties.
- A complete reproducible notebook and dependency list.

## References

- NASA Planetary Data System, MEDA archive: https://pdsatmospheres.nmsu.edu/data_and_services/atmospheres_data/PERSEVERANCE/meda.html
- MEDA archive DOI: https://doi.org/10.17189/1522849
