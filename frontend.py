import streamlit as st

pages = [
    st.Page("welcome.py", title="Willkommen"),
    st.Page("demos/tsp.py", title="TSP"),
    st.Page("demos/vrp.py", title="VRP")
]
pg = st.navigation(pages)
pg.run()