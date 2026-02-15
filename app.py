import streamlit as st
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# --- పర్యావరణ వేరియబుల్స్ లోడ్ చేయడం ---
load_dotenv()

# --- BACKEND LOGIC IMPORT ---
try:
    from crew import run_crew 
except ImportError:
    st.error("🚨 Neural Bridge Offline. Check if 'crew.py' is in the same folder.")

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AgentForge Elite | AI Command Center",
    page_icon="💎",
    layout="wide",
)

# --- MAKE.COM WEBHOOK URL ---
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/m4dzevy0jky3h3r86cbrhedvyibjkt8j"

# --- CUSTOM CSS (PREMIUM DARK THEME) ---
st.markdown("""
    <style>
    .main { background: #080a0f; color: #ffffff; }
    .stApp { background: radial-gradient(circle at 50% 50%, #111827 0%, #080a0f 100%); }
    
    /* Neon Status Cards */
    .agent-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(59, 130, 246, 0.4);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        transition: 0.3s;
    }
    .agent-card:hover { border-color: #3b82f6; box-shadow: 0 0 15px rgba(59, 130, 246, 0.2); }
    
    /* Terminal Style Output */
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
    
    /* Premium Button */
    div.stButton > button {
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        color: white; border: none; border-radius: 8px;
        font-weight: bold; width: 100%; height: 3.5em;
        text-transform: uppercase; letter-spacing: 1px;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTROL PANEL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.title("Elite Control")
    st.markdown("---")
    st.success("Core: Llama-3.3-70B")
    st.info("Status: Optimized")
    st.markdown("---")
    if st.button("🔄 RESET SESSION"):
        st.session_state.final_report = None
        st.rerun()

# --- HEADER SECTION ---
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>⚡ AGENTFORGE <span style='color:white;'>ELITE</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Advanced Autonomous Intelligence & Content Synthesis</p>", unsafe_allow_html=True)

# --- REAL-TIME AGENT MONITOR ---
st.markdown("### 📡 Active Neural Agents")
p1, p2, p3 = st.columns(3)
p1.markdown('<div class="agent-card"><b>🔍 Researcher (8B)</b><br><span style="color:#10b981">Ready</span></div>', unsafe_allow_html=True)
p2.markdown('<div class="agent-card"><b>✍️ Architect (70B)</b><br><span style="color:#10b981">Ready</span></div>', unsafe_allow_html=True)
p3.markdown('<div class="agent-card"><b>📢 Strategist (70B)</b><br><span style="color:#10b981">Ready</span></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- MAIN WORKSPACE ---
col_left, col_right = st.columns([1, 1.5], gap="large")

with col_left:
    st.markdown("### 🖋️ Objective")
    topic = st.text_area("What is the mission topic?", placeholder="Enter keywords or a full sentence...", height=150)
    
    st.markdown("#### ⚙️ Settings")
    tone = st.selectbox("Tone of Voice", ["Professional", "Provocative", "Educational", "Minimalist"])
    
    if st.button("🚀 INITIATE SWARM"):
        if not topic:
            st.warning("Please define a topic before execution.")
        else:
            with st.status("🔗 Connecting to Neural Swarm...", expanded=True) as status:
                try:
                    # Run the Backend Crew
                    response = run_crew(topic)
                    # Store result in session state
                    st.session_state.final_report = response.raw if hasattr(response, 'raw') else str(response)
                    status.update(label="✅ Synthesis Complete!", state="complete", expanded=False)
                except Exception as e:
                    st.error(f"Execution Error: {str(e)}")

with col_right:
    st.markdown("### 📑 Intelligence Feed")
    if 'final_report' in st.session_state and st.session_state.final_report:
        # Display the result in a nice container
        st.markdown(f'<div class="output-container">{st.session_state.final_report}</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Action Buttons
        d1, d2 = st.columns(2)
        with d1:
            st.download_button("📥 DOWNLOAD REPORT", st.session_state.final_report, file_name=f"Intel_{datetime.now().strftime('%Y%m%d')}.txt")
        with d2:
            if st.button("📡 DISPATCH TO WEBHOOK"):
                with st.spinner("Broadcasting..."):
                    try:
                        res = requests.post(MAKE_WEBHOOK_URL, json={"content": st.session_state.final_report, "topic": topic})
                        if res.status_code == 200:
                            st.success("Successfully Sent to Make.com!")
                            st.balloons()
                        else:
                            st.error("Failed to Dispatch. Check Webhook.")
                    except Exception as e:
                        st.error(f"Error: {e}")
    else:
        st.markdown("<div style='text-align:center; padding-top:100px; color:#4b5563; border: 1px dashed #30363d; border-radius:12px; height:300px; display:flex; align-items:center; justify-content:center;'>Awaiting Intelligence Input...</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption(f"© {datetime.now().year} AgentForge Elite v4.5 | Optimized for Veera Babu")
