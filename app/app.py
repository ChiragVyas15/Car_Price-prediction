import streamlit as st
import pandas as pd
import numpy as np
import pickle 

# Load your trained pipeline
pipe = pickle.load(open("C:\\Users\\chira\\OneDrive\\Desktop\\New folder\\car_price pred\\app\\car_price_pipe.pkl", 'rb'))  # Save your pipeline as car_price_pipe.pkl

st.title("Car Price Predictor")

# User input fields
name = st.text_input("Car Name (e.g. Maruti Suzuki Swift)")
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'LPG', 'CNG'])
year = st.number_input("Year", min_value=1990, max_value=2025, value=2015)
kms_driven = st.number_input("KMs Driven", min_value=0, max_value=500000, value=30000)
company = st.text_input("Company (e.g. Maruti)")

if st.button("Predict Price"):
    input_df = pd.DataFrame([[name, fuel_type, year, kms_driven, company]],
                            columns=['name', 'fuel_type', 'year', 'kms_driven', 'company'])
    price = pipe.predict(input_df)[0]
    st.success(f"Predicted Price: ₹{int(price):,}")

st.write("Note: This is a demo. Results depend on your model and data quality.")