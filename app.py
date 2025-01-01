import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

data = pd.read_csv("vehicles_us.csv" )

st.title("Interactive Vehicle Data Dashboard")

st.sidebar.header("Filters")
fuel_filter = st.sidebar.multiselect("Select Fuel Type", data['fuel'].unique(), default=data['fuel'].unique())
condition_filter = st.sidebar.multiselect("Select Condition", data['condition'].unique(), default=data['condition'].unique())

filtered_data = data[(data['fuel'].isin(fuel_filter)) & (data['condition'].isin(condition_filter))]

st.subheader("Price vs Odometer")
scatter_plot = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='odometer:Q',
    y='price:Q',
    color='fuel:N',
    tooltip=['price', 'odometer', 'fuel']
).properties(
    width=700,
    height=400
).interactive()
st.altair_chart(scatter_plot, use_container_width=True)