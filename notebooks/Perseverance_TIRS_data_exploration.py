# %%
print("Hello Mars!")

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("Numpy version:", np.__version__)
print("Pandas version:", pd.__version__)
print ("All libraries imported succesfully.")

# %% [markdown]
# # NASA MEDA — Initial Data Exploration
# 
# ## Sol 1741: Calibrated TIRS Observations
# 
# Objective:
# To understand the structure, variables, and quality
# of the Martian environmental observations before analysis.

# %% [markdown]
# ## 1. Loading the NASA MEDA Dataset
# 
# The calibrated TIRS observations from Perseverance's Sol 1741
# will be imported into Python using the Pandas library.
# 
# Our objective is to convert the raw CSV file into a
# structured DataFrame for further exploration.

# %%
file_path_1741 = "../data/raw/WE__1741___________CAL_TIRS________________P01.csv"
sol_1741 = pd.read_csv(file_path_1741)
print (type(sol_1741))

# %% [markdown]
# ## 2. Initial Dataset Inspection
# 
# Before performing any calculations, we need to understand
# the structure and contents of our dataset.
# 
# We will examine its dimensions, column names, data types,
# and the first few observations.

# %%
sol_1741.head() #printing everything from the 1st 5 rows in a tabular format to check visually

# %%
sol_1741.shape #printing the size of the whole CSV file in (rows,columns) format

# %%
sol_1741.columns #printing all column headings to check all content types

# %% [markdown]
# ## 3. Examining Dataset Structure
# 
# We will inspect the dimensions, data types and
# available observations to understand how the
# NASA MEDA measurements are organised.

# %%
sol_1741.info()

# %%
sol_1741.describe()

# %% [markdown]
# ## 5. Temperature Distribution
# 
# We will examine the statistical distribution of
# air and ground temperatures recorded by MEDA TIRS.
# 
# Our objective is to understand their ranges,
# central tendencies and differences.

# %%
print ("Air Temperature:")
print (sol_1741["AIR_TEMP"].describe())
print ("\nGround Temperature:")
print (sol_1741["GROUND_TEMP"].describe())

# %% [markdown]
# ## 6. Temperature Conversion
# 
# For easier physical interpretation, we will convert
# the air and ground temperatures from Kelvin to Celsius.
# 
# The original NASA measurements will remain unchanged.

# %%
sol_1741["AIR_TEMP_C"] = sol_1741["AIR_TEMP"] - 273.15
sol_1741["GROUND_TEMP_C"] = sol_1741["GROUND_TEMP"] - 273.15
sol_1741[["AIR_TEMP_C", "GROUND_TEMP_C"]].describe()

# %%
print(sol_1741[["SCLK", "LMST", "LTST", "AIR_TEMP_C", "GROUND_TEMP_C"]].head(10))
sol_1741[["SCLK", "LMST", "LTST", "AIR_TEMP_C", "GROUND_TEMP_C"]].tail(10)

# %% [markdown]
# ## 7. Exploring the daily temperature cycle
# Although the LTST is the True Local Standard Time (based on Sun's actual position in the sky), we will still use the LMST here (the Mean Standard Time that is according to a hypothetical constant rate of Sun's movement) for our convenience to plot our temperature curve throughout the Sol 1741.

# %%
# Converting LMST into decimal hours for Matplotlib's easy understanding 
sol_1741["LMST_HOURS"] = (
    pd.to_timedelta(sol_1741["LMST"].str.split("M").str[1])
    .dt.total_seconds() / 3600
)

# Check the converted values
print(sol_1741[["LMST", "LMST_HOURS"]].tail())

# Plotting Time-Temp graph
plt.figure(figsize=(13, 6))

plt.plot(sol_1741["LMST_HOURS"], sol_1741["AIR_TEMP_C"], label="Air Temperature")
plt.plot(sol_1741["LMST_HOURS"], sol_1741["GROUND_TEMP_C"], label="Ground Temperature")

plt.xlabel("Local Mean Solar Time (hours)")
plt.ylabel("Temperature (°C)")
plt.title("Air and Ground Temperature Variation — Mars Sol 1741")

plt.xticks(range(0, 25, 2))
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()



# Find temperature extremes
air_max = sol_1741["AIR_TEMP_C"].idxmax()
air_min = sol_1741["AIR_TEMP_C"].idxmin()

ground_max = sol_1741["GROUND_TEMP_C"].idxmax()
ground_min = sol_1741["GROUND_TEMP_C"].idxmin()

# Display the results
print("AIR TEMPERATURE")
print("Maximum:", sol_1741.loc[air_max, "AIR_TEMP_C"], "°C")
print("Time:", sol_1741.loc[air_max, "LMST"])

print("\nMinimum:", sol_1741.loc[air_min, "AIR_TEMP_C"], "°C")
print("Time:", sol_1741.loc[air_min, "LMST"])

print("\nGROUND TEMPERATURE")
print("Maximum:", sol_1741.loc[ground_max, "GROUND_TEMP_C"], "°C")
print("Time:", sol_1741.loc[ground_max, "LMST"])

print("\nMinimum:", sol_1741.loc[ground_min, "GROUND_TEMP_C"], "°C")
print("Time:", sol_1741.loc[ground_min, "LMST"])

# %% [markdown]
# ## 8. Ground-Air Temperature Difference

# %%
# Calculate the simultaneous ground-air temperature difference
sol_1741["TEMP_DIFFERENCE"] = sol_1741["GROUND_TEMP_C"] - sol_1741["AIR_TEMP_C"]

# Inspect the new column
print(sol_1741[["LMST", "AIR_TEMP_C", "GROUND_TEMP_C", "TEMP_DIFFERENCE"]].head(10))



plt.figure(figsize=(13, 5))

plt.plot(sol_1741["LMST_HOURS"], sol_1741["TEMP_DIFFERENCE"])

plt.axhline(y=0, linestyle="--", label="Equal temperature")

plt.xlabel("Local Mean Solar Time (hours)")
plt.ylabel("Ground - Air Temperature (°C)")
plt.title("Ground_Air Temperature Difference — Mars Sol 1741")

plt.xticks(range(0, 25, 2))
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# %%
# Find maximum and minimum temperature differences
max_diff = sol_1741["TEMP_DIFFERENCE"].idxmax()
min_diff = sol_1741["TEMP_DIFFERENCE"].idxmin()

print("Maximum ground-air temperature difference:")
print(sol_1741.loc[max_diff, ["LMST", "TEMP_DIFFERENCE"]])

print("\nMinimum ground-air temperature difference:")
print(sol_1741.loc[min_diff, ["LMST", "TEMP_DIFFERENCE"]])


# Group observations by their LMST hour
hourly_difference = sol_1741.groupby(
    sol_1741["LMST_HOURS"].astype(int)
)["TEMP_DIFFERENCE"].mean()

print(hourly_difference)



plt.figure(figsize=(12, 5))

plt.plot(hourly_difference.index, hourly_difference.values, marker="o")

plt.axhline(y=0, linestyle="--", label="Equal temperature")

plt.xlabel("Local Mean Solar Time (hours)")
plt.ylabel("Average Ground - Air Temperature (°C)")
plt.title("Hourly Average Ground–Air Temperature Difference — Sol 1741")

plt.xticks(range(0, 24, 2))
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# %% [markdown]
# ## 9. Hourly Temperature Profiles

# %%
# Calculate hourly average temperatures
hourly_temps = sol_1741.groupby(
    sol_1741["LMST_HOURS"].astype(int)
)[["AIR_TEMP_C", "GROUND_TEMP_C"]].mean()

print(hourly_temps)



plt.figure(figsize=(12, 5))

plt.plot(hourly_temps.index, hourly_temps["AIR_TEMP_C"],
         marker="o", label="Air Temperature")

plt.plot(hourly_temps.index, hourly_temps["GROUND_TEMP_C"],
         marker="o", label="Ground Temperature")

plt.xlabel("Local Mean Solar Time (hours)")
plt.ylabel("Average Temperature (°C)")
plt.title("Hourly Average Air and Ground Temperatures — Sol 1741")

plt.xticks(range(0, 24, 2))
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# %% [markdown]
# ## 10. Data Quality Check for each Hour

# %%
# First-pass observation quality screening for Sol 1741

sol_1741["QUALITY_OK"] = (
    (sol_1741["ROVER_LOW_TILT"] == 1)
    & (sol_1741["ROVER_STILL"] == 1)
    & (sol_1741["TIRS_GROUND_FOOTPRINT_NOT_IN_SHADOW"] == 1)
    & (sol_1741["SUN_OUTSIDE_TIRS_FOV"] == 1)
)

# Count observations passing the screen in each hour
quality_by_hour = sol_1741.groupby(
    sol_1741["LMST_HOURS"].astype(int)
)["QUALITY_OK"].agg(["sum", "count"])

print(quality_by_hour)


# %%
flags = [
    "ROVER_LOW_TILT",
    "ROVER_STILL",
    "TIRS_GROUND_FOOTPRINT_NOT_IN_SHADOW",
    "SUN_OUTSIDE_TIRS_FOV"
]

# Fraction of observations marked 1 for each condition, by hour
flag_summary = sol_1741.groupby(
    sol_1741["LMST_HOURS"].astype(int)
)[flags].mean()

print(flag_summary.loc[6:17].round(2))

# %% [markdown]
# ## 11. Reflected solar radiation and Ground Thermal Response

# %%
# Select observations passing our preliminary quality screening
good = sol_1741[sol_1741["QUALITY_OK"]].copy()

# Divide the sol into 10-minute time bins
good["BIN_10MIN"] = (good["LMST_HOURS"] * 6).astype(int)

# Calculate 10-minute averages and observation counts
ten_min = good.groupby("BIN_10MIN").agg(
    sw=("UPWARD_SW_IRRADIANCE", "mean"),
    ground=("GROUND_TEMP_C", "mean"),
    count=("UPWARD_SW_IRRADIANCE", "count")
).reindex(range(144))

# Require at least 300 observations per 10-minute bin
ten_min.loc[ten_min["count"] < 300, ["sw", "ground"]] = float("nan")

ten_min["LMST_HOURS"] = ten_min.index / 6

fig, ax = plt.subplots(2, 1, figsize=(12, 7), sharex=True)

ax[0].plot(ten_min["LMST_HOURS"], ten_min["sw"])
ax[0].set_ylabel("Upward SW Irradiance (W/m²)")
ax[0].set_title("Reflected Shortwave Radiation — Sol 1741")
ax[0].grid(True)

ax[1].plot(ten_min["LMST_HOURS"], ten_min["ground"],
           color="orange")
ax[1].set_ylabel("Ground Brightness Temp (°C)")
ax[1].set_xlabel("Local Mean Solar Time (hours)")
ax[1].set_title("Ground Thermal Response — Sol 1741")
ax[1].grid(True)

plt.xlim(8, 14)
plt.xticks(range(8, 15))
plt.tight_layout()
plt.show()

# %%
# Identify the 10-minute bins with maximum average values
sw_peak_bin = ten_min["sw"].idxmax()
ground_peak_bin = ten_min["ground"].idxmax()

# Calculate the difference between their peak-bin start times
delay_minutes = (ground_peak_bin - sw_peak_bin) * 10

print("Upward SW irradiance:")
print("Peak 10-minute average:", round(ten_min.loc[sw_peak_bin, "sw"], 2), "W/m²")
print("Peak LMST bin:", f"{sw_peak_bin//6:02d}:{(sw_peak_bin%6)*10:02d}")

print("\nGround brightness temperature:")
print("Peak 10-minute average:", round(ten_min.loc[ground_peak_bin, "ground"], 2), "°C")
print("Peak LMST bin:", f"{ground_peak_bin//6:02d}:{(ground_peak_bin%6)*10:02d}")

print("\nGround peak minus SW peak:", delay_minutes, "minutes")

# %% [markdown]
# ## 12. Peak Timing Relative to True Solar Noon

# %%
# Load Sol 1750
sol1750 = pd.read_csv(
    "../data/raw/WE__1750___________CAL_TIRS________________P01.csv"
)

# Extract LMST in decimal hours
sol1750["LMST_HOURS"] = (
    pd.to_timedelta(sol1750["LMST"].str.split("M").str[1])
    .dt.total_seconds() / 3600
)

# Apply the same observation-condition screening
sol1750["QUALITY_OK"] = (
    (sol1750["ROVER_LOW_TILT"] == 1)
    & (sol1750["ROVER_STILL"] == 1)
    & (sol1750["TIRS_GROUND_FOOTPRINT_NOT_IN_SHADOW"] == 1)
    & (sol1750["SUN_OUTSIDE_TIRS_FOV"] == 1)
)

good1750 = sol1750[sol1750["QUALITY_OK"]].copy()

# Group into 10-minute intervals
good1750["BIN_10MIN"] = (good1750["LMST_HOURS"] * 6).astype(int)

ten1750 = good1750.groupby("BIN_10MIN").agg(
    sw=("UPWARD_SW_IRRADIANCE", "mean"),
    ground=("GROUND_TEMP", "mean"),
    count=("UPWARD_SW_IRRADIANCE", "count")
).reindex(range(144))

ten1750.loc[ten1750["count"] < 300, ["sw", "ground"]] = float("nan")

# Compare peak times for both sols

for sol, data, summary in [
    (1741, sol_1741, ten_min),
    (1750, sol1750, ten1750)
]:
    print(f"\nSOL {sol}")

    for name, column in [
        ("Upward SW", "sw"),
        ("Ground Temperature", "ground")
    ]:
        peak_bin = summary[column].idxmax()

        matching_rows = data[
            data["QUALITY_OK"] &
            ((data["LMST_HOURS"] * 6).astype(int) == peak_bin)
        ]

        ltst = pd.to_timedelta(
            matching_rows["LTST"].str.split().str[-1]
        ).median()

        minutes_after_noon = (
            ltst - pd.Timedelta(hours=12)
        ).total_seconds() / 60

        print(name)
        print("LTST:", ltst)
        print("Minutes after solar noon:", round(minutes_after_noon, 1))

# %% [markdown]
# ## 13. Cross-Sol Midday Radiative and Thermal Comparison

# %%
# Compare measurements in the same LTST interval

for sol, data in [(1741, sol_1741), (1750, sol1750)]:

    ltst = pd.to_timedelta(
        data["LTST"].str.split().str[-1]
    )

    midday = data[
        data["QUALITY_OK"]
        & ltst.between(
            pd.Timedelta("12:30:00"),
            pd.Timedelta("13:30:00")
        )
    ]

    print(f"\nSOL {sol}")
    print("Valid observations:", len(midday))

    print("Mean upward SW:",
          round(midday["UPWARD_SW_IRRADIANCE"].mean(), 2), "W/m²")

    print("Mean upward LW:",
          round(midday["UPWARD_LW_IRRADIANCE"].mean(), 2), "W/m²")

    print("Mean ground brightness temperature:",
          round(midday["GROUND_TEMP"].mean() - 273.15, 2), "°C")

# %% [markdown]
# ## 14. Measurement Uncertainty and Variability

# %%
for sol, data in [(1741, sol_1741), (1750, sol1750)]:

    # Convert LTST to a time quantity
    ltst = pd.to_timedelta(
        data["LTST"].str.split().str[-1]
    )

    # Select our previously used midday interval
    midday = data[
        data["QUALITY_OK"]
        & (ltst >= pd.Timedelta("12:30:00"))
        & (ltst < pd.Timedelta("13:30:00"))
    ]

    print(f"\nSOL {sol}")
    print("Number of observations:", len(midday))

    print("\nUpward LW irradiance:")
    print("Mean:", round(midday["UPWARD_LW_IRRADIANCE"].mean(), 2), "W/m²")
    print("Mean reported uncertainty:",
          round(midday["UPWARD_LW_IRRADIANCE_UNCERTAINTY"].mean(), 2),
          "W/m²")

    print("\nGround brightness temperature:")
    print("Mean:", round(midday["GROUND_TEMP"].mean() - 273.15, 2), "°C")
    print("Mean reported uncertainty:",
          round(midday["GROUND_TEMP_UNCERTAINTY"].mean(), 2),
          "K")

    for sol, data in [(1741, sol_1741), (1750, sol1750)]:

     ltst = pd.to_timedelta(
        data["LTST"].str.split().str[-1]
    )

    mask = (
        data["QUALITY_OK"]
        & (ltst >= pd.Timedelta("12:30:00"))
        & (ltst < pd.Timedelta("13:30:00"))
    )

    midday = data.loc[mask].copy()

    # Assign each observation to a 10-minute LTST interval
    midday["TIME_BIN"] = ltst[mask].dt.floor("10min")

    # Calculate average measurements for each interval
    binned = midday.groupby("TIME_BIN").agg(
        LW_MEAN=("UPWARD_LW_IRRADIANCE", "mean"),
        GROUND_MEAN=("GROUND_TEMP", "mean"),
        COUNT=("GROUND_TEMP", "count")
    )

    binned["GROUND_MEAN"] -= 273.15

    print(f"\nSOL {sol}")
    print(binned.round(2))

    # Sol 1741: 10-minute averages between 12:30 and 13:30 LTST

ltst_1741 = pd.to_timedelta(
    sol_1741["LTST"].str.split().str[-1]
)

mask_1741 = (
    sol_1741["QUALITY_OK"]
    & (ltst_1741 >= pd.Timedelta("12:30:00"))
    & (ltst_1741 < pd.Timedelta("13:30:00"))
)

midday_1741 = sol_1741.loc[mask_1741].copy()

midday_1741["TIME_BIN"] = (
    ltst_1741[mask_1741].dt.floor("10min")
)

binned_1741 = midday_1741.groupby("TIME_BIN").agg(
    LW_MEAN=("UPWARD_LW_IRRADIANCE", "mean"),
    GROUND_MEAN=("GROUND_TEMP", "mean"),
    COUNT=("GROUND_TEMP", "count")
)

binned_1741["GROUND_MEAN"] -= 273.15

print("SOL 1741")
print(binned_1741.round(2))

# %% [markdown]
# ## 15. Final Observation Summary

# %%
# Convert Sol 1750 temperatures from Kelvin to Celsius

sol1750["AIR_TEMP_C"] = sol1750["AIR_TEMP"] - 273.15
sol1750["GROUND_TEMP_C"] = sol1750["GROUND_TEMP"] - 273.15

# Verify the new columns
print(sol1750[[
    "AIR_TEMP", "AIR_TEMP_C",
    "GROUND_TEMP", "GROUND_TEMP_C"
]].head())

# %%
def make_ten_min_summary(df):
    df_good = df[df["QUALITY_OK"]].copy()

    df_good["BIN_10MIN"] = (df_good["LMST_HOURS"] * 6).astype(int)

    summary = df_good.groupby("BIN_10MIN").agg(
        AIR_TEMP_C=("AIR_TEMP_C", "mean"),
        GROUND_TEMP_C=("GROUND_TEMP_C", "mean"),
        UPWARD_SW_IRRADIANCE=("UPWARD_SW_IRRADIANCE", "mean"),
        UPWARD_LW_IRRADIANCE=("UPWARD_LW_IRRADIANCE", "mean"),
        COUNT=("LMST_HOURS", "count")
    ).reindex(range(144))

    # Keep only bins with enough observations
    summary.loc[summary["COUNT"] < 300, [
        "AIR_TEMP_C",
        "GROUND_TEMP_C",
        "UPWARD_SW_IRRADIANCE",
        "UPWARD_LW_IRRADIANCE"
    ]] = float("nan")

    summary["LMST_HOURS"] = summary.index / 6
    return summary

ten1741 = make_ten_min_summary(sol_1741)
ten1750 = make_ten_min_summary(sol1750)

# %%
plt.figure(figsize=(12, 6))

plt.plot(ten1741["LMST_HOURS"], ten1741["GROUND_TEMP_C"], label="Ground Temp — Sol 1741")
plt.plot(ten1741["LMST_HOURS"], ten1741["AIR_TEMP_C"], label="Air Temp — Sol 1741")

plt.plot(ten1750["LMST_HOURS"], ten1750["GROUND_TEMP_C"], label="Ground Temp — Sol 1750")
plt.plot(ten1750["LMST_HOURS"], ten1750["AIR_TEMP_C"], label="Air Temp — Sol 1750")

plt.xlabel("Local Mean Solar Time (hours)")
plt.ylabel("Temperature (°C)")
plt.title("Ground and Air Temperature Variation on Mars — Sol 1741 vs Sol 1750")
plt.xticks(range(0, 25, 2))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(12, 6))

plt.plot(ten1741["LMST_HOURS"], ten1741["UPWARD_SW_IRRADIANCE"], label="Sol 1741")
plt.plot(ten1750["LMST_HOURS"], ten1750["UPWARD_SW_IRRADIANCE"], label="Sol 1750")

plt.xlabel("Local Mean Solar Time (hours)")
plt.ylabel("Upward SW Irradiance (W/m²)")
plt.title("Reflected Shortwave Irradiance on Mars — Sol 1741 vs Sol 1750")
plt.xticks(range(0, 25, 2))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(12, 6))

plt.plot(ten1741["LMST_HOURS"], ten1741["UPWARD_LW_IRRADIANCE"], label="Sol 1741")
plt.plot(ten1750["LMST_HOURS"], ten1750["UPWARD_LW_IRRADIANCE"], label="Sol 1750")

plt.xlabel("Local Mean Solar Time (hours)")
plt.ylabel("Upward LW Irradiance (W/m²)")
plt.title("Surface Thermal Emission on Mars — Sol 1741 vs Sol 1750")
plt.xticks(range(0, 25, 2))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# %%
comparison_table = pd.DataFrame({
    "Measurement": [
        "Peak reflected SW (10-min avg)",
        "Peak SW time (LTST)",
        "Peak ground temp (10-min avg)",
        "Peak ground temp time (LTST)",
        "Midday mean upward LW (12:30–13:30 LTST)",
        "Midday mean ground temp"
    ],
    "Sol 1741": [
        "76.67 W/m²",
        "12:52:46",
        "6.53 °C",
        "12:52:46",
        "157.06 W/m²",
        "6.18 °C"
    ],
    "Sol 1750": [
        "73.36 W/m²",
        "12:50:59",
        "-1.32 °C",
        "13:00:58",
        "137.54 W/m²",
        "-1.66 °C"
    ]
})

print(comparison_table)

# %%
fig, axes = plt.subplots(
    2, 1,
    figsize=(12, 7),
    sharex=True
)

# Consistent colors for the two sols
colors = {
    1741: "#2563A6",
    1750: "#D97732"
}

datasets = [
    (1741, ten1741),
    (1750, ten1750)
]

for sol, data in datasets:

    time = data["LMST_HOURS"]

    # Upper panel: Ground brightness temperature
    axes[0].plot(
        time, data["GROUND_TEMP_C"],
        color=colors[sol],
        linewidth=2.2,
        label=f"Sol {sol}"
    )

    # Lower panel: TIRS air temperature
    axes[1].plot(
        time, data["AIR_TEMP_C"],
        color=colors[sol],
        linewidth=1.8,
        label=f"Sol {sol}"
    )

axes[0].set_title(
    "Ground Brightness Temperature",
    fontweight="bold"
)
axes[0].set_ylabel("Temperature (°C)")
axes[0].axhline(0, color="gray", linestyle="--", alpha=0.5)

axes[1].set_title(
    "TIRS Atmospheric Temperature (IR2)",
    fontweight="bold"
)
axes[1].set_ylabel("Temperature (°C)")
axes[1].set_xlabel("Local Mean Solar Time (LMST, hours)")

for ax in axes:
    ax.grid(alpha=0.22)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

axes[0].legend(ncol=2, frameon=False)

axes[1].set_xlim(0, 24)
axes[1].set_xticks(range(0, 25, 2))

fig.suptitle(
    "Martian Temperature Variation | Sol 1741 vs Sol 1750",
    fontsize=15,
    fontweight="bold"
)

fig.text(
    0.08, 0.015,
    "10-minute means; gaps reflect preliminary screening. "
    "TIRS IR2 air-temperature channel has viewing-geometry limitations.",
    fontsize=9,
    color="dimgray"
)

plt.tight_layout(rect=[0, 0.05, 1, 0.95])

plt.savefig(
    "Mars_Temperature_Comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


