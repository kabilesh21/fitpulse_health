import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("💓 FitPulse – Heart Rate Visualization by Gender")

# Load data
file_path = r"D:\fitpulse_health\Excel\fitpulse.xlsx"
data = pd.read_excel(file_path)

st.subheader("📄 Raw Data Preview")
st.dataframe(data.head())

# Step 1: Clean and standardize 'gender'

data['gender'] = data['gender'].astype(str).str.strip().str.lower().replace({
    'm': 'male',
    'f': 'female',
    'nan': 'unknown'
})

# Step 2: Convert heart_beat_per_minute to numeric
data['heart_beat_per_minute'] = pd.to_numeric(data['heart_beat_per_minute'], errors='coerce')

# Step 3: Drop rows with NaN heart rate
data_cleaned = data.dropna(subset=['heart_beat_per_minute'])

# Step 4: Calculate average heart rate by gender
avg_hr_by_gender = data_cleaned.groupby('gender')['heart_beat_per_minute'].mean()

st.subheader("📊 Average Heart Rate by Gender")
st.dataframe(avg_hr_by_gender.reset_index().rename(columns={'heart_beat_per_minute':'avg_heart_rate'}))

# Prepare DataFrame for Plotly

df = pd.DataFrame({
    "gender": avg_hr_by_gender.index,
    "avg_heart_rate": avg_hr_by_gender.values,
    "size": [15, 25, 35],  # Adjust marker sizes
    "color": [1, 2, 3]     # For color scale
})

# 1️⃣ Scatter plot with color scale

st.subheader("1️⃣ Scatter Plot with Color Scale")
fig1 = px.scatter(
    df,
    x="gender",
    y="avg_heart_rate",
    size="size",
    color="color",
    color_continuous_scale="Viridis",
    title="Scatter Plot of Average Heart Rate by Gender"
)
st.plotly_chart(fig1, width="stretch")

# 2️⃣ Line chart with markers (Graph Objects)

st.subheader("2️⃣ Line Chart with Points")
fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=df["gender"],
    y=df["avg_heart_rate"],
    mode="lines+markers",
    name="Heart Rate"
))
fig2.update_layout(title="Line Chart of Average Heart Rate by Gender")
st.plotly_chart(fig2, width="stretch")

# 3️⃣ Simple line chart (Plotly Express)

st.subheader("3️⃣ Simple Line Chart")
fig3 = px.line(
    df,
    x="gender",
    y="avg_heart_rate",
    markers=True,
    title="Average Heart Rate by Gender"
)
st.plotly_chart(fig3, width="stretch")

