import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime


# Load historical dataset
final_df = pd.read_csv("final_df.csv", parse_dates=["date"])

# -------------------------------
# LOAD MODEL
# -------------------------------
model = joblib.load("gradient_boosting_energy_model.pkl")
feature_cols = joblib.load("feature_cols.pkl")

# -------------------------------
# APP CONFIG
# -------------------------------
st.set_page_config(
    page_title="PowerPulse – Energy Forecast",
    layout="centered"
)

st.title("⚡ PowerPulse: Household Energy Usage Forecast")
st.write("Predict household electricity consumption using a trained Gradient Boosting model.")

# -------------------------------
# USER INPUTS
# -------------------------------
st.subheader("Enter Time Information")

input_datetime = st.date_input(
    "Select Date",
    value=datetime.today(),
)

hour = st.selectbox(
    "Hour of Day",
    options=list(range(1, 25)),
    index=11,
)

hour = hour - 1  # convert to 0–23 for model

dayofweek = input_datetime.weekday()
month = input_datetime.month

rolling_mean_24h = final_df["Global_active_power"].tail(24).mean()

# Optional weather
if "avg_temperature" in feature_cols:
    final_df_avg_temperature = (
        final_df.loc[final_df["month"] == month, "avg_temperature"].mean()
    )
    avg_temperature = st.number_input(
        "Average Temperature (°C)",
        value=final_df_avg_temperature,
    )

# -------------------------------
# BUILD INPUT DATAFRAME
# -------------------------------
input_data = {
    "hour": hour,
    "dayofweek": dayofweek,
    "month": month,
    "rolling_mean_24h": rolling_mean_24h,
}

if "avg_temperature" in feature_cols:
    input_data["avg_temperature"] = avg_temperature

input_df = pd.DataFrame([input_data])

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("Predict Energy Usage"):
    prediction = model.predict(input_df)[0]

    st.success(f"🔮 Predicted Energy Consumption: **{prediction:.2f} kW**")

    st.caption("Prediction is based on Sceaux, France historical household energy patterns.")
