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
    st.error("🚨 Neural Bridge Offline. Check crew.py")

# --- CONFIG ---
st.set_page_config(page_title="AgentForge Studio", page_icon="⚡", layout="wide")

# --- STYLING (THE VISIONARY LOOK) ---
st.markdown("""
    <style>
    .main { background: #0b0e14; color: #ffffff; }
    .agent-status {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid #3b82f6;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        font-size: 0.8rem;
    }
    .output-container {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 25px;
        color: #e6edf3;
        font-family: 'Inter', sans-serif;
    }
    .img-placeholder {
        height: 300px;
        border: 2px dashed #30363d;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: #0d1117;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚡ CONTROL")
    st.markdown("---")
    st.toggle("High Quality Renders", value=True)
    st.toggle("Auto-Post to Socials", value=False)
    st.markdown("---")
    st.info("Engine: Groq Llama-3.3")

# --- HEADER ---
st.markdown("<h1 style='color:#3b82f6;'>AGENTFORGE <span style='color:white;'>VISUAL STUDIO</span></h1>", unsafe_allow_html=True)
st.markdown("---")

# --- UI LAYOUT ---
col_input, col_output = st.columns([1, 1.5], gap="large")

with col_input:
    st.subheader("🖋️ Content Mission")
    topic = st.text_area("What is the core message?", placeholder="e.g., The rise of AI in Sustainable Energy", height=100)
    
    # Agent Pulse Monitor
    st.markdown("#### 📡 Agent Pulse")
    p1, p2, p3 = st.columns(3)
    p1.markdown('<div class="agent-status">Researcher<br>● Ready</div>', unsafe_allow_html=True)
    p2.markdown('<div class="agent-status">Architect<br>● Ready</div>', unsafe_allow_html=True)
    p3.markdown('<div class="agent-status">Visionary<br>● Ready</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 EXECUTE SYNTHESIS"):
        if topic:
            with st.status("Agents Interfacing...", expanded=True) as status:
                try:
                    response = run_crew(topic)
                    st.session_state.final_report = response.raw if hasattr(response, 'raw') else str(response)
                    status.update(label="SUCCESS: Intelligence Synthesized", state="complete")
                except Exception as e:
                    st.error(f"Execution Error: {e}")

with col_output:
    if 'final_report' in st.session_state and st.session_state.final_report:
        tab1, tab2 = st.tabs(["📝 Content Report", "🖼️ Visual Studio"])
        
        with tab1:
            st.markdown(f'<div class="output-container">{st.session_state.final_report}</div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("💾 Save Report", st.session_state.final_report)
            with c2:
                if st.button("📡 Dispatch to LinkedIn"):
                    st.toast("Transmitting via Webhook...")
                    # logic: requests.post(MAKE_WEBHOOK_URL, json={"message": st.session_state.final_report})

        with tab2:
            st.subheader("Visual Asset Generation")
            st.markdown("Generate a custom high-fidelity image based on your content.")
            
            # ఇక్కడ మనం ఒక ఇమేజ్ ప్రాంప్ట్ తయారు చేస్తున్నాం
            image_prompt = f"Professional 3D render, futuristic style, related to: {topic[:50]}"
            st.text_input("Generated Prompt", value=image_prompt)
            
            if st.button("🎨 GENERATE VISUAL (Nano Banana)"):
                with st.spinner("Synthesizing Visuals..."):
                    # Note: ఇక్కడ మనం భవిష్యత్తులో మీ ఇమేజ్ జనరేషన్ API ని కనెక్ట్ చేయవచ్చు
                    st.markdown('<div class="img-placeholder">Image Generation Engine Connecting...</div>', unsafe_allow_html=True)
                    st.info("I can help you generate images (quota: 100/day). Would you like me to create a specific image for this content now?")
    else:
        st.markdown("<div style='height:400px; display:flex; align-items:center; justify-content:center; border:1px dashed #30363d; border-radius:12px; color:#484f58;'>Awaiting Neural Authorization to begin...</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("AgentForge v4.5 | Proprietary Neural Orchestration for Veera Babu")
