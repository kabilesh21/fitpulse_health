import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"D:\fitpulse_health\Excel\fitpulse.xlsx"

st.title("FitPulse Data Analysis")

# Read Excel file
data = pd.read_excel(file_path)

# Null value check
st.subheader("Null Value Check")
st.write(data.isnull().sum(), '\n')

# Convert to Numpy arrays
heart = data['heart_beat_per_minute'].to_numpy()
pulse = data['pulse_rate'].to_numpy()
steps = data['steps'].to_numpy()
gend = data['gender'].to_numpy()

# Show shapes
st.subheader("Numpy Array Shapes")
st.write("Heart Numpy Shape:", heart.shape)
st.write("Pulse Numpy Shape:", pulse.shape)
st.write("Steps Numpy Shape:", steps.shape)
st.write("Gender Numpy Shape:", gend.shape)
