import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from crew import run_crew

# Page Configuration
st.set_page_config(
    page_title="AgentForge",
    page_icon="🚀",
    layout="centered"
)

# UI Header
st.title("🚀 AgentForge – Multi-Agent AI Blog Generator")
st.write("Generate AI-powered research and blog content using collaborative agents.")

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Validate API key
if not api_key:
    st.error("❌ OPENAI_API_KEY not found. Please configure your .env file.")
    st.stop()

# User Input
topic = st.text_input("Enter Topic")

# Generate Button
if st.button("Generate"):
    if not topic:
        st.warning("⚠️ Please enter a topic.")
    else:
        with st.spinner("🤖 Agents are working..."):
            try:
                result = run_crew(topic)

                st.success("✅ Content Generated Successfully!")
                st.markdown("---")
                st.markdown(result)

            except Exception as e:
                st.error(f"🚨 Error occurred: {e}")
