import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(
    page_title="ChatGPT Usage Monitor",
    layout="wide"
)

st.title("🚀 ChatGPT Usage Monitor")

requests = random.randint(1000, 5000)
tokens = random.randint(100000, 1000000)
cost = round(tokens * 0.000002, 2)

col1, col2, col3 = st.columns(3)

col1.metric("Requests", requests)
col2.metric("Tokens", f"{tokens:,}")
col3.metric("Estimated Cost", f"${cost}")

df = pd.DataFrame({
    "Hour": list(range(24)),
    "Tokens":[random.randint(1000,5000) for _ in range(24)]
})

fig = px.line(
    df,
    x="Hour",
    y="Tokens",
    title="Token Usage Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Recent Activity")

st.dataframe(pd.DataFrame({
    "User":["Maneesh","Agent","Copilot"],
    "Requests":[125,84,55]
}))
