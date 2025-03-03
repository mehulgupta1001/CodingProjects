import streamlit as st
import pandas as pd
import plotly.express as px
from model import predict_trends

st.title("🦠 HealthTrend AI: Predicting Disease Outbreaks")

# User input for predictions
days = st.slider("Predict cases for next X days", min_value=7, max_value=90, value=30)
forecast = predict_trends(days)

# Show forecast data
st.subheader("📊 Prediction Data")
st.dataframe(forecast)

# Plot predictions
fig = px.line(forecast, x="ds", y="yhat", title="Disease Trend Prediction")
st.plotly_chart(fig)
