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
st.subheader("Multi-Agent AI Blog Generator (Powered by Groq)")
st.write(
    "Generate AI-powered research and structured blog content "
    "using collaborative CrewAI agents running on Groq."
)

st.markdown("---")

# -----------------------------
# API Key Check (Groq)
# -----------------------------
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ_API_KEY not found. Please configure it in Streamlit Secrets.")
    st.stop()

# -----------------------------
# User Input
# -----------------------------
topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Artificial Intelligence in Healthcare"
)

generate_button = st.button("Generate Content")

# -----------------------------
# Execution Section
# -----------------------------
if generate_button:

    if not topic.strip():
        st.warning("⚠️ Please enter a valid topic.")
    else:
        with st.spinner("🤖 Agents are collaborating with Groq..."):
            try:
                result = run_crew(topic)

                st.success("✅ Content Generated Successfully!")

                st.markdown("---")

                with st.expander("📄 View Generated Content", expanded=True):
                    st.markdown(result)

            except Exception as e:
                st.error(f"🚨 Error occurred: {str(e)}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built with CrewAI + Groq + Streamlit | AgentForge")
