import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

# 1. Load Environment Variables (API Keys)
load_dotenv()

# Streamlit Page UI Settings
st.set_page_config(page_title="AgentForge ELITE", page_icon="⚡", layout="wide")
st.title("⚡ AgentForge ELITE")
st.markdown("*Professional AI Content Orchestration for LinkedIn*")

# 2. LLM Configuration (FIX: Increased max_tokens to prevent content loss)
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096,  # 👈 ముఖ్యమైన మార్పు: దీనివల్ల కంటెంట్ అసంపూర్తిగా ఆగదు
    max_retries=5
)

def run_agentic_workflow(topic):
    # Assign the upgraded LLM to all agents
    research_agent.llm = smart_llm
    writer_agent.llm = smart_llm
    linkedin_agent.llm = smart_llm

    # Initialize Tasks
    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)
    linkedin_task = create_linkedin_task(linkedin_agent)

    # Crew Assembly (Memory is set to False for Streamlit stability)
    crew = Crew(
        agents=[research_agent, writer_agent, linkedin_agent],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential,
        memory=False, 
        verbose=True,
        cache=True
    )

    return crew.kickoff()

# 3. Streamlit GUI Elements
with st.sidebar:
    st.header("Settings")
    st.info("Using Model: Llama-3.3-70b (Groq)")
    if not os.getenv("GROQ_API_KEY"):
        st.error("⚠️ GROQ_API_KEY not found in .env!")

topic_input = st.text_input("Enter Topic / Project Objective:", "The Emergence of Agent-First Architecture")

if st.button("🚀 Run Orchestration"):
    if topic_input:
        with st.status("Agents are coordinating...", expanded=True) as status:
            try:
                st.write("🔍 Researching technical patterns...")
                # Start the workflow
                result = run_agentic_workflow(topic_input)
                
                status.update(label="✅ Content Generation Complete!", state="complete", expanded=False)
                
                # Display Output
                st.divider()
                st.subheader("Your Elite LinkedIn Post")
                
                # st.markdown handles the bold unicode perfectly
                st.markdown(result.raw)
                
                # Easy Copy Section
                st.divider()
                st.write("📋 **Copy for LinkedIn:**")
                st.text_area(label="", value=result.raw, height=450)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a topic first.")
