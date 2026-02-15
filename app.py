import streamlit as st
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# --- LOAD ENVIRONMENT VARIABLES ---
load_dotenv()

# --- IMPORT YOUR CREW LOGIC ---
# క్రూ లాజిక్ ఇంపోర్ట్ - మనం ఇందాక crew.py లో మార్చిన పేరుతో సింక్ చేశాను
try:
    from crew import run_crew 
except ImportError:
    st.error("🚨 Error: 'crew.py' file not found in the current directory. Please check file names.")

# --- CONFIG & THEME ---
st.set_page_config(
    page_title="AgentForge Elite",
    page_icon="💎",
    layout="wide",
)

# --- WEBHOOK CONFIG ---
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/m4dzevy0jky3h3r86cbrhedvyibjkt8j"

# --- THE ARCHITECT'S PRIVATE STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background: radial-gradient(circle at top right, #1e293b, #0f172a); }
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #2dd4bf);
        color: white; border: none; border-radius: 12px;
        font-weight: 600; padding: 0.6rem 1rem;
        transition: all 0.3s ease; width: 100%;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px rgba(45, 212, 191, 0.4); }
    .output-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px; border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white; line-height: 1.6;
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE FOR DATA PERSISTENCE ---
if 'final_report' not in st.session_state:
    st.session_state.final_report = None

# --- HEADER SECTION ---
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("# 💎 AgentForge <span style='color:#3b82f6; font-size:18px;'>ELITE</span>", unsafe_allow_html=True)
    st.caption("Professional Neural Orchestration & Social Distribution")

with col_h2:
    st.markdown(f'''<div style="text-align:right;"><small style="color:#94a3b8">SESSION ID</small><br><span style="color:#3b82f6; font-weight:bold;">AF-{datetime.now().strftime('%H%M')}</span></div>''', unsafe_allow_html=True)

st.markdown("---")

# --- MAIN WORKSPACE ---
left_col, right_col = st.columns([1, 1.2], gap="large")

with left_col:
    st.markdown("### 🖋️ Research Parameters")
    topic = st.text_input("Project Objective", placeholder="e.g. Impact of Generative AI on Software Engineering")
    audience = st.selectbox("Target Audience", ["Technical", "Executive", "Creative"])
    # Note: audience/length parameters can be passed to run_crew if your function supports them
    generate_btn = st.button("🚀 RUN ORCHESTRATION")

with right_col:
    if generate_btn:
        if not topic:
            st.error("Please define a project focus.")
        else:
            with st.status("📡 Orchestrating Agent Hive...", expanded=True) as status:
                try:
                    # అప్‌గ్రేడ్ చేసిన crew.py నుండి run_crew ని పిలుస్తున్నాం
                    response = run_crew(topic)
                    
                    # CrewAI అవుట్‌పుట్ నుండి పూర్తి టెక్స్ట్ తీయడం
                    st.session_state.final_report = response.raw if hasattr(response, 'raw') else str(response)
                    
                    status.update(label="✅ Analysis Synthesized", state="complete", expanded=False)
                except Exception as e:
                    status.update(label="🚨 Fault Detected", state="error")
                    st.error(f"Execution Error: {str(e)}")

    if st.session_state.final_report:
        st.markdown("### 📑 Intelligence Output")
        st.markdown(f'<div class="output-box">', unsafe_allow_html=True)
        # Markdown లో డిస్ప్లే చేయడం వల్ల బోల్డ్ యూనికోడ్ స్పష్టంగా కనిపిస్తుంది
        st.markdown(st.session_state.final_report)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📢 Social Distribution")
        
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("💾 DOWNLOAD MD", st.session_state.final_report, file_name=f"report_{datetime.now().strftime('%Y%m%d')}.md")
        
        with c2:
            if st.button("🚀 PUBLISH TO LINKEDIN"):
                with st.spinner("Pushing to LinkedIn via Make.com..."):
                    try:
                        # Webhook పంపేటప్పుడు కూడా Unicode భద్రంగా ఉంటుంది
                        payload = {"message": st.session_state.final_report}
                        res = requests.post(MAKE_WEBHOOK_URL, json=payload)
                        
                        if res.status_code == 200:
                            st.success("🎯 Live! Your post has been dispatched to LinkedIn.")
                            st.balloons()
                        else:
                            st.error(f"Failed to publish. Status: {res.status_code}")
                    except Exception as e:
                        st.error(f"Connection Error: {str(e)}")
    else:
        st.info("Awaiting objective initialization to generate intelligence.")

st.markdown("<br><br><p style='text-align: center; color: #475569;'>AgentForge v2.5.0 • Enterprise Shield Active</p>", unsafe_allow_html=True)
