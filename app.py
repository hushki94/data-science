import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Load the dataset
DATA_FILE = "vehicles_us.csv"  # Replace with your dataset name
data = pd.read_csv(DATA_FILE)

# Streamlit app title
st.title("Interactive Vehicle Data Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
fuel_filter = st.sidebar.multiselect("Select Fuel Type", data['fuel'].unique(), default=data['fuel'].unique())
condition_filter = st.sidebar.multiselect("Select Condition", data['condition'].unique(), default=data['condition'].unique())

# Filter the data
filtered_data = data[(data['fuel'].isin(fuel_filter)) & (data['condition'].isin(condition_filter))]
