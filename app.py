import streamlit as st
import os
import sys

# Fix import path for Streamlit Cloud
sys.path.append(os.path.dirname(__file__))

from crew import run_crew

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AgentForge",
    page_icon="🚀",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.title("🚀 AgentForge")
st.subheader("Multi-Agent AI Blog Generator")
st.write(
    "Generate AI-powered research and structured blog content "
    "using collaborative CrewAI agents."
)

st.markdown("---")

# -----------------------------
# API Key Check
# -----------------------------
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY not found. Please configure it in Streamlit Secrets.")
    st.stop()

# -----------------------------
# Input Section
# -----------------------------
topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Artificial Intelligence in Healthcare"
)

if st.button("Generate Content"):

    if not topic.strip():
        st.warning("⚠️ Please enter a valid topic.")
    else:
        with st.spinner("🤖 Agents are collaborating..."):
            try:
                result = run_crew(topic)

                st.success("✅ Content Generated Successfully!")

                st.markdown("---")
                st.markdown(result)

            except Exception as e:
                st.error(f"🚨 Error: {str(e)}")

st.markdown("---")
st.caption("Built with CrewAI + Streamlit | AgentForge")
