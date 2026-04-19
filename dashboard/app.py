import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("📊 Job Dashboard")

# ✅ Use SQLAlchemy instead
engine = create_engine("mysql+pymysql://root:root123@127.0.0.1/jobs_db")

df = pd.read_sql("SELECT * FROM clean_jobs", engine)

# -------------------------------
# 🔹 HANDLE EMPTY DATA (IMPORTANT)
# -------------------------------
if df.empty:
    st.warning("No data available in clean_jobs table")
    st.stop()

st.write("### All Jobs")
st.dataframe(df)

# -------------------------------
# 🔹 FILTER
# -------------------------------
company = st.selectbox("Filter by company", df['company'].unique())

filtered = df[df['company'] == company]

st.write("### Filtered Jobs")
st.dataframe(filtered)