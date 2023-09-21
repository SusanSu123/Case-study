import streamlit as st
import pandas as pd

# Set the title of your Streamlit app
st.title("Data Science App")

# Define the relative path to the dataset in the same directory as your .py file
file_path = "vic_data.xlsx"

# Read the local dataset into a DataFrame
try:
    df = pd.read_excel(file_path)
    st.write("## Data Preview")
    st.write(df)
except Exception as e:
    st.error(f"An error occurred: {e}")
