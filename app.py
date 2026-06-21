import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from risk import risk_score
from rag_engine import ask_ai
from autonomous_agents import AutonomousAgent


st.markdown("""
<style>

/* Dark futuristic background */
body {
    background: radial-gradient(circle at 20% 20%, #0f172a, #020617);
    color: #e2e8f0;
}

/* Main container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Glass card effect */
div[data-testid="metric-container"] {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 15px;
    border-radius: 12px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0,255,255,0.08);
}

/* Titles glow effect */
h1, h2, h3 {
    color: #38bdf8;
    text-shadow: 0 0 10px rgba(56,189,248,0.4);
}

/* Sidebar futuristic style */
section[data-testid="stSidebar"] {
    background-color: #0b1220;
    border-right: 1px solid #1e293b;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #0ea5e9, #6366f1);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5rem 1rem;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px rgba(99,102,241,0.5);
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<marquee style="color:#38bdf8;">
LIVE MARKET FEED • AI AGENTS ACTIVE • RISK ENGINE RUNNING • PORTFOLIO SCANNING •
</marquee>
""", unsafe_allow_html=True)


# ======================
# PAGE CONFIG
# ======================
st.set_page_config(page_title="Canada AI Financial Dashboard", layout="wide")

st.title("Canada AI Financial Intelligence Dashboard")

st.markdown("""
<div style="
    background-image: url('https://images.unsplash.com/photo-1535223289827-42f1e9919769');
    background-size: cover;
    padding: 60px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 20px;
    opacity: 0.9;
">
<h1 style="color:white;">AI Financial Intelligence System</h1>
<p style="color:#cbd5e1;">Real-time market intelligence powered by AI agents</p>
</div>
""", unsafe_allow_html=True)




# ======================
# DATABASE CONNECTION
# ======================
engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/canada_intel"
)


# ======================
# LOAD DATA
# ======================
df = pd.read_sql("SELECT * FROM stock_prices", engine)

df.columns = [c.lower() for c in df.columns]

df["date"] = pd.to_datetime(df["date"], errors="coerce")

df = df.dropna()


# ======================
# SIDEBAR FILTER
# ======================
st.sidebar.header("📊 Filters")

stock = st.sidebar.selectbox("Select Stock", df["ticker"].unique())

filtered = df[df["ticker"] == stock]


# ======================
# KPI CARDS
# ======================
col1, col2, col3 = st.columns(3)

col1.metric("📊 Records", len(filtered))
col2.metric("💰 Latest Price", filtered["close"].iloc[-1])
col3.metric("⚠️ Risk Score", risk_score(filtered))

# ======================
# CHARTS
# ======================
st.subheader("📈 Price Trend")

if len(filtered) > 0:
    st.line_chart(filtered.set_index("date")["close"])
    st.bar_chart(filtered.set_index("date")["volume"])
else:
    st.warning("No data available for this stock")


st.subheader("💬 AI Stock Analyst")

question = st.text_input("Ask anything about this stock")

if question:
    with st.spinner("🧠 AI Neural Engine Processing..."):
        response = ask_ai(question, filtered, stock)

    st.write("🤖 AI Answer")
    st.write(response)


st.subheader("🧠 Multi-Agent Market Intelligence")

if st.button("Run AI Agents Analysis"):

    tech_agent = AutonomousAgent("TECH STRATEGIST")
    bank_agent = AutonomousAgent("BANK ANALYST")
    energy_agent = AutonomousAgent("ENERGY ANALYST")

    tech_report = tech_agent.decide(str(filtered.tail(30)))
    bank_report = bank_agent.decide(str(filtered.tail(30)))
    energy_report = energy_agent.decide(str(filtered.tail(30)))

    st.markdown("### 🛒 Tech Agent")
    st.write(tech_report)

    st.markdown("### 🏦 Bank Agent")
    st.write(bank_report)

    st.markdown("### ⚡ Energy Agent")
    st.write(energy_report)
