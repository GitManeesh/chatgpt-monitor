import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="ChatGPT Usage Monitor",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 ChatGPT Usage Monitor")
st.caption("Personal ChatGPT Dashboard")

st.warning(
    """
    ChatGPT.com does not currently provide a public API that exposes
    personal prompt counts, token usage, or real-time account activity.

    This dashboard shows account status and is ready for future integration.
    """
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Platform",
        "ChatGPT"
    )

with col2:
    st.metric(
        "Account",
        "Active"
    )

with col3:
    st.metric(
        "Deployment",
        "Live"
    )

with col4:
    st.metric(
        "Version",
        "1.0"
    )

st.divider()

st.subheader("📊 Dashboard Status")

status = pd.DataFrame(
    {
        "Component": [
            "GitHub Repository",
            "Streamlit Deployment",
            "Usage Collection",
            "Authentication",
            "Real-Time Usage API"
        ],
        "Status": [
            "✅ Working",
            "✅ Working",
            "⚠️ Not Available",
            "⚠️ Not Configured",
            "❌ Not Available"
        ]
    }
)

st.dataframe(
    status,
    use_container_width=True
)

st.divider()

st.subheader("📈 Example Usage Visualization")

example = pd.DataFrame(
    {
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],
        "Activity": [
            20,
            35,
            28,
            41,
            22,
            15,
            12
        ]
    }
)

fig = px.bar(
    example,
    x="Day",
    y="Activity",
    title="Sample Visualization"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("ℹ️ Deployment Information")

st.code(
f"""
Repository : GitManeesh/chatgpt-monitor
Platform   : Streamlit Cloud
Status     : Running
Updated    : {datetime.now()}
"""
)

st.success(
    "Application deployed successfully and ready for future integrations."
)

st.info(
    """
    Future integrations:

    • OpenAI API Usage
    • Azure OpenAI Usage
    • LangSmith
    • Helicone
    • Langfuse
    • Custom AI Agent Monitoring
    """
)
