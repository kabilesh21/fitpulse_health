import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💓 Average Heart Beat by Gender (Matplotlib)")

file_path = r"D:\app\Excel\fitpulse.xlsx"
data = pd.read_excel(file_path)

# Calculate average heart beat by gender
avg_male_heart_beat = data.loc[
    data['gender'].str.lower().str.strip().isin(['male', 'm']),
    'heart_beat_per_minute'
].mean()

avg_female_heart_beat = data.loc[
    data['gender'].str.lower().str.strip().isin(['female', 'f']),
    'heart_beat_per_minute'
].mean()

st.write(f"👨 Average Male Heart Beat: {avg_male_heart_beat:.2f} bpm")
st.write(f"👩 Average Female Heart Beat: {avg_female_heart_beat:.2f} bpm")

# Plot using matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(['Male 👨', 'Female 👩'], [avg_male_heart_beat, avg_female_heart_beat],
       color=['green', 'yellow'], width=0.6)
ax.set_title("💓 Average Heart Beat Per Minute by Gender")
ax.set_xlabel("Gender")
ax.set_ylabel("Average Heart Beat Per Minute")

st.pyplot(fig)  # <-- Display the plot in Streamlit
