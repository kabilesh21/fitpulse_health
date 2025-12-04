import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

st.title("🏠 Linear Regression – House Price Prediction")

# Sample dataset
data = pd.DataFrame({
    "area": [1000, 1500, 2500, 6000],
    "price": [10, 15, 20, 50]
})

st.subheader("📄 Dataset")
st.dataframe(data)

# Features and Target
x = data[['area']]
y = data[['price']]

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

st.write(f"✅ Training size: {len(x_train)}, Test size: {len(x_test)}")

# Train model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict
pred = model.predict(x_test)

# Show predictions
st.subheader("📊 Predictions on Test Data")
results = pd.DataFrame({
    "Area": x_test['area'],
    "Actual Price": y_test['price'].values,
    "Predicted Price": pred.flatten()
})
st.dataframe(results)

# Show Mean Squared Error
mse = mean_squared_error(y_test, pred)
st.write(f"🧮 Mean Squared Error (MSE): **{mse:.3f}**")
