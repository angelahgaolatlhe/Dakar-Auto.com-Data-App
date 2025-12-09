import streamlit as st

st.title("Google Form")

url = "https://forms.gle/T7iejCxbwXw5Fg7K8"

st.components.v1.iframe(url, height=600)