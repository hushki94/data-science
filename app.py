import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Load the dataset
DATA_FILE = "vehicles_us.csv"  # Replace with your dataset name
data = pd.read_csv(DATA_FILE)

# Streamlit app title
st.title("Interactive Vehicle Data Dashboard")
