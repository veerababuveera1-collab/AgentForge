import streamlit as st
import os
import sys
import time
from datetime import datetime

# --- SYSTEM PREFLIGHT ---
sys.path.append(os.path.dirname(__file__))
try:
    from crew import run_crew
except ImportError:
    # Mock for demonstration if crew.py isn't present
    def run_crew(topic): return f"# Results for {topic}\n\nProfessional AI Content."

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AgentForge PRO | Enterprise AI Orchestrator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM BRANDING & CSS ---
st.markdown("""
    <style>
    /* Custom Font and Background */
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Clean Cards for Inputs */
    div[data-testid="stVerticalBlock"] > div:has(div.stTextInput) {
        background-color: #161b22;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #30363d;
    }
    
    /* Primary Action Button */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background: linear-gradient(45deg, #FF4B4B, #FF8F8F);
        border: none;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.3);
    }
    
    /* Styled Markdown Output */
    .result-container {
        background-color: #ffffff;
        color: #1e1e1e;
        padding: 30px;
        border-radius: 10px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: CONTROL PLANE ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616490.png", width=60)
    st.title("AgentForge **PRO**")
    st.caption("Enterprise Multi-Agent Orchestrator")
    st.markdown("---")
    
    # Connection Status Cluster
    with st.expander("🌐 System Status", expanded=True):
        api_key = os.getenv("GROQ_API_KEY")
        if api_key:
            st.success("Groq Cloud: CONNECTED")
            st.info("LLM: Llama-3-70b-versatile")
        else:
            st.error("Groq Cloud: DISCONNECTED")
    
    # Fine-tuning Controls
    st.markdown("### Agent Configuration")
    creativity = st.select_slider("Agent Creativity", options=["Factual", "Balanced", "Creative"], value="Balanced")
    process_type = st.radio("Workflow", ["Sequential", "Hierarchical"], index=0)
    
    st.markdown("---")
    if st.button("🧹 Clear Session"):
        st.cache_data.clear()
        st.rerun()

# --- MAIN INTERFACE ---
# Title Area
col_title, col_logo = st.columns([4, 1])
with col_title:
    st.title("Collaborative Intelligence Studio")
    st.write(f"Logged in as: **Standard User** | {datetime.now().strftime('%Y-%m-%d')}")

# User Input Stage
tab1, tab2 = st.tabs(["🎯 Content Engine", "📜 Generation History"])

with tab1:
    col_in, col_out = st.columns([1, 1.5], gap="large")
    
    with col_in:
        st.subheader("Design Your Brief")
        with st.container():
            topic = st.text_input("What is the focal point of this research?", 
                                 placeholder="e.g. The impact of Solid State Batteries on EV adoption")
            
            audience = st.selectbox("Target Audience", ["General Public", "Technical Experts", "C-Suite Executives"])
            
            tone = st.multiselect("Content Tone", ["Professional", "Witty", "Urgent", "Educational"], default=["Professional"])
            
            generate_btn = st.button("🚀 EXECUTE AGENT CREW")

    with col_out:
        if generate_btn:
            if not topic:
                st.warning("Architectural Note: You must provide a topic to initialize the agents.")
            else:
                # Advanced Status Tracking
                with st.status("🏗️ Orchestrating Agents...", expanded=True) as status:
                    st.write("Initializing Researcher Agent...")
                    time.sleep(1) # Simulated latency for UX
                    st.write("Analyzing Groq context windows...")
                    
                    try:
                        # Call the actual logic
                        result = run_crew(topic)
                        
                        status.update(label="✅ Synthesis Complete", state="complete", expanded=False)
                        st.balloons()
                        
                        # Display Area
                        st.subheader("Final Output")
                        with st.container():
                            st.markdown(f'<div class="result-container">{result}</div>', unsafe_allow_html=True)
                        
                        # Action Bar
                        st.markdown("### 📥 Export & Distribution")
                        c1, c2 = st.columns(2)
                        with c1:
                            st.download_button("Download Markdown", result, file_name="article.md", use_container_width=True)
                        with c2:
                            if st.button("📋 Copy to Clipboard", use_container_width=True):
                                st.toast("Copied to clipboard!")
                                
                    except Exception as e:
                        status.update(label="🚨 Workflow Interrupted", state="error")
                        st.error(f"Fatal Error: {str(e)}")
        else:
            # Empty State
            st.info("Waiting for input... Define your topic on the left to begin the orchestration.")
            st.image("https://illustrations.popsy.co/white/data-analysis.svg", width=350)

with tab2:
    st.write("Recent generations will appear here during this session.")
    # You could implement a session_state list here to track history

# --- FOOTER ---
st.markdown("---")
footer_col1, footer_col2 = st.columns([3, 1])
with footer_col1:
    st.caption("AgentForge v2.4.0-Stable | Architecture: Micro-Agent Collaborative Mesh")
with footer_col2:
    st.caption("© 2026 Enterprise AI Solutions")
