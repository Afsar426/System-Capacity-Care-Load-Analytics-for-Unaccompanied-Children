import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="System Capacity Dashboard", layout="wide")

# -------------------------
# TITLE
# -------------------------
st.title("📊 System Capacity & Care Load Dashboard")
st.markdown("AI-powered analytics for unaccompanied children care system")

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")  # 🔴 Rename your dataset to data.csv
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# -------------------------
# SIDEBAR FILTER
# -------------------------
st.sidebar.title("🔍 Filters")

date_range = st.sidebar.date_input("Select Date Range", [])

if len(date_range) == 2:
    df = df[(df['Date'] >= pd.to_datetime(date_range[0])) &
            (df['Date'] <= pd.to_datetime(date_range[1]))]

# -------------------------
# KPI CARDS
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Children", int(df['Children in CBP custody'].sum()))
col2.metric("Average Daily", int(df['Children in CBP custody'].mean()))
col3.metric("Max Load", int(df['Children in CBP custody'].max()))

st.divider()

# -------------------------
# TREND GRAPH
# -------------------------
st.subheader("📈 Custody Trend Over Time")

df = df.sort_values('Date')
st.line_chart(df.set_index('Date')['Children in CBP custody'])

# -------------------------
# AREA CHART
# -------------------------
st.subheader("⚖️ Capacity vs Load Analysis")

st.area_chart(df.set_index('Date')['Children in CBP custody'])

# ML PREDICTION (FINAL FIX)
# -------------------------
st.subheader("🔮 Future Prediction (Next 10 Days)")

# Clean data
df_clean = df.dropna(subset=['Children in CBP custody']).copy()

# Create Day column
df_clean['Day'] = np.arange(len(df_clean))

# ✅ DEFINE MODEL FIRST
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Train model
model.fit(df_clean[['Day']], df_clean['Children in CBP custody'])

# Predict future
future_days = np.arange(len(df_clean), len(df_clean)+10).reshape(-1,1)
predictions = model.predict(future_days)

# Show result
pred_df = pd.DataFrame({
    "Day": range(1, 11),
    "Predicted Load": predictions
})

st.line_chart(pred_df.set_index('Day'))
