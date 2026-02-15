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
    st.error("🚨 Error: 'crew.py' not found.")

# --- CONFIG & THEME ---
st.set_page_config(
    page_title="AgentForge Elite | AI Orchestrator",
    page_icon="💎",
    layout="wide",
)

# --- WEBHOOK CONFIG ---
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/m4dzevy0jky3h3r86cbrhedvyibjkt8j"

# --- ADVANCED PROFESSIONAL STYLING (THE ARCHITECT'S UI) ---
st.markdown("""
    <style>
    /* Global Background */
    .main { background-color: #0f172a; color: #f8fafc; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }

    /* Glassmorphism Cards */
    .stMetric, .output-box, .status-container {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }

    /* Professional Button Styling */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.5);
    }

    /* Heading Styling */
    h1, h2, h3 { color: #f1f5f9 !important; font-weight: 700 !important; }
    .highlight { color: #3b82f6; font-weight: bold; }

    /* Custom Output Box */
    .output-box {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        line-height: 1.8;
        color: #e2e8f0;
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (CONTROL PANEL) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.title("Control Panel")
    st.markdown("---")
    
    st.subheader("⚙️ System Status")
    st.success("Groq Engine: Online")
    st.success("LinkedIn Webhook: Active")
    
    st.markdown("---")
    st.caption(f"Server ID: AF-{datetime.now().strftime('%d%m%H%M')}")
    st.caption("Version 3.0.1 (Elite Edition)")

# --- MAIN HEADER ---
st.markdown("# 💎 AgentForge <span class='highlight'>ELITE</span>", unsafe_allow_html=True)
st.markdown("#### *Enterprise Neural Orchestration for Executive Branding*")
st.markdown("---")

# --- LAYOUT: INPUT & OUTPUT ---
col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.markdown("### 🖋️ Intelligence Request")
    with st.container():
        topic = st.text_area("What is the core objective?", placeholder="e.g., The Future of Multi-Agent Systems in Fintech", height=100)
        
        c1, c2 = st.columns(2)
        with c1:
            audience = st.selectbox("Target Tone", ["Technical Excellence", "Executive Leadership", "Creative Visionary"])
        with c2:
            length = st.selectbox("Complexity", ["Concise Post", "Deep Dive", "Standard"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        generate_btn = st.button("🚀 EXECUTE ORCHESTRATION")

with col2:
    if generate_btn:
        if not topic:
            st.warning("⚠️ Objective cannot be empty.")
        else:
            with st.status("📡 Agents are synthesizing intelligence...", expanded=True) as status:
                try:
                    # Run Crew
                    response = run_crew(topic)
                    st.session_state.final_report = response.raw if hasattr(response, 'raw') else str(response)
                    status.update(label="✅ Synthesis Complete", state="complete", expanded=False)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # Intelligence Display Area
    if st.session_state.final_report:
        st.markdown("### 📑 Intelligence Report")
        st.markdown(f'<div class="output-box">{st.session_state.final_report}</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📢 Distribution Hub")
        
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            st.download_button("💾 Export to Markdown", st.session_state.final_report, file_name="AF_Report.md")
        
        with d_col2:
            if st.button("🚀 DISPATCH TO LINKEDIN"):
                with st.spinner("Pushing to LinkedIn..."):
                    payload = {"message": st.session_state.final_report}
                    res = requests.post(MAKE_WEBHOOK_URL, json=payload)
                    if res.status_code == 200:
                        st.balloons()
                        st.success("🎯 Dispatched Successfully!")
    else:
        # Placeholder when no content is present
        st.info("Awaiting input to generate strategic intelligence.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>© 2026 AgentForge Enterprise | Secure Neural Channel Active</p>", unsafe_allow_html=True)
