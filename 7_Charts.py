import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 FitPulse – Steps and Heart Rate Analysis")

# Load data
file_path = r"D:\fitpulse_health\Excel\fitpulse.xlsx"
data = pd.read_excel(file_path)

st.subheader("📄 Raw Data Preview")
st.dataframe(data.head())

# Steps per Customer Bar Chart

st.header("🚶 Steps Taken by Each Customer")
fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(data['Customer_ID'], data['steps'], color='purple')
ax1.set_title('Steps Taken by Each Customer')
ax1.set_xlabel('Customer ID')
ax1.set_ylabel('Steps')
st.pyplot(fig1)

# Scatter Plot: Steps vs Heart Rate

st.header("💓 Correlation: Steps vs Heart Rate")
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.scatter(data['steps'], data['heart_beat_per_minute'], 
            color='red', alpha=0.6, edgecolor='black')
ax2.set_title('Correlation between Steps and Heart Rate', fontsize=14)
ax2.set_xlabel('Steps', fontsize=12)
ax2.set_ylabel('Heart Beat per Minute', fontsize=12)
ax2.grid(True)
st.pyplot(fig2)

# Correlation Value

correlation = data['steps'].corr(data['heart_beat_per_minute'])
st.write(f"🔗 Correlation between Steps and Heart Rate: **{correlation:.3f}**")
