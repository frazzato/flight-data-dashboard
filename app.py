import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Flight Passenger Dashboard",
    layout="wide"
)

st.title("✈️ Flight Passenger Dashboard")
st.markdown("Monthly airline passenger numbers from **1949 to 1960**.")

@st.cache_data
def load_data():
    data = pd.read_csv(
        "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
    )
    data["Month"] = pd.to_datetime(data["Month"])
    data["Year"] = data["Month"].dt.year
    return data

df = load_data()

# --- Year dropdown ---
years = ["All"] + sorted(df["Year"].unique().tolist())
selected_year = st.selectbox("Select Year", years)

if selected_year != "All":
    filtered_df = df[df["Year"] == selected_year]
else:
    filtered_df = df

# Clean display
filtered_df["Month"] = filtered_df["Month"].dt.strftime("%Y-%m")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Max Passengers", int(filtered_df["Passengers"].max()))
col2.metric("Min Passengers", int(filtered_df["Passengers"].min()))
col3.metric("Avg Passengers", int(filtered_df["Passengers"].mean()))

# Table
st.dataframe(filtered_df, use_container_width=True)

# Chart
st.line_chart(filtered_df.set_index("Month")["Passengers"])
