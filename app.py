import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import random

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Monitor Pro",
    page_icon="🚀",
    layout="wide"
)

# -------------------------
# STYLING
# -------------------------

st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.metric-box {
    background: linear-gradient(
        135deg,
        #1e293b,
        #334155
    );
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 10px;
    border: 1px solid #475569;
}

.metric-value {
    font-size: 32px;
    font-weight: bold;
    color: white;
}

.metric-title {
    color: #cbd5e1;
}

.big-title {
    font-size: 48px;
    font-weight: bold;
    background: linear-gradient(
        90deg,
        #00c6ff,
        #0072ff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("🚀 AI Monitor")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "CSV Upload",
        "Live Metrics",
        "Settings"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("✅ Streamlit Running")
st.sidebar.info("Version 2.0")

# -------------------------
# DASHBOARD
# -------------------------

if page == "Dashboard":

    st.markdown(
        '<div class="big-title">AI Usage Dashboard</div>',
        unsafe_allow_html=True
    )

    st.caption("Modern AI Monitoring Platform")

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("124", "Conversations"),
        ("Active", "Status"),
        ("GitHub", "Repository"),
        ("99.9%", "Health"),
    ]

    cols = [c1, c2, c3, c4]

    for col, (value, title) in zip(cols, metrics):
        with col:
            st.markdown(
                f"""
                <div class="metric-box">
                    <div class="metric-value">{value}</div>
                    <div class="metric-title">{title}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    data = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Usage": [25,35,45,30,65,40,38]
    })

    fig = px.area(
        data,
        x="Day",
        y="Usage",
        title="Weekly AI Activity"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------
# ANALYTICS
# -------------------------

elif page == "Analytics":

    st.title("📈 Analytics")

    df = pd.DataFrame({
        "Model": ["ChatGPT","Copilot","Claude","Gemini"],
        "Usage": [45,25,20,10]
    })

    col1, col2 = st.columns(2)

    with col1:

        pie = px.pie(
            df,
            names="Model",
            values="Usage",
            hole=0.6
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    with col2:

        bar = px.bar(
            df,
            x="Model",
            y="Usage"
        )

        st.plotly_chart(
            bar,
            use_container_width=True
        )

# -------------------------
# CSV UPLOAD
# -------------------------

elif page == "CSV Upload":

    st.title("📂 CSV Upload")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.success("CSV Loaded Successfully")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.write("### Summary")

        st.write(df.describe())

# -------------------------
# LIVE METRICS
# -------------------------

elif page == "Live Metrics":

    st.title("⚡ Live Metrics")

    r1, r2, r3 = st.columns(3)

    r1.metric(
        "Requests/min",
        random.randint(50, 300)
    )

    r2.metric(
        "Tokens/min",
        f"{random.randint(1000,15000):,}"
    )

    r3.metric(
        "Response Time",
        f"{round(random.uniform(0.5,2.5),2)}s"
    )

    data = pd.DataFrame({
        "Minute": list(range(20)),
        "Requests": [
            random.randint(50,300)
            for _ in range(20)
        ]
    })

    line = px.line(
        data,
        x="Minute",
        y="Requests",
        title="Live Request Trend"
    )

    st.plotly_chart(
        line,
        use_container_width=True
    )

# -------------------------
# SETTINGS
# -------------------------

elif page == "Settings":

    st.title("⚙️ Settings")

    st.text_input(
        "OpenAI API Key",
        type="password"
    )

    st.text_input(
        "Azure OpenAI Endpoint"
    )

    st.toggle(
        "Enable Monitoring",
        value=True
    )

    st.info(
        """
        Future integration area:

        • OpenAI API
        • Azure OpenAI
        • LangSmith
        • Langfuse
        • Helicone
        """
    )

# -------------------------
# FOOTER
# -------------------------

st.markdown("---")

st.caption(
    f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)
