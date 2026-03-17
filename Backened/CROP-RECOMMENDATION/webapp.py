# -------------------------------
# Import Libraries
# -------------------------------

from sensor_reader import read_sensor_data

import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
from streamlit_autorefresh import st_autorefresh
from datetime import datetime


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(page_title="KrushtiTech", layout="wide")

# Auto refresh every 2 seconds
st_autorefresh(interval=2000, key="sensor_refresh")


# -------------------------------
# Load Image
# -------------------------------

img = Image.open("crop.png")
st.image(img)


# -------------------------------
# Load Dataset
# -------------------------------

df = pd.read_csv('Crop_recommendation.csv')

X = df[['N','P','K','temperature','humidity','ph','rainfall']]
y = df['label']


# -------------------------------
# Load Model
# -------------------------------

model = pickle.load(open("RF.pkl","rb"))


# -------------------------------
# Prediction Function
# -------------------------------

def predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):

    input_data = np.array(
        [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]
    ).reshape(1,-1)

    prediction = model.predict(input_data)

    return prediction


# -------------------------------
# Streamlit App
# -------------------------------

def main():

    st.markdown(
        "<h1 style='text-align: center;'>SMART CROP RECOMMENDATIONS</h1>",
        unsafe_allow_html=True
    )

    # --------------------------------
    # Initialize Sensor Data in Session State
    # --------------------------------

    if "sensor" not in st.session_state:
        st.session_state["sensor"] = {
            "temperature": 0,
            "humidity": 0,
            "moisture": 0,
            "light": 0,
            "rain": 1
        }

    # --------------------------------
    # Read Sensor Data
    # --------------------------------

    sensor_data = read_sensor_data()

    if sensor_data is not None:
        st.session_state["sensor"] = sensor_data

    sensor = st.session_state["sensor"]

    # --------------------------------
    # Sensor Dashboard
    # --------------------------------

    st.subheader("🌱 Live Sensor Data")

    col1, col2, col3 = st.columns(3)

    col1.metric("Temperature (°C)", sensor["temperature"])
    col2.metric("Humidity (%)", sensor["humidity"])
    col3.metric("Soil Moisture", sensor["moisture"])

    col4, col5 = st.columns(2)

    rain_status = "Detected" if sensor["rain"] == 0 else "No Rain"

    col4.metric("Rain Status", rain_status)
    col5.metric("Light Level", sensor["light"])


    # --------------------------------
    # Irrigation Status
    # --------------------------------

    st.subheader("💧 Smart Irrigation Status")

    # Soil sensor range 0-1023
    if sensor["moisture"] > 700:

        st.success("Pump ON (Soil Dry)")

    else:

        st.info("Pump OFF (Soil Moist)")


    # --------------------------------
    # Sidebar
    # --------------------------------

    st.sidebar.title("KrushtiTech")
    st.sidebar.header("Enter Crop Details")

    nitrogen = st.sidebar.number_input("Nitrogen", 0.0, 140.0, 0.0, key="nitrogen")
    phosphorus = st.sidebar.number_input("Phosphorus", 0.0, 145.0, 0.0, key="phosphorus")
    potassium = st.sidebar.number_input("Potassium", 0.0, 205.0, 0.0, key="potassium")
    ph = st.sidebar.number_input("pH Level", 0.0, 14.0, 0.0, key="ph")

    temperature = sensor["temperature"]
    humidity = sensor["humidity"]

    rainfall = 1 if sensor["rain"] == 0 else 0


    # --------------------------------
    # Prediction Button
    # --------------------------------

    if st.sidebar.button("Predict"):

        if nitrogen == 0 or phosphorus == 0 or potassium == 0 or ph == 0:

            st.error("Please fill all input values")

        else:

            prediction = predict_crop(
                nitrogen,
                phosphorus,
                potassium,
                temperature,
                humidity,
                ph,
                rainfall
            )

            st.session_state["prediction"] = prediction[0]
            st.session_state["inputs"] = {
                "nitrogen": nitrogen,
                "phosphorus": phosphorus,
                "potassium": potassium,
                "ph": ph,
                "temperature": temperature,
                "humidity": humidity,
                "rainfall": rainfall
            }

    # --------------------------------
    # Display Prediction and Report
    # --------------------------------

    if "prediction" in st.session_state:

        st.success(f"The recommended crop is: {st.session_state['prediction']}")

        # -------------------------
        # Farmer Report
        # -------------------------

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        inputs = st.session_state["inputs"]

        report = f"""
KRUSHTITECH SMART AGRICULTURE REPORT
-----------------------------------

Date & Time : {current_time}

Live Sensor Data
----------------
Temperature      : {inputs["temperature"]} °C
Humidity         : {inputs["humidity"]} %
Soil Moisture    : {sensor["moisture"]}
Light Level      : {sensor["light"]}
Rain Status      : {"Rain Detected" if inputs["rainfall"] == 1 else "No Rain"}

Soil Input Values
-----------------
Nitrogen         : {inputs["nitrogen"]}
Phosphorus       : {inputs["phosphorus"]}
Potassium        : {inputs["potassium"]}
pH Level         : {inputs["ph"]}

Crop Recommendation
-------------------
Recommended Crop : {st.session_state['prediction']}

Generated by KrushtiTech
"""

        # Download Button
        st.download_button(
            label="📄 Download Farmer Report",
            data=report,
            file_name="krushtitech_farmer_report.txt",
            mime="text/plain"
        )

            


# -------------------------------
# Run App
# -------------------------------

if __name__ == "__main__":
    main()