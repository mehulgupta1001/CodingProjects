import pandas as pd
import numpy as np
from prophet import Prophet

# Example dataset (historical disease cases)
data = {
    "ds": pd.date_range(start="2020-01-01", periods=100, freq="D"),
    "y": np.random.randint(5, 50, size=100)
}
df = pd.DataFrame(data)

# Train Prophet model
model = Prophet()
model.fit(df)

def predict_trends(days=30):
    """Predicts future disease cases for given days"""
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(days)
