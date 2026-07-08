import streamlit as st
import pandas as pd
import plotly.express as px
from ai_chatbot import ask_ai

from analytics import (
    get_statistics,
    compare_locations,
    highest_temperature,
    highest_salinity,
    highest_wave
)
from visualization import (
    plot_temperature,
    plot_salinity,
    plot_wave
)

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="FloatChat",
    page_icon="🌊",
    layout="wide"
)

# -------------------------------------------------
# GLOBAL STYLE
# -------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

/* ===== MAIN BACKGROUND ===== */
.stApp{
    background:
        radial-gradient(circle at 15% 10%, rgba(100,255,218,0.10) 0%, transparent 45%),
        radial-gradient(circle at 85% 90%, rgba(0,180,216,0.14) 0%, transparent 45%),
        linear-gradient(135deg, #052E4A 0%, #0A4C73 45%, #052E4A 100%);
    background-attachment: fixed;
}



/* Sidebar headings */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:#FFFFFF !important;
    font-weight:700;
}

/* Labels */
/* ===== SIDEBAR LABELS ===== */

section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stRadio label,
section[data-testid="stSidebar"] .stMultiSelect label{
    color:#FFFFFF !important;
    -webkit-text-fill-color:#FFFFFF !important;
    font-size:16px !important;
    font-weight:700 !important;
    opacity:1 !important;
}
/* Selectbox */
section[data-testid="stSidebar"]

/* Selected value */
section[data-testid="stSidebar"]

 /* Arrow */
section[data-testid="stSidebar"] 

section[data-testid="stSidebar"] hr{
    border-color:rgba(150,220,255,.2);
}/* ===== SIDEBAR ===== */

section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0E4D75 0%,#082C46 100%);
    border-right:1px solid rgba(150,220,255,.2);
}

/* ===== SIDEBAR SELECTBOX ===== */

section[data-testid="stSidebar"] .stSelectbox{
    margin-bottom:12px;
}

/* White box */
section[data-testid="stSidebar"] .stSelectbox > div{
    background:#FFFFFF !important;
    border-radius:12px !important;
}

/* EVERYTHING inside the selectbox */
section[data-testid="stSidebar"] .stSelectbox *{
    color:#000000 !important;
    -webkit-text-fill-color:#000000 !important;
}

/* SVG arrow */
section[data-testid="stSidebar"] .stSelectbox svg{
    fill:#000000 !important;
}
/* Sidebar headings */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:#FFFFFF !important;
    font-weight:700;
}

/* Labels */
/* ===== SIDEBAR LABELS ===== */

section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] div[data-testid="stWidgetLabel"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span{
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

/* Selectbox */
section[data-testid="stSidebar"] 

/* Selected value */
section[data-testid="stSidebar"]

/* Arrow */
section[data-testid="stSidebar"] 

section[data-testid="stSidebar"] hr{
    border-color:rgba(150,220,255,.2);
}
/* Sidebar subtitle / footer note */
.sidebar-tag{
    display:inline-block;
    margin-top:6px;
    padding:4px 12px;
    border-radius:999px;
    background:rgba(100,255,218,0.15);
    border:1px solid rgba(100,255,218,0.35);
    font-size:12px;
    font-weight:600;
    letter-spacing:.3px;
}

/* ================================================= */
/* SIDEBAR INPUTS - STREAMLIT 1.58 */
/* ================================================= */





/* Selected text */


/* Input */

/* Arrow */
section[data-testid="stSidebar"] svg{
    fill:#000000 !important;
}

/* Dropdown popup */



/* Dropdown popover */


/* Make selected value in sidebar selectbox visible */

/* Input text */


/* Placeholder */

/* Dropdown arrow */

/* ===== TOP TOOLBAR ===== */
header[data-testid="stHeader"]{ background: transparent !important; box-shadow: none; }
[data-testid="stToolbar"]{ background: transparent !important; }

/* ===== BOTTOM CHAT BAR ===== */
[data-testid="stBottomBlockContainer"]{
    background: linear-gradient(180deg, rgba(5,46,74,0) 0%, #052E4A 55%) !important;
}
[data-testid="stBottom"]{ background: transparent !important; }




/* ===== HERO HEADER ===== */
.main-title{
    position:relative;
    text-align:center;
    padding:42px 30px;
    border-radius:26px;
    background: linear-gradient(115deg, #023E5C 0%, #0077b6 40%, #00b4d8 75%, #48cae4 100%);
    color:white;
    box-shadow: 0 15px 45px rgba(0,229,255,0.25);
    margin-bottom:26px;
    border: 1px solid rgba(255,255,255,0.18);
    overflow:hidden;
}
.main-title::before{
    content:"";
    position:absolute;
    inset:0;
    background: radial-gradient(circle at 80% 20%, rgba(255,255,255,0.18), transparent 55%);
    pointer-events:none;
}
.main-title h1{
    font-size:48px;
    font-weight:800;
    margin-bottom:8px;
    text-shadow: 0 2px 14px rgba(0,0,0,0.25);
    letter-spacing:.5px;
}
.main-title p{ font-size:17px; opacity:.95; font-weight:300; }
.main-title .badges{ margin-top:16px; }
.hero-badge{
    display:inline-block;
    margin:4px 6px;
    padding:6px 16px;
    border-radius:999px;
    background:rgba(255,255,255,0.16);
    border:1px solid rgba(255,255,255,0.35);
    font-size:13px;
    font-weight:600;
    backdrop-filter: blur(6px);
}

/* ===== SECTION HEADERS ===== */
.section-eyebrow{
    display:inline-block;
    font-size:12px;
    font-weight:700;
    letter-spacing:1.4px;
    text-transform:uppercase;
    color:#64FFDA;
    background: rgba(100,255,218,0.10);
    border:1px solid rgba(100,255,218,0.3);
    padding:3px 12px;
    border-radius:999px;
    margin-bottom:6px;
}

/* ===== GLASS CARDS (real container wrappers) ===== */
div[data-testid="stVerticalBlockBorderWrapper"]{
    background: rgba(255,255,255,0.08) !important;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(200,235,255,0.20) !important;
    border-radius: 22px !important;
    box-shadow: 0 10px 32px rgba(0,0,0,0.22);
    padding: 6px;
    margin-bottom: 24px;
    transition: 0.25s ease;
}
div[data-testid="stVerticalBlockBorderWrapper"]:hover{
    border-color: rgba(100,229,255,0.45) !important;
    box-shadow: 0 14px 40px rgba(0,229,255,0.18);
}

.stApp h1, .stApp h2, .stApp h3 { color:#F5FCFF !important; font-weight:600; }
.stApp p, .stApp label, .stApp span { color:#EAF7FF; }

/* ===== METRIC CARDS ===== */
[data-testid="metric-container"], [data-testid="stMetric"]{
    background: rgba(255,255,255,0.10);
    backdrop-filter: blur(14px);
    border-radius:18px;
    padding:20px;
    border:1px solid rgba(200,235,255,0.25);
    box-shadow: 0 8px 20px rgba(0,0,0,.15);
    transition:0.3s;
}
[data-testid="metric-container"]:hover, [data-testid="stMetric"]:hover{
    transform:translateY(-5px);
    box-shadow:0 15px 30px rgba(0,229,255,.28);
    border-color:#64FFDA;
}
[data-testid="stMetricValue"]{
    background: linear-gradient(90deg,#F0FBFF,#64FFDA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight:700;
}
[data-testid="stMetricLabel"]{ color:#D6F2FF !important; }

/* ===== BUTTONS ===== */
.stButton>button,
[data-testid="stDownloadButton"] button{
    width:100%;
    border:none;
    border-radius:12px;
    background: linear-gradient(90deg,#0077b6,#00b4d8);
    color:white;
    font-size:15px;
    font-weight:600;
    padding:12px;
    transition:.25s;
    box-shadow: 0 4px 14px rgba(0,229,255,0.22);
}
.stButton>button:hover,
[data-testid="stDownloadButton"] button:hover{
    transform:translateY(-2px) scale(1.01);
    background: linear-gradient(90deg,#00b4d8,#64FFDA);
    box-shadow: 0 8px 22px rgba(0,229,255,.38);
}

/* ===== CHAT MESSAGES ===== */
.stChatMessage{
    border-radius:16px;
    padding:14px;
    background: rgba(255,255,255,0.10);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(200,235,255,0.20);
    box-shadow: 0 6px 18px rgba(0,0,0,.15);
    margin-bottom:10px;
    color:#F0FBFF;
}

/* ===== DATAFRAMES ===== */
[data-testid="stDataFrame"]{
    background: #0A3A5C !important;
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(150,220,255,0.22);
    box-shadow: 0 10px 25px rgba(0,0,0,0.18);
}
[data-testid="stDataFrame"] > div{ background: #0A3A5C !important; }
[data-testid="stDataFrameResizable"]{ background: #0A3A5C !important; }
.glideDataEditor, .gdg-glide-data-grid{ background: #0A3A5C !important; }

/* ===== PLOTLY CHARTS ===== */
.js-plotly-plot{
    border-radius:18px;
    overflow:hidden;
    box-shadow: 0 8px 20px rgba(0,0,0,.15);
}

/* ===== INPUTS ===== */

/* ================================================= */
/* SEARCH BOX */
/* ================================================= */

div[data-testid="stTextInput"] input{
    background:#ffffff !important;
    color:#000000 !important;
    -webkit-text-fill-color:#000000 !important;
    border-radius:12px;
    border:2px solid #64FFDA;
}

div[data-testid="stTextInput"] input::placeholder{
    color:#777777 !important;
}


/* ================================================= */
/* SEARCH BOX */
/* ================================================= */

div[data-testid="stTextInput"] input{
    background:#ffffff !important;
    color:#000000 !important;
    -webkit-text-fill-color:#000000 !important;
    border-radius:12px;
    border:2px solid #64FFDA;
}

div[data-testid="stTextInput"] input::placeholder{
    color:#777777 !important;
}
/* Placeholder */

/* ===== ALERTS ===== */
.stAlert{ border-radius:14px; backdrop-filter: blur(8px); }

/* ===== DIVIDER ===== */
hr{ border:0; height:2px; background: linear-gradient(to right, transparent, #64FFDA, transparent); }

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar{ width:8px; }
::-webkit-scrollbar-thumb{ background: rgba(100,255,218,0.4); border-radius:10px; }


/* ===== CHAT INPUT FIX ===== */
/* ================================================= */
/* CHAT INPUT */
/* ================================================= */

div[data-testid="stChatInput"]{
    background:#ffffff !important;
    border-radius:15px;
}

div[data-testid="stChatInput"] textarea{
    color:#000000 !important;
    -webkit-text-fill-color:#000000 !important;
}

div[data-testid="stChatInput"] textarea::placeholder{
    color:#777777 !important;
}

div[data-testid="stChatInput"] button svg{
    fill:#0077b6 !important;
}

/* Chat input container */

/* Text you type */


/* Placeholder */


/* Send button icon */


/* ===== FOOTER ===== */
.floatchat-footer{
    text-align:center;
    padding:14px;
    font-size:13px;
    color:#BEE8FF;
}

/* ===== FORCE ALL TEXT INPUTS TO BLACK ===== */



/* Streamlit text input */
div[data-testid="stTextInput"] input{
    background: #FFFFFF !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

div[data-testid="stTextInput"] input::placeholder{
    color: #666666 !important;
}



</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/ocean_data.csv")

from live_data import get_live_ocean_data

try:
    df = get_live_ocean_data()
    if df.empty:
        raise Exception("No live data returned from API.")
    st.success("✅ Live data loaded")
except Exception as e:
    st.error(f"Live API Error: {e}")
    df = load_data()

# Clean column names
df.columns = df.columns.map(str).str.strip()

OCEANS = {
    "Chennai": "Bay of Bengal",
    "Mumbai": "Arabian Sea",
    "Kochi": "Arabian Sea",
    "Goa": "Arabian Sea",
    "Visakhapatnam": "Bay of Bengal",
    "Puducherry": "Bay of Bengal",
    "Mangalore": "Arabian Sea",
    "Kanyakumari": "Indian Ocean",
    "Tuticorin": "Gulf of Mannar",
    "Paradip": "Bay of Bengal",
    "Puri": "Bay of Bengal",
    "Kollam": "Arabian Sea",
    "Alappuzha": "Arabian Sea",
    "Karwar": "Arabian Sea",
    "Veraval": "Arabian Sea"
}

if "Ocean" not in df.columns:
    df["Ocean"] = df["Location"].map(OCEANS)

# Check required columns
required_columns = ["Date", "Location", "SST", "Salinity", "WaveHeight"]
missing = [col for col in required_columns if col not in df.columns]

if missing:
    st.error(f"Missing columns: {missing}")
    st.stop()

# Convert numeric columns
for col in ["SST", "Salinity", "WaveHeight"]:
    df[col] = df[col].astype(str).str.strip()
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -------------------------------------------------
# HERO HEADER
# -------------------------------------------------
st.markdown("""
<div class="main-title">
  <h1>🌊 FloatChat</h1>
  <p>AI-Powered Ocean Data Discovery &amp; Visualization Platform</p>
  <div class="badges">
    <span class="hero-badge">🛰️ Live Ocean Feeds</span>
    <span class="hero-badge">🤖 AI Assistant</span>
    <span class="hero-badge">📊 Interactive Analytics</span>
  </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# Chat History
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("🌊 FloatChat")
st.sidebar.markdown('<span class="sidebar-tag">Ocean Explorer</span>', unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown(
    "<h4 style='color:white;margin-bottom:5px;'>📍 Choose Location</h4>",
    unsafe_allow_html=True
)

location = st.sidebar.selectbox(
    "",
    ["All"] + sorted(df["Location"].unique().tolist()),
    label_visibility="collapsed"
)

st.sidebar.markdown(
    "<h4 style='color:white;margin-bottom:5px;'>📈 Parameter</h4>",
    unsafe_allow_html=True
)

parameter = st.sidebar.selectbox(
    "",
    ["All", "SST", "Salinity", "WaveHeight"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.caption("Data refreshes automatically from live ocean feeds when available.")

# Filter Location
filtered_df = df.copy()
if location != "All":
    filtered_df = filtered_df[filtered_df["Location"] == location]

filtered_df = filtered_df.reset_index(drop=True)

if filtered_df.empty:
    st.warning("No data available.")
    st.stop()

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------
with st.container(border=True):
    st.markdown('<span class="section-eyebrow">Overview</span>', unsafe_allow_html=True)
    st.subheader("📊 Ocean Dashboard")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Average SST", f"{filtered_df['SST'].mean():.2f} °C")
    c2.metric("Average Salinity", f"{filtered_df['Salinity'].mean():.2f}")
    c3.metric("Average Wave Height", f"{filtered_df['WaveHeight'].mean():.2f} m")
    c4.metric("Records", len(filtered_df))

# -------------------------------------------------
# CHATBOT
# -------------------------------------------------
with st.container(border=True):
    st.markdown('<span class="section-eyebrow">Assistant</span>', unsafe_allow_html=True)
    header_col, btn_col = st.columns([5, 1])
    with header_col:
        st.subheader("💬 FloatChat Assistant")
    with btn_col:
        if st.button("🗑 Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    query = st.chat_input("Ask anything about ocean data...")

    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)

        answer = ask_ai(query)

        # ----------------------------
        # Show Location
        # ----------------------------
        if answer.startswith("SHOW_LOCATION:"):
            city = answer.split(":")[1].strip()
            city_df = df[df["Location"] == city]

            if not city_df.empty:
                ocean = city_df.iloc[0]["Ocean"]
                message = f"🌊 Showing ocean details for {city} ({ocean})."

                st.session_state.messages.append({"role": "assistant", "content": message})
                with st.chat_message("assistant"):
                    st.write(message)

                st.dataframe(city_df, width="stretch")
                st.plotly_chart(plot_temperature(city_df), width="stretch")
                st.plotly_chart(plot_salinity(city_df), width="stretch")
                st.plotly_chart(plot_wave(city_df), width="stretch")
            else:
                with st.chat_message("assistant"):
                    st.write("No data available for this location.")
        else:
            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.write(answer)

# -------------------------------------------------
# OCEAN INSIGHTS
# -------------------------------------------------
with st.container(border=True):
    st.markdown('<span class="section-eyebrow">Highlights</span>', unsafe_allow_html=True)
    st.subheader("🧠 Ocean Insights")

    max_temp = filtered_df.loc[filtered_df["SST"].fillna(-999).idxmax()]
    min_temp = filtered_df.loc[filtered_df["SST"].fillna(999).idxmin()]
    max_wave = filtered_df.loc[filtered_df["WaveHeight"].fillna(-999).idxmax()]
    max_salinity = filtered_df.loc[filtered_df["Salinity"].fillna(-999).idxmax()]

    ic1, ic2 = st.columns(2)
    with ic1:
        st.success(f"🔥 Highest Temperature: {max_temp['Location']} ({max_temp['SST']} °C)")
        st.warning(f"🌊 Highest Wave Height: {max_wave['Location']} ({max_wave['WaveHeight']} m)")
    with ic2:
        st.info(f"❄️ Lowest Temperature: {min_temp['Location']} ({min_temp['SST']} °C)")
        st.write(f"🧂 Highest Salinity: {max_salinity['Location']} ({max_salinity['Salinity']})")

# -------------------------------------------------
# OCEAN SUMMARY
# -------------------------------------------------
with st.container(border=True):
    st.markdown('<span class="section-eyebrow">Statistics</span>', unsafe_allow_html=True)
    st.subheader("📈 Ocean Data Summary")

    summary_table = pd.DataFrame({
        "Parameter": ["Sea Surface Temperature", "Salinity", "Wave Height"],
        "Minimum": [
            filtered_df["SST"].min(),
            filtered_df["Salinity"].min(),
            filtered_df["WaveHeight"].min()
        ],
        "Maximum": [
            filtered_df["SST"].max(),
            filtered_df["Salinity"].max(),
            filtered_df["WaveHeight"].max()
        ],
        "Average": [
            round(filtered_df["SST"].mean(), 2),
            round(filtered_df["Salinity"].mean(), 2),
            round(filtered_df["WaveHeight"].mean(), 2)
        ]
    })

    st.dataframe(summary_table, width="stretch")

# -------------------------------------------------
# OCEAN HEALTH STATUS
# -------------------------------------------------
with st.container(border=True):
    st.markdown('<span class="section-eyebrow">Condition Check</span>', unsafe_allow_html=True)
    st.subheader("🌍 Ocean Health Status")

    health_df = filtered_df.copy()

    def health_status(row):
        if row["SST"] < 29 and row["WaveHeight"] < 2 and row["Salinity"] >= 34:
            return "🟢 Excellent"
        elif row["SST"] < 30 and row["WaveHeight"] < 2.5:
            return "🟡 Good"
        elif row["SST"] < 31:
            return "🟠 Moderate"
        else:
            return "🔴 Poor"

    health_df["Health Status"] = health_df.apply(health_status, axis=1)

    st.dataframe(
        health_df[["Date", "Location", "SST", "Salinity", "WaveHeight", "Health Status"]],
        width="stretch"
    )

# -------------------------------------------------
# OCEAN ALERTS
# -------------------------------------------------
with st.container(border=True):
    st.markdown('<span class="section-eyebrow">Warnings</span>', unsafe_allow_html=True)
    st.subheader("🚨 Ocean Alerts")

    alerts = []
    for _, row in filtered_df.iterrows():
        if row["SST"] >= 30:
            alerts.append(f"🌡 High Sea Surface Temperature at {row['Location']} ({row['SST']} °C)")
        if row["WaveHeight"] >= 2.5:
            alerts.append(f"🌊 High Wave Height at {row['Location']} ({row['WaveHeight']} m)")
        if row["Salinity"] >= 35.5:
            alerts.append(f"🧂 High Salinity at {row['Location']} ({row['Salinity']})")

    if alerts:
        for alert in alerts:
            st.warning(alert)
    else:
        st.success("✅ No ocean alerts detected.")

# -------------------------------------------------
# PARAMETER DISTRIBUTION
# -------------------------------------------------
with st.container(border=True):
    st.markdown('<span class="section-eyebrow">Visualization</span>', unsafe_allow_html=True)
    st.subheader("📊 Ocean Parameter Distribution")

    chart_option = st.selectbox("Select Parameter", ["SST", "Salinity", "WaveHeight"])

    fig = px.histogram(
        filtered_df,
        x=chart_option,
        color="Location",
        nbins=10,
        title=f"{chart_option} Distribution"
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#EAF7FF",
        legend_title_text="Location"
    )

    st.plotly_chart(fig, width="stretch")

# -------------------------------------------------
# AI OCEAN SUMMARY
# -------------------------------------------------
with st.container(border=True):
    st.markdown('<span class="section-eyebrow">AI Generated</span>', unsafe_allow_html=True)
    st.subheader("🤖 AI Ocean Summary")

    avg_sst = filtered_df["SST"].mean()
    avg_sal = filtered_df["Salinity"].mean()
    avg_wave = filtered_df["WaveHeight"].mean()
    highest_temp_loc = filtered_df.loc[filtered_df["SST"].idxmax(), "Location"]
    highest_wave_loc = filtered_df.loc[filtered_df["WaveHeight"].idxmax(), "Location"]

    ai_summary = f"""
The selected dataset contains {len(filtered_df)} ocean observations.

• Average Sea Surface Temperature: {avg_sst:.2f} °C

• Average Salinity: {avg_sal:.2f}

• Average Wave Height: {avg_wave:.2f} m

• Highest temperature was recorded at {highest_temp_loc}.

• Highest wave height was recorded at {highest_wave_loc}.

Overall, the ocean conditions appear stable based on the available data.
"""
    st.info(ai_summary)

# -------------------------------------------------
# SEARCH + DATASET
# -------------------------------------------------
with st.container(border=True):
    st.markdown('<span class="section-eyebrow">Explore</span>', unsafe_allow_html=True)
    st.subheader("🔍 Search Ocean Data")

    search = st.text_input("Search by Location")

    search_df = filtered_df
    if search:
        search_df = filtered_df[filtered_df["Location"].str.contains(search, case=False)]
        st.success(f"{len(search_df)} record(s) found.")

    st.subheader("📋 Ocean Dataset")
    st.dataframe(
        filtered_df[["Date", "Location", "Ocean", "SST", "Salinity", "WaveHeight"]],
        width="stretch"
    )

    csv = search_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Ocean Data",
        data=csv,
        file_name="ocean_data.csv",
        mime="text/csv"
    )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown(
    '<div class="floatchat-footer">🌊 FloatChat &nbsp;•&nbsp; Developed using Streamlit, Pandas &amp; Plotly</div>',
    unsafe_allow_html=True
)