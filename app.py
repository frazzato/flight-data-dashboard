import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("📊 Passenger Trends Overview")

@st.cache_data
def load_data():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
    )
    df["Month"] = pd.to_datetime(df["Month"])
    df["Year"] = df["Month"].dt.year
    return df

df = load_data()

# ---------------- Sidebar (Web3 style controls) ----------------
st.sidebar.header("⚙️ Controls")

years = ["All"] + sorted(df["Year"].unique().tolist())
selected_year = st.sidebar.selectbox("Select Year", years)

if selected_year != "All":
    df = df[df["Year"] == selected_year]

# Formatting
df["Month"] = df["Month"].dt.strftime("%Y-%m")

# ---------------- Metrics (Card Layout) ----------------
col1, col2, col3 = st.columns(3)

col1.metric("📈 Max Passengers", int(df["Passengers"].max()))
col2.metric("📉 Min Passengers", int(df["Passengers"].min()))
col3.metric("📊 Avg Passengers", int(df["Passengers"].mean()))

st.divider()

# ---------------- Chart First (Web3 feel) ----------------
st.subheader("Passenger Volume Over Time")
st.line_chart(df.set_index("Month")["Passengers"], use_container_width=True)

st.divider()

# ---------------- Data Table ----------------
st.subheader("Raw Data")
st.dataframe(df, use_container_width=True)
``
