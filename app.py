from ast import main

from networkx import predecessor
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction Model")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms", step=1)
bathrooms = st.number_input("Bathrooms", step=1)
stories = st.number_input("Stories", step=1)
parking = st.number_input("Parking", step=1)

mainroad = st.selectbox("Main Road", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])
furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

price_per_area = 0  # unknown at prediction time → keep 0 or remove feature in training
total_rooms = bedrooms + bathrooms
area_per_room = area / (bedrooms if bedrooms != 0 else 1)


input_df = pd.DataFrame([{
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "parking": parking,
    "mainroad": mainroad,
    "guestroom": guestroom,
    "basement": basement,
    "hotwaterheating": hotwaterheating,
    "airconditioning": airconditioning,
    "prefarea": prefarea,
    "furnishingstatus": furnishingstatus,
    "price_per_area": price_per_area,
    "total_rooms": total_rooms,
    "area_per_room": area_per_room
}])


if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")