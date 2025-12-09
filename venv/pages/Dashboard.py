import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Use full-width layout
st.set_page_config(layout="wide")

# Title and description
st.markdown("<h2 style='text-align:center; color: #1E3A8A;'>Dakar-Auto.com Data Dashboard</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Insights from cleaned (no missing values and duplicates) Cars, Motorcycles, and Rentals datasets.</p>", unsafe_allow_html=True)
st.markdown("---")

# Load data
cars = pd.read_csv('data/dakar_auto_voitures-4(clean).csv')
motos = pd.read_csv('data/dakar_auto_motocycles(clean).csv')
rentals = pd.read_csv('data/dakar_auto_rentals(clean).csv')

# summary section
st.markdown("""
<div style="
    background-color:#E0F2FE;
    padding:20px;
    border-radius:10px;
    margin-bottom:25px;
">
<h3 style="text-align:center; margin-top:0;">Overview Summary</h3>
</div>
""", unsafe_allow_html=True)

# Summary metrics inside columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cars Listed", len(cars))

with col2:
    st.metric("Motorcycles Listed", len(motos))

with col3:
    st.metric("Car Rentals Listed", len(rentals))

st.markdown("---")

# Plots
left_col, right_col = st.columns(2)

# Histogram (Motorcycle prices)
with left_col:
    st.subheader("Price Distribution of Motorcycles")
    if "price" in motos.columns:
        fig1, ax1 = plt.subplots()
        ax1.hist(motos["price"].dropna(), bins=30)
        ax1.set_xlabel("Price (FCFA)")
        ax1.set_ylabel("Frequency")
        st.pyplot(fig1)
    else:
        st.info("Price column not found in Motorcycle dataset.")

# Bar chart (Top 10 car brands)
with right_col:
    st.subheader("Top 10 Car Brands")
    if "brand" in cars.columns:
        top_brands = cars["brand"].value_counts().head(10)

        fig2, ax2 = plt.subplots()
        top_brands.plot(kind='bar', ax=ax2)
        ax2.set_xlabel("Brand")
        ax2.set_ylabel("Count")
        ax2.set_title("Top 10 Car Brands")
        st.pyplot(fig2)
    else:
        st.info("Brand column not found in Cars dataset.")
