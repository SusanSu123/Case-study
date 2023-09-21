import streamlit as st
import pandas as pd

# Set the title of your Streamlit app
st.title("Data Science Prototype")

# Define the path to your local Excel file
file_path = "/Users/susan/RMIT/3. S2 2023/Case Studies in Data Science/WIL Project/vic_data.xlsx"

# Check if the file exists at the specified path
if st.button("Load Local Excel File"):
    try:
        df = pd.read_excel(file_path)
        st.success("File loaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
