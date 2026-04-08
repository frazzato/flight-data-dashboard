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
    return data

df = load_data()

# Clean display
df["Month"] = df["Month"].dt.strftime("%Y-%m")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Max Passengers", int(df["Passengers"].max()))
col2.metric("Min Passengers", int(df["Passengers"].min()))
col3.metric("Avg Passengers", int(df["Passengers"].mean()))

st.dataframe(df, use_container_width=True)

# Chart
st.line_chart(df.set_index("Month")["Passengers"])
