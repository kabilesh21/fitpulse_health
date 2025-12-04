import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FitPulse Cleaner", layout="wide")

st.title("📊 FitPulse Data Cleaning + Plotly Visualization")

file_path = r"D:\fitpulse_health\Excel\fitpulse.xlsx"

# Load Excel File
try:
    data = pd.read_excel(file_path)
except Exception as e:
    st.error(f"Error loading Excel file: {e}")
    st.stop()

# Show Original Data

st.subheader("🔹 Original Data (First 5 Rows)")
st.dataframe(data.head())

# Clean heart_beat_per_minute

st.header("❤️ Cleaning Heart Beat Column")


data['heart_beat_per_minute'] = pd.to_numeric(
    data['heart_beat_per_minute'], errors='coerce'
)

data['heart_beat_per_minute'] = data['heart_beat_per_minute'].fillna(0).astype(int)

st.subheader("Cleaned Heart Beat Data")
st.dataframe(data[['heart_beat_per_minute']].head())

# Clean Steps Column

st.header("🚶 Cleaning Steps Column")

data['steps'] = pd.to_numeric(data['steps'], errors='coerce')
data['steps'] = data['steps'].fillna(0).astype(int)

st.subheader("Cleaned Steps Data")
st.dataframe(data[['steps']].head())

# Plotly Charts (NO TRENDLINE ANYWHERE)

st.header("📈 Plotly Charts")

# Heart Beat Distribution
fig1 = px.histogram(
    data,
    x="heart_beat_per_minute",
    nbins=30,
    title="Heart Beat Distribution"
)
st.plotly_chart(fig1, width="stretch")

# Steps Distribution
fig2 = px.histogram(
    data,
    x="steps",
    nbins=30,
    title="Steps Distribution"
)
st.plotly_chart(fig2, width="stretch")

# Scatter Plot (NO TRENDLINE)
fig3 = px.scatter(
    data,
    x="steps",
    y="heart_beat_per_minute",
    title="Heart Beat vs Steps Scatter Plot"
)
st.plotly_chart(fig3, width="stretch")

