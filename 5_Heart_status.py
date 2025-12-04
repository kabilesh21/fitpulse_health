import streamlit as st
import pandas as pd
import numpy as np

st.title("💓 FitPulse – Heart Status Checker")

# Load Excel file
file_path = r"D:\fitpulse_health\Excel\fitpulse.xlsx"
data = pd.read_excel(file_path)

st.subheader("📄 Raw Data Preview")
st.dataframe(data.head())

# Heart status function with emojis
def heart_status(rate):
    if rate < 60:
        return 'Low ❄️'
    elif 60 <= rate <= 100:
        return 'Normal 🙂'
    else:
        return 'High 🔥'

# Apply function
data['Heart_Status'] = data['heart_beat_per_minute'].apply(heart_status)

st.subheader("💗 Heart Beat Status Result")
st.dataframe(data[['heart_beat_per_minute', 'Heart_Status']].head(15))

st.success("Heart status calculated successfully! 💚")
