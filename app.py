import streamlit as st
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# --- LOAD ENVIRONMENT VARIABLES ---
load_dotenv()

# --- IMPORT YOUR CREW LOGIC ---
try:
    from crew import run_crew 
except ImportError:
    st.error("🚨 Error: 'crew.py' connection failed.")

# --- CONFIG ---
st.set_page_config(
    page_title="AgentForge Elite | Premium AI",
    page_icon="💠",
    layout="wide",
)

# --- WEBHOOK ---
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/m4dzevy0jky3h3r86cbrhedvyibjkt8j"

# --- THE "CYBER-WHITE" PROFESSIONAL STYLING ---
st.markdown("""
    <style>
    /* Main Background with a subtle gradient */
    .main {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        color: #1e293b;
    }

    /* Clean Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }

    /* Card Styling */
    .stMetric, .output-box, .input-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }

    /* Primary Action Button - Minimalist Gradient */
    div.stButton > button:first-child {
        background: #0f172a;
        color: #ffffff;
        border: none;
        border-radius: 6px;
        padding: 0.7rem 1.2rem;
        font-weight: 500;
        transition: all 0.2s ease;
        width: 100%;
    }
    div.stButton > button:hover {
        background: #334155;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2);
    }

    /* Status Container */
    .stStatus {
        border-radius: 10px;
        border: 1px solid #cbd5e1;
    }

    /* Output Box with High Readability */
    .output-box {
        font-family: 'SF Pro Display', 'Inter', sans-serif;
        font-size: 1.05rem;
        line-height: 1.7;
        color: #334155;
        border-left: 4px solid #3b82f6;
        white-space: pre-wrap;
    }

    /* Title Styling */
    .main-title {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(to right, #0f172a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTROL PANEL ---
with st.sidebar:
    st.markdown("### 💠 **AgentForge v3.5**")
    st.caption("Active Session Control")
    st.markdown("---")
    
    # Intelligence Parameters in Sidebar
    st.subheader("Global Settings")
    st.checkbox("Enable Neural Memory", value=True)
    st.checkbox("High Contrast Mode", value=True)
    
    st.markdown("---")
    st.info("System: Groq Engine Active")
    st.success("Network: Connected")

# --- TOP HEADER ---
st.markdown("<h1 class='main-title'>💠 AgentForge ELITE</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748b; font-size:1.1rem;'>Orchestrating agents for the next generation of thought leadership.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- WORKSPACE ---
left, right = st.columns([1, 1.4], gap="large")

with left:
    st.markdown("#### 🖋️ Core Objective")
    with st.container():
        topic = st.text_area("", placeholder="Define your strategic focus here...", height=120)
        
        st.markdown("#### 🎯 Audience Strategy")
        audience = st.segmented_control("Selection", ["Technical", "Executive", "Creative"], default="Executive")
        
        st.markdown("<br>", unsafe_allow_html=True)
        generate_btn = st.button("EXECUTE ORCHESTRATION")

with right:
    if generate_btn:
        if not topic:
            st.error("Please provide an objective.")
        else:
            with st.status("📡 Agents Analyzing Data...", expanded=True) as status:
                try:
                    # Run CrewAI Logic
                    response = run_crew(topic)
                    st.session_state.final_report = response.raw if hasattr(response, 'raw') else str(response)
                    status.update(label="✅ Intelligence Ready", state="complete", expanded=False)
                except Exception as e:
                    st.error(f"Logic Error: {str(e)}")

    if st.session_state.final_report:
        st.markdown("#### 📑 Strategic Intelligence Output")
        st.markdown(f'<div class="output-box">{st.session_state.final_report}</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Social Distribution Card
        st.markdown("#### 📢 Global Distribution")
        dist_col1, dist_col2 = st.columns(2)
        with dist_col1:
            st.download_button("💾 Download Report", st.session_state.final_report, file_name="AgentForge_Report.md")
        with dist_col2:
            if st.button("🚀 Dispatch to LinkedIn"):
                with st.spinner("Pushing to Make.com..."):
                    payload = {"message": st.session_state.final_report}
                    res = requests.post(MAKE_WEBHOOK_URL, json=payload)
                    if res.status_code == 200:
                        st.success("Dispatched to LinkedIn!")
                        st.balloons()
    else:
        st.markdown("<div style='text-align:center; padding:50px; color:#94a3b8; border:2px dashed #e2e8f0; border-radius:12px;'>Initialize your project on the left to begin analysis.</div>", unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; color: #94a3b8;'>Secure Neural Channel | Powered by Groq & CrewAI</p>", unsafe_allow_html=True)
