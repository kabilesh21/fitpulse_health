import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import streamlit as st

# Load Data

file_path = r"D:\app\Excel\fitpulse.xlsx"
data = pd.read_excel(file_path)
st.write("### Raw Data", data.head())

# Clean Data

data['heart_beat_per_minute'] = pd.to_numeric(data['heart_beat_per_minute'], errors='coerce')
data_cleaned = data.dropna(subset=['heart_beat_per_minute'])
st.write("### Cleaned Data", data_cleaned.head())

# K-Means Clustering

heartbeat_data = data_cleaned['heart_beat_per_minute'].to_numpy().reshape(-1, 1)

km = KMeans(n_clusters=3, init='k-means++', random_state=42, n_init=10)
km.fit(heartbeat_data)
clusters = km.predict(heartbeat_data)

# Plot Clusters

fig, ax = plt.subplots(figsize=(8, 4))
scatter = ax.scatter(heartbeat_data, np.zeros_like(heartbeat_data), c=clusters, cmap='viridis')
ax.set_title('K-Means Clustering of Heart Beat Per Minute')
ax.set_xlabel('Heart Beat Per Minute')
ax.set_yticks([])  # Hide y-axis
ax.grid(True)

# Display plot in Streamlit
st.pyplot(fig)

