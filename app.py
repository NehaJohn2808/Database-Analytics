import streamlit as st
import pandas as pd
import mysql.connector

st.title("📊 Employee Analytics Dashboard")

# Connect MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="",
    database="travel_db"
)

# Fetch Data
query = "SELECT * FROM employee"
df = pd.read_sql(query, conn)

# Show Data
st.subheader("Employee Data")
st.dataframe(df)

# Salary Chart
st.subheader("Salary Analysis")
st.bar_chart(df.set_index("name")["salary"])

# Experience Chart
st.subheader("Experience Analysis")
st.line_chart(df.set_index("name")["experience"])