import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("System Capacity & Care Load Dashboard")

# Load dataset
df = pd.read_csv("HHS_Unaccompanied_Alien_Children_Program.csv")

# Clean columns
df.columns = df.columns.str.strip()

# Simple display
st.subheader("Dataset Preview")
st.write(df.head())

# Example chart
st.subheader("CBP Custody Trend")
if 'Children in CBP custody' in df.columns:
    st.line_chart(df['Children in CBP custody'])
