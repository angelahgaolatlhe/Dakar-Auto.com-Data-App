import streamlit as st
import pandas as pd

# Page Title
st.markdown("<h2 style='text-align:center; color: #1E3A8A; '>Dakar-Auto.com Data Downloads</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Download and explore raw datasets from <a href='https://dakar-auto.com' target='_blank'>Dakar-Auto.com</a></p>", unsafe_allow_html=True)
st.markdown("---")

# Function to load and display data
def load_(dataframe, title, key):
    if st.button(title, key=key):
        st.write(f"Data dimensions: **{dataframe.shape[0]} rows × {dataframe.shape[1]} columns**")
        st.dataframe(dataframe, use_container_width=True)

# Button appearance
st.markdown("""
<style>
.stButton>button {
    font-size: 14px;
    padding: 0.6em 2em;
    border-radius: 6px;
    background-color: #1f77b4;
    color: white;
}
.stButton>button:hover {
    background-color: #155a89;
}
</style>
""", unsafe_allow_html=True)

# Load data
load_(pd.read_csv('data/dakar_auto_voitures-4.csv'), 'Cars', '1')
load_(pd.read_csv('data/Dakar-auto-motocycles.csv'), 'Motocycles & Scooters', '2')
load_(pd.read_csv('data/Dakar-auto-rentals.csv'), 'Car Rentals', '3')
