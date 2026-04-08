import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Flight Passenger Dashboard",
    layout="wide"
)

st.title("✈️ Flight Passenger Dashboard")
st.markdown("Monthly airline passenger numbers from **1949 to 1960**.")

# --- Load data ---
@st.cache_data
def load_data():
    data = pd.read_csv(
        "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
    )
    df["Month"] = df["Month"].dt.strftime("%Y-%m")
    return data

df = load_data()

st.dataframe(df)
