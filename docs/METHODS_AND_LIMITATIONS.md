# Methods, results, and interpretation limitations

## Scope

**Independent educational exploratory comparison** of two Martian sols, **1741 and 1750**, using NASA Perseverance **MEDA–TIRS calibrated** products. Two selected sols are insufficient to establish a seasonal trend, a climate pattern or the physical cause of an observed difference.

## Methods actually recorded in the original notebook

- Read each sol's calibrated `CAL_TIRS` CSV with pandas and inspect its columns and observations.
- Convert temperature quantities from Kelvin to degrees Celsius with `°C = K − 273.15`.
- Parse `LMST` into a decimal-hour axis for diurnal plotting.
- Form an initial **unfiltered hourly-mean** Sol 1741 temperature overview; this is **Figure 1**.
- Create a preliminary `QUALITY_OK` mask requiring all these fields to equal `1`: `ROVER_LOW_TILT`, `ROVER_STILL`, `TIRS_GROUND_FOOTPRINT_NOT_IN_SHADOW`, `SUN_OUTSIDE_TIRS_FOV`.
- Aggregate the screened observations into 10-minute **LMST** bins, keeping the bins with at least **300 retained samples**. Excluded/missing intervals remain as gaps rather than being interpolated.
- Plot ground brightness temperature, TIRS IR2-derived atmospheric temperature, upward SW irradiance and upward LW irradiance for sols 1741 and 1750.
- Evaluate a noon-adjacent **LTST** window reported as 12:30–13:30 for selected descriptive averages and observational uncertainties.

**Screening caveat:** These flag choices were made by the author as first-pass observation-condition screens. They are **not a complete independently verified PDS4/TIRS validity specification**. The source XML and MEDA RDR SIS must be considered when asserting sensor-channel reliability.

## Reported values

| Quantity | Sol 1741 | Sol 1750 |
|---|---:|---:|
| Peak 10-minute mean upward SW irradiance | 76.67 W/m² | 73.36 W/m² |
| Time of reported upward SW peak (LTST) | 12:52:46 | 12:50:59 |
| Peak 10-minute mean ground brightness temperature | 6.53 °C | −1.32 °C |
| Time of reported ground peak (LTST) | 12:52:46 | 13:00:58 |
| Midday mean upward SW irradiance | 76.14 W/m² | 72.56 W/m² |
| Midday mean upward LW irradiance | 157.06 W/m² | 137.54 W/m² |
| Midday mean ground brightness temperature | 6.18 °C | −1.66 °C |

Reported **Sol 1750 minus Sol 1741** midday differences: **−3.58 W/m²** (upward SW), **−19.52 W/m²** (upward LW), **−7.84 °C** (ground brightness temperature).

The notebook includes saved outputs supporting the midday means, but its final `comparison_table` contains **literal values rather than full data-driven calculations**. All results remain subject to reproducibility and correctness checks using the original PDS products.

## What the gaps mean

The first hourly temperature figure was created without the later screening. In the comparative plots, selected readings and low-count ten-minute bins are excluded, leaving visible gaps. A gap is **not itself evidence** of a sudden Martian thermal event or permanent instrument failure. Connecting disjoint screened intervals with straight lines would be misleading.

## Why IR2 atmospheric temperature is more variable

The TIRS IR2-derived atmospheric-temperature estimate is **not the same measurement as MEDA ATS near-surface air temperature**. Observational geometry, radiometric retrievals and reported uncertainties may influence the variability, as may genuine atmospheric change. The plots alone cannot isolate these explanations; ten-minute averaging should not be used as justification for forcefully smoothing away real or unexplained structure.

## Physical units and timing

- `GROUND_TEMP` is a radiometrically derived **ground brightness temperature**, not direct soil-contact temperature.
- `UPWARD_SW_IRRADIANCE` has units W/m² and concerns reflected shortwave radiation; it is not itself an albedo measurement.
- `UPWARD_LW_IRRADIANCE` has units W/m² and concerns emitted thermal infrared radiation; it is not a temperature quantity.
- Comparative plot x-axes use **LMST (Local Mean Solar Time)**. Reported peak times and the 12:30–13:30 window are in **LTST (Local True Solar Time)**. These are distinct reference systems.
- The notebook has an **inconsistent end-point convention** in different LTST midday calculations: `.between()` includes 13:30 by default, whereas another uses `< 13:30`. This requires standardization for strict replication.

## Current limitations

- Original CSV and XML datasets were **not supplied to the repository**, so this package was not run end-to-end from source data.
- Some summary results are manually inserted in a notebook table, and the last figures are standalone exports rather than a fully automated figure-generation pipeline.
- The uncertainty section has a nested-loop indentation/control-flow issue (documented in [code review notes](CODE_REVIEW_NOTES.md)).
- Sample-coverage and complete validity checks have not been established against all official calibration/quality guidance.
- Averaging and differences do not by themselves demonstrate causation, and quoted uncertainty means have not been propagated into formal differences or hypothesis tests.

## Source and credit

- [NASA PDS MEDA archive](https://pdsatmospheres.nmsu.edu/data_and_services/atmospheres_data/PERSEVERANCE/meda.html)
- [MEDA dataset DOI](https://doi.org/10.17189/1522849)
- Official MEDA RDR SIS and corresponding PDS XML metadata should be consulted for instrument-specific interpretation.
