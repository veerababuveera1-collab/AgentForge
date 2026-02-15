import streamlit as st
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# --- LOAD ENVIRONMENT VARIABLES ---
load_dotenv()

# --- IMPORT YOUR CREW LOGIC ---
# ఇక్కడ మీ GitHub లోని crew.py నుండి ఫంక్షన్‌ని ఇంపోర్ట్ చేస్తున్నాం
try:
    from crew import run_crew 
except ImportError as e:
    st.error(f"🚨 Error: 'crew.py' not found or import error: {e}")
    st.info("💡 Hint: Ensure crew.py is in the same folder as app.py in your GitHub repo.")

# --- CONFIG & THEME ---
st.set_page_config(
    page_title="AgentForge Elite",
    page_icon="💎",
    layout="wide",
)

# --- WEBHOOK CONFIG ---
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/m4dzevy0jky3h3r86cbrhedvyibjkt8j"

# --- CSS STYLING ---
st.markdown("""
    <style>
    .output-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px; border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white; line-height: 1.6;
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'final_report' not in st.session_state:
    st.session_state.final_report = None

# --- UI HEADER ---
st.markdown("# 💎 AgentForge ELITE")
st.markdown("---")

# --- MAIN WORKSPACE ---
left_col, right_col = st.columns([1, 1.2], gap="large")

with left_col:
    st.markdown("### 🖋️ Research Parameters")
    topic = st.text_input("Project Objective")
    generate_btn = st.button("🚀 RUN ORCHESTRATION")

with right_col:
    if generate_btn:
        if not topic:
            st.error("Please define a project focus.")
        else:
            with st.status("📡 Orchestrating Agent Hive...", expanded=True) as status:
                try:
                    # Execute Logic
                    response = run_crew(topic)
                    
                    # Store Result
                    st.session_state.final_report = response.raw if hasattr(response, 'raw') else str(response)
                    status.update(label="✅ Analysis Synthesized", state="complete", expanded=False)
                except Exception as e:
                    st.error(f"Execution Error: {str(e)}")

    if st.session_state.final_report:
        st.markdown("### 📑 Intelligence Output")
        st.markdown(f'<div class="output-box">', unsafe_allow_html=True)
        st.markdown(st.session_state.final_report)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # LinkedIn Publish Button
        if st.button("🚀 PUBLISH TO LINKEDIN"):
            # Webhook Logic
            payload = {"message": st.session_state.final_report}
            res = requests.post(MAKE_WEBHOOK_URL, json=payload)
            if res.status_code == 200:
                st.success("🎯 Live on LinkedIn!")
                st.balloons()
