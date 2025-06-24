import streamlit as st
import requests
import pandas as pd

API_URL = "http://api:8000/recommend"  # Use 'localhost' if running locally outside Docker

st.title("Business Matchmaker Recommendations")

st.write("Fetching recommendations...")

try:
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    businesses = data.get("recommendations", [])
    if businesses:
        df = pd.DataFrame(businesses)
        st.dataframe(df)
    else:
        st.info("No recommendations found.")
except Exception as e:
    st.error(f"Failed to fetch recommendations: {e}") 