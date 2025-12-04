🚀 FitPulse – Health Anomaly Detection System
📌 Overview

FitPulse Health Anomaly Detection is a data-driven system designed to analyze fitness-tracking data (heart rate, steps, gender, and activity features) and identify unusual or abnormal health patterns.
It uses Python, Numpy, Pandas, Matplotlib, and Machine Learning algorithms like Linear Regression and K-Means Clustering to generate insights and visualizations in an interactive Streamlit dashboard.

🧠 What is Health Anomaly Detection?

Health anomaly detection refers to identifying unexpected or unusual changes in biometric data — such as sudden heart rate spikes, irregular step patterns, or abnormal activity levels.

It helps in:
Detecting possible health risks
Monitoring fitness trends
Improving decision-making using data

🔧 Tech Stack & Key Components
📘 1. NumPy
NumPy is the foundation of numerical computing in Python.

🐼 2. Pandas

Pandas is used for data manipulation and cleaning.

📊 3. Matplotlib

Matplotlib is a powerful data-visualization library.

🌐 4. Streamlit

Streamlit turns models into interactive dashboards.

🧹 Data Cleaning & Preprocessing
❗ Handling Null Values

Missing data is cleaned using:
-->isnull() to identify missing values
-->fillna() to replace them with mean/median/0

👥 Creating Gender Codes

To standardize gender:
-->Convert to lower case
-->Remove extra spaces

🤖 Machine Learning Models
📈 1. Linear Regression

Used to:
-->Predict heart rate

-->Understand relationships

Identify trend-based anomalies
Example Outputs: Regression line, Prediction vs Actual chart

🔵 2. K-Means Clustering

Used to group similar health patterns.
Helps identify:

Normal vs abnormal clients

High-risk clusters

Unusual behavior in heart rate/steps
Example Outputs: Cluster scatter plot, Centroid visualization
