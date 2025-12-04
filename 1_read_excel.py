import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"D:\fitpulse_health\Excel\fitpulse.xlsx"
st.title("FitPulse Data")
# Read Excel file
data = pd.read_excel(file_path)
st.write(data)

