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
    st.error("🚨 System Breach: 'crew.py' connection lost.")

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AgentForge | Command Center",
    page_icon="⚡",
    layout="wide",
)

# --- WEBHOOK ---
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/m4dzevy0jky3h3r86cbrhedvyibjkt8j"

# --- THE "MIDNIGHT EMERALD" UI STYLING ---
st.markdown("""
    <style>
    /* Dark Slate Background */
    .main {
        background-color: #050505;
        color: #e0e0e0;
    }

    /* Neon Emerald Borders for Cards */
    .stMetric, .output-box, .input-section {
        background: #0a0a0a;
        border: 1px solid #10b981;
        border-radius: 4px;
        padding: 20px;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.1);
        margin-bottom: 20px;
    }

    /* Glowing Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 2px solid #10b981;
    }

    /* Terminal Style Buttons */
    div.stButton > button:first-child {
        background: transparent;
        color: #10b981;
        border: 2px solid #10b981;
        border-radius: 0px;
        font-family: 'Courier New', monospace;
        text-transform: uppercase;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: #10b981;
        color: #000000;
        box-shadow: 0 0 20px #10b981;
    }

    /* Typography */
    h1, h2, h3 {
        font-family: 'Courier New', monospace;
        color: #10b981 !important;
        letter-spacing: 2px;
    }

    /* Output Area */
    .output-box {
        font-family: 'Inter', sans-serif;
        background-color: #0d0d0d;
        color: #10b981;
        line-height: 1.6;
        border-left: 5px solid #10b981;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: #050505; }
    ::-webkit-scrollbar-thumb { background: #10b981; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR COMMANDS ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>CORE</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("🛰️ **SATELLITE:** CONNECTED")
    st.write("🧠 **NEURAL ENGINE:** GROQ-v3")
    st.write("🔐 **ENCRYPTION:** AES-256")
    st.markdown("---")
    
    # Quick Action
    if st.button("RESET SYSTEM"):
        st.session_state.final_report = None
        st.rerun()

# --- MAIN INTERFACE ---
st.markdown("<h1>⚡ AGENTFORGE : COMMAND CENTER</h1>", unsafe_allow_html=True)
st.caption(f"SYSTEM TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | STATUS: SECURE")
st.markdown("<br>", unsafe_allow_html=True)

col_input, col_output = st.columns([1, 1.5], gap="medium")

with col_input:
    st.markdown("### [ INPUT_OBJECTIVE ]")
    topic = st.text_area("", placeholder="Enter Mission Parameters...", height=150)
    
    st.markdown("### [ TONE_PROTOCOL ]")
    tone = st.radio("Choose Protocol", ["Aggressive Growth", "Philosophical", "Strategic Alpha"], horizontal=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("RUN EXECUTION"):
        if topic:
            with st.status("Initializing Agent Swarm...", expanded=True) as status:
                try:
                    response = run_crew(topic)
                    st.session_state.final_report = response.raw if hasattr(response, 'raw') else str(response)
                    status.update(label="PROTOCOL COMPLETE", state="complete")
                except Exception as e:
                    st.error(f"FATAL ERROR: {e}")
        else:
            st.warning("⚠️ Objective required.")

with col_output:
    st.markdown("### [ INTELLIGENCE_FEED ]")
    if st.session_state.final_report:
        st.markdown(f'<div class="output-box">{st.session_state.final_report}</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 EXPORT DATA", st.session_state.final_report, file_name="INTEL_REPORT.md")
        with c2:
            if st.button("📡 BROADCAST TO LINKEDIN"):
                payload = {"message": st.session_state.final_report}
                res = requests.post(MAKE_WEBHOOK_URL, json=payload)
                if res.status_code == 200:
                    st.toast("BROADCAST SUCCESSFUL")
                    st.balloons()
    else:
        st.info("Awaiting input data for neural processing...")

st.markdown("<br><br><p style='text-align: center; color: #333;'>SYSTEM-UID: " + os.getenv("GROQ_API_KEY")[:8] + "XXXX-AGENTFORGE</p>", unsafe_allow_html=True)
