import streamlit as st
import pandas as pd

# Set the title of your Streamlit app
st.title("Data Science Prototype")

# Define the URL of the dataset
dataset_url = "https://rmiteduau-my.sharepoint.com/:x:/g/personal/s3970670_student_rmit_edu_au/EdR2K2roIBBPqGjHhwiz5XEB1qIy18gyfuZ7BQ_b_XJg0Q?e=AwHIOn"

# Read the dataset from the URL into a DataFrame
df = pd.read_excel(dataset_url)
st.write("## Data Preview")
st.write(df)
