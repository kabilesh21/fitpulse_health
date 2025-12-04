import streamlit as st
import pandas as pd
import numpy as np

st.title("FitPulse – Gender Code Generator")

# File path (you can also use uploader if needed)
file_path = r"D:\fitpulse_health\Excel\fitpulse.xlsx"

# Load data
data = pd.read_excel(file_path)

st.subheader("Raw Data Preview")
st.dataframe(data.head())

# Create gender code
gender_map = {'male': 1, 'female': 0, 'm': 1, 'f': 0}

data['gender_code'] = (
    data['gender']
    .astype(str)
    .str.strip()
    .str.lower()
    .map(gender_map)
    .fillna(2)
    .astype(int)
)

st.subheader("Gender Code Output")
st.dataframe(data[['gender', 'gender_code']].head(10))
