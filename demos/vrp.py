import streamlit as st

st.header("Vehicle Routing Problem (VRP)")
number_vehicles = st.slider('Anzahl der Fahrzeuge', min_value=1, max_value=3)
number_cities = st.slider('Anzahl der Städte', min_value=1, max_value=20)