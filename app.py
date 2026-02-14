import streamlit as st
import os
import sys
import time
from datetime import datetime

# --- IMPORT YOUR CREW LOGIC ---
# మీ crew.py నుండి run_crew ఫంక్షన్‌ను ఇంపోర్ట్ చేస్తున్నాము
from crew import run_crew 

# --- CONFIG & THEME ---
st.set_page_config(
    page_title="AgentForge Elite",
    page_icon="💎",
    layout="wide",
)

# --- THE ARCHITECT'S PRIVATE STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background: radial-gradient(circle at top right, #1e293b, #0f172a); }
    div[data-testid="stVerticalBlock"] > div:has(div.stTextInput) {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 12px;
        border-left: 4px solid #3b82f6;
        margin-bottom: 10px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #2dd4bf);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.4);
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 25px rgba(45, 212, 191, 0.6); }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
col_h1, col_h2, col_h3 = st.columns([2, 1, 1])
with col_h1:
    st.markdown("# 💎 AgentForge <span style='color:#3b82f6; font-size:18px;'>ELITE</span>", unsafe_allow_html=True)
    st.caption("Advanced Neural Orchestration Layer")

with col_h2:
    st.markdown(f'''<div class="metric-card"><small style="color:#94a3b8">SYSTEM UPTIME</small><br><span style="color:#2dd4bf; font-weight:bold;">99.9%</span></div>''', unsafe_allow_html=True)

with col_h3:
    st.markdown(f'''<div class="metric-card"><small style="color:#94a3b8">SESSION ID</small><br><span style="color:#3b82f6; font-weight:bold;">AF-{datetime.now().strftime('%H%M')}</span></div>''', unsafe_allow_html=True)

st.markdown("---")

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛠️ Core Engine")
    api_key = os.getenv("GROQ_API_KEY")
    if api_key: st.info("⚡ Groq Llama-3 Active")
    else: st.error("❌ API Key Missing")
    st.markdown("---")
    st.markdown("### ⚙️ Parameters")
    temp = st.slider("Neural Temp", 0.0, 1.0, 0.7)
    st.markdown("---")
    st.caption(f"Date: {datetime.now().strftime('%Y-%m-%d')}")

# --- MAIN WORKSPACE ---
left_col, right_col = st.columns([1, 1.2], gap="large")

with left_col:
    st.markdown("### 🖋️ Create Brief")
    with st.container():
        topic = st.text_input("Project Objective", placeholder="e.g. AI in Healthcare")
        audience = st.selectbox("Audience", ["Technical", "Executive", "Creative"])
        length = st.selectbox("Scope", ["Briefing", "Detailed Report", "Whitepaper"])
        generate = st.button("RUN ORCHESTRATION")

with right_col:
    if generate:
        if not topic:
            st.error("Missing Objective: Please define a project focus.")
        else:
            with st.status("🚀 Initializing Agent Hive...", expanded=True) as status:
                st.write("📡 Connecting to Groq LPU...")
                
                # --- ACTUAL EXECUTION ---
                try:
                    # ఇక్కడ మనం మీ crew.py లోని run_crew ఫంక్షన్‌ను పిలుస్తున్నాము
                    response = run_crew(topic)
                    
                    # CrewAI 0.28+ వెర్షన్లలో result.raw వాడాలి
                    result = response.raw if hasattr(response, 'raw') else str(response)
                    
                    status.update(label="✅ Analysis Synthesized", state="complete", expanded=False)
                    
                    st.markdown("### 📑 Intelligence Output")
                    st.markdown(f"""
                        <div style="background: rgba(255,255,255,0.05); padding: 25px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.1); color: white;">
                            {result}
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("---")
                    st.download_button("💾 EXPORT AS ASSET", result, file_name=f"agentforge_{datetime.now().strftime('%Y%m%d')}.md")
                
                except Exception as e:
                    status.update(label="🚨 Fault Detected", state="error")
                    st.error(f"Error: {str(e)}")
    else:
        st.markdown("""
            <div style="text-align: center; margin-top: 50px; opacity: 0.5;">
                <img src="https://cdn-icons-png.flaticon.com/512/2593/2593414.png" width="100" style="filter: invert(1);"><br>
                <p>Awaiting Objective Initialization...</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569;'>AgentForge v2.4.0 • Enterprise Shield Active</p>", unsafe_allow_html=True)
