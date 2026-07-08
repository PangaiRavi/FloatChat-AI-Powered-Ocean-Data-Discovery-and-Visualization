# analytics.py

import pandas as pd


# ------------------------------------
# Overall Statistics
# ------------------------------------
def get_statistics(df):

    stats = pd.DataFrame({
        "Metric": [
            "Average SST (°C)",
            "Average Salinity",
            "Average Wave Height (m)",
            "Maximum SST",
            "Minimum SST",
            "Maximum Salinity",
            "Minimum Salinity",
            "Maximum Wave Height",
            "Minimum Wave Height",
            "Total Records"
        ],
        "Value": [
            round(df["SST"].mean(), 2),
            round(df["Salinity"].mean(), 2),
            round(df["WaveHeight"].mean(), 2),
            round(df["SST"].max(), 2),
            round(df["SST"].min(), 2),
            round(df["Salinity"].max(), 2),
            round(df["Salinity"].min(), 2),
            round(df["WaveHeight"].max(), 2),
            round(df["WaveHeight"].min(), 2),
            len(df)
        ]
    })

    return stats


# ------------------------------------
# Compare Locations
# ------------------------------------
def compare_locations(df):

    comparison = (
        df.groupby("Location")[["SST", "Salinity", "WaveHeight"]]
        .mean()
        .round(2)
    )

    return comparison


# ------------------------------------
# Highest Temperature
# ------------------------------------
def highest_temperature(df):

    avg = df.groupby("Location")["SST"].mean()

    city = avg.idxmax()

    value = avg.max()

    return f"{city} has the highest average SST ({value:.2f} °C)."


# ------------------------------------
# Highest Salinity
# ------------------------------------
def highest_salinity(df):

    avg = df.groupby("Location")["Salinity"].mean()

    city = avg.idxmax()

    value = avg.max()

    return f"{city} has the highest average Salinity ({value:.2f})."


# ------------------------------------
# Highest Wave Height
# ------------------------------------
def highest_wave(df):

    avg = df.groupby("Location")["WaveHeight"].mean()

    city = avg.idxmax()

    value = avg.max()

    return f"{city} has the highest average Wave Height ({value:.2f} m)."


# ------------------------------------
# Lowest Temperature
# ------------------------------------
def lowest_temperature(df):

    avg = df.groupby("Location")["SST"].mean()

    city = avg.idxmin()

    value = avg.min()

    return f"{city} has the lowest average SST ({value:.2f} °C)."


# ------------------------------------
# Lowest Salinity
# ------------------------------------
def lowest_salinity(df):

    avg = df.groupby("Location")["Salinity"].mean()

    city = avg.idxmin()

    value = avg.min()

    return f"{city} has the lowest average Salinity ({value:.2f})."


# ------------------------------------
# Lowest Wave Height
# ------------------------------------
def lowest_wave(df):

    avg = df.groupby("Location")["WaveHeight"].mean()

    city = avg.idxmin()

    value = avg.min()

    return f"{city} has the lowest average Wave Height ({value:.2f} m)."