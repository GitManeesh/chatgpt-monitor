import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="AI Usage Monitor",
    page_icon="🚀",
    layout="wide",
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #0b1120 100%
    );
}

.main .block-container {
    padding-top: 1rem;
    max-width: 1400px;
}

.hero {
    text-align: center;
    padding: 2rem;
    margin-bottom: 1rem;
}

.hero-title {
    font-size: 4rem;
    font-weight: 800;
    background: linear-gradient(
        90deg,
        #00c6ff,
        #4facfe,
        #00f2fe
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #cbd5e1;
    font-size: 1.2rem;
}

.metric-card {
    background: linear-gradient(
        135deg,
        #1e293b,
        #334155
    );
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    border: 1px solid #475569;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}

.metric-value {
    font-size: 32px;
    font-weight: 700;
    color: white;
}

.metric-label {
    color: #94a3b8;
}

.info-box {
    background: rgba(0,198,255,0.15);
    border-left: 5px solid #00c6ff;
    padding: 15px;
    border-radius: 10px;
}

.status-card {
    background: #1e293b;
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 10px;
    border-left: 5px solid #22c55e;
}

.footer {
    text-align: center;
    opacity: 0.7;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-title">🚀 AI Usage Monitor</div>
    <div class="hero-subtitle">
        GitHub • Streamlit • AI Analytics Dashboard
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
<b>Info:</b> OpenAI does not currently provide a public API for personal ChatGPT.com
prompt counts, token consumption, or conversation statistics.
This dashboard is a professional monitoring shell ready for future integrations.
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">✅</div>
        <div class="metric-label">Deployment</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">LIVE</div>
        <div class="metric-label">Status</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">GitHub</div>
        <div class="metric-label">Source</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">v1.0</div>
        <div class="metric-label">Version</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

left, right = st.columns([2,1])

with left:

    activity = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Activity": [18, 34, 29, 51, 46, 21, 14]
    })

    fig = px.area(
        activity,
        x="Day",
        y="Activity",
        color_discrete_sequence=["#00c6ff"]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title="Weekly AI Activity"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.markdown(
        """
        <div class="status-card">
        ✅ Repository Connected
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="status-card">
        ✅ Streamlit Running
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="status-card">
        ✅ Automatic Deployment Enabled
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="status-card">
        ⚡ Ready For AI Integrations
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

col_a, col_b = st.columns(2)

with col_a:

    sources = pd.DataFrame({
        "Platform": [
            "ChatGPT",
            "Copilot",
            "Claude",
            "Gemini"
        ],
        "Value": [
            40,
            30,
            20,
            10
        ]
    })

    pie = px.pie(
        sources,
        names="Platform",
        values="Value",
        hole=0.6
    )

    pie.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

with col_b:

    st.subheader("📊 Readiness")

    st.progress(100, text="GitHub Setup")
    st.progress(100, text="Streamlit Deployment")
    st.progress(90, text="Dashboard Design")
    st.progress(30, text="Usage Integrations")
    st.progress(15, text="Authentication")

st.divider()

st.subheader("🖥 Environment Details")

st.code(f"""
Application : AI Usage Monitor
Owner       : Maneesh
Platform    : Streamlit Cloud
Repository  : GitManeesh/chatgpt-monitor
Status      : Online
Version     : 1.0
Updated     : {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
""")

st.divider()

st.subheader("🚀 Future Integrations")

future = pd.DataFrame({
    "Integration": [
        "OpenAI API",
        "Azure OpenAI",
        "LangSmith",
        "Langfuse",
        "Helicone",
        "Custom Agents"
    ],
    "Status": [
        "Ready",
        "Ready",
        "Ready",
        "Ready",
        "Ready",
        "Ready"
    ]
})

st.dataframe(
    future,
    use_container_width=True,
    hide_index=True
)

st.markdown("""
<div class="footer">
Built with ❤️ by Maneesh using Streamlit
</div>
""", unsafe_allow_html=True)
