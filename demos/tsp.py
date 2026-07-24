import streamlit as st

st.header("Travelling Salesman Problem (TSP)")
number_cities = st.slider('Anzahl der Städte', min_value=1, max_value=20)