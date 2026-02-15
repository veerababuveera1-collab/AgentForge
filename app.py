import streamlit as st
import os
import requests
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# --- 1. పర్యావరణ వేరియబుల్స్ లోడ్ చేయడం ---
load_dotenv()

# --- 2. ఇంపోర్ట్ పాత్ ఫిక్స్ (Neural Bridge Fix) ---
# ఇది app.py ఉన్న ఫోల్డర్‌ను వెతికి crew.pyని కనెక్ట్ చేస్తుంది
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
if str(current_dir) not in sys.path:
    sys.path.append(str(current_dir))

# --- 3. BACKEND LOGIC IMPORT ---
try:
    from crew import run_crew 
    bridge_status = True
except Exception as e:
    bridge_status = False
    error_detail = str(e)

# --- 4. PAGE CONFIG ---
st.set_page_config(
    page_title="AgentForge Elite | AI Command Center",
    page_icon="💎",
    layout="wide",
)

# --- 5. MAKE.COM WEBHOOK URL ---
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/m4dzevy0jky3h3r86cbrhedvyibjkt8j"

# --- 6. CUSTOM CSS (PREMIUM DARK THEME) ---
st.markdown("""
    <style>
    .main { background: #080a0f; color: #ffffff; }
    .stApp { background: radial-gradient(circle at 50% 50%, #111827 0%, #080a0f 100%); }
    
    .agent-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(59, 130, 246, 0.4);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
    }
    
    .output-container {
        background: #0d1117;
        border-radius: 10px;
        padding: 20px;
        border-left: 5px solid #3b82f6;
        font-family: 'Inter', sans-serif;
        line-height: 1.7;
        color: #e6edf3;
        white-space: pre-wrap;
    }
    
    div.stButton > button {
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        color: white; border: none; border-radius: 8px;
        font-weight: bold; width: 100%; height: 3.5em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 7. SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.title("Elite Control")
    st.markdown("---")
    if bridge_status:
        st.success("🛰️ Neural Bridge: ONLINE")
    else:
        st.error("🚨 Neural Bridge: OFFLINE")
        st.caption(f"Error: {error_detail}")
    
    st.info("Core: Llama-3.3-70B")
    if st.button("🔄 RESET SESSION"):
        st.session_state.final_report = None
        st.rerun()

# --- 8. HEADER ---
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>⚡ AGENTFORGE <span style='color:white;'>ELITE</span></h1>", unsafe_allow_html=True)

# --- 9. AGENT MONITOR ---
st.markdown("### 📡 Active Neural Agents")
p1, p2, p3 = st.columns(3)
status_color = "#10b981" if bridge_status else "#ef4444"
status_text = "Ready" if bridge_status else "Offline"

p1.markdown(f'<div class="agent-card"><b>🔍 Researcher (8B)</b><br><span style="color:{status_color}">{status_text}</span></div>', unsafe_allow_html=True)
p2.markdown(f'<div class="agent-card"><b>✍️ Architect (70B)</b><br><span style="color:{status_color}">{status_text}</span></div>', unsafe_allow_html=True)
p3.markdown(f'<div class="agent-card"><b>📢 Strategist (70B)</b><br><span style="color:{status_color}">{status_text}</span></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 10. MAIN WORKSPACE ---
col_left, col_right = st.columns([1, 1.5], gap="large")

with col_left:
    st.markdown("### 🖋️ Objective")
    topic = st.text_area("What is the mission topic?", placeholder="e.g. AI in Healthcare 2026...", height=150)
    
    if st.button("🚀 INITIATE SWARM"):
        if not bridge_status:
            st.error("Cannot start: Backend is offline. Check error in sidebar.")
        elif not topic:
            st.warning("Please define a topic.")
        else:
            with st.status("🔗 Swarm Agents Activating...", expanded=True) as status:
                try:
                    response = run_crew(topic)
                    st.session_state.final_report = response.raw if hasattr(response, 'raw') else str(response)
                    status.update(label="✅ Synthesis Complete!", state="complete", expanded=False)
                except Exception as e:
                    st.error(f"Execution Error: {str(e)}")

with col_right:
    st.markdown("### 📑 Intelligence Feed")
    if 'final_report' in st.session_state and st.session_state.final_report:
        st.markdown(f'<div class="output-container">{st.session_state.final_report}</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        d1, d2 = st.columns(2)
        with d1:
            st.download_button("📥 DOWNLOAD", st.session_state.final_report, file_name="Report.txt")
        with d2:
            if st.button("📡 DISPATCH TO WEBHOOK"):
                res = requests.post(MAKE_WEBHOOK_URL, json={"content": st.session_state.final_report, "topic": topic})
                if res.status_code == 200:
                    st.success("Sent to Make.com!")
                    st.balloons()
    else:
        st.markdown("<div style='text-align:center; padding-top:100px; color:#4b5563; border: 1px dashed #30363d; border-radius:12px; height:300px; display:flex; align-items:center; justify-content:center;'>Awaiting Mission Authorization...</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption(f"© {datetime.now().year} AgentForge Elite v4.5")
