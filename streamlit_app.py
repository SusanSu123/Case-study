import streamlit as st
import pandas as pd

# Set the title of your Streamlit app
st.title("Data Science App")

# Define the GitHub URL of the raw dataset file in your repository
github_url = "https://github.com/SusanSu123/Case-study/blob/b07f3ab3bf24b783fd4219d405927145b8bdaabc/vic_data.xlsx"

# Read the dataset from the GitHub URL into a DataFrame
try:
    df = pd.read_excel(github_url)
    st.write("## Data Preview")
    st.write(df)
except Exception as e:
    st.error(f"An error occurred: {e}")
