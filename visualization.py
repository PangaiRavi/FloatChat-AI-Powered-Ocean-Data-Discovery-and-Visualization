# visualization.py

import plotly.express as px


# -----------------------------------------
# Temperature Graph
# -----------------------------------------
def plot_temperature(df):

    fig = px.line(
        df,
        x="Date",
        y="SST",
        color="Location",
        markers=True,
        title="Sea Surface Temperature (SST)"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Temperature (°C)"
    )

    return fig


# -----------------------------------------
# Salinity Graph
# -----------------------------------------
def plot_salinity(df):

    fig = px.line(
        df,
        x="Date",
        y="Salinity",
        color="Location",
        markers=True,
        title="Ocean Salinity"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Salinity (PSU)"
    )

    return fig


# -----------------------------------------
# Wave Height Graph
# -----------------------------------------
def plot_wave(df):

    fig = px.line(
        df,
        x="Date",
        y="WaveHeight",
        color="Location",
        markers=True,
        title="Ocean Wave Height"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Wave Height (m)"
    )

    return fig


# -----------------------------------------
# Temperature Bar Chart
# -----------------------------------------
def temperature_bar(df):

    fig = px.bar(
        df,
        x="Location",
        y="SST",
        color="Location",
        title="Average Sea Surface Temperature"
    )

    return fig


# -----------------------------------------
# Salinity Bar Chart
# -----------------------------------------
def salinity_bar(df):

    fig = px.bar(
        df,
        x="Location",
        y="Salinity",
        color="Location",
        title="Average Salinity"
    )

    return fig


# -----------------------------------------
# Wave Height Bar Chart
# -----------------------------------------
def wave_bar(df):

    fig = px.bar(
        df,
        x="Location",
        y="WaveHeight",
        color="Location",
        title="Average Wave Height"
    )

    return fig


# -----------------------------------------
# Scatter Plot
# -----------------------------------------
def scatter_plot(df):

    fig = px.scatter(
        df,
        x="SST",
        y="Salinity",
        color="Location",
        size="WaveHeight",
        hover_data=["Date"],
        title="Ocean Data Scatter Plot"
    )

    return fig