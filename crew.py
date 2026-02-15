import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

# 1. పర్యావరణ వేరియబుల్స్ లోడ్ చేయడం
load_dotenv()

# స్ట్రీమ్‌లిట్ UI సెట్టింగ్స్
st.set_page_config(page_title="AgentForge ELITE", page_icon="💎", layout="wide")
st.title("💎 AgentForge ELITE")
st.markdown("*Professional Neural Orchestration & Social Distribution*")

# 2. LLM కాన్ఫిగరేషన్ (కంటెంట్ మిస్ అవ్వకుండా max_tokens పెంచాం)
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096,  # 👈 కంటెంట్ మధ్యలో ఆగిపోకుండా ఉండటానికి ఇది కీలకం
    max_retries=5
)

def run_agentic_workflow(topic):
    # ఏజెంట్లకు అప్‌గ్రేడ్ చేసిన LLMని కేటాయించడం
    research_agent.llm = smart_llm
    writer_agent.llm = smart_llm
    linkedin_agent.llm = smart_llm

    # టాస్క్‌లను ఇనిషియలైజ్ చేయడం
    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)
    linkedin_task = create_linkedin_task(linkedin_agent)

    # Crew అసెంబ్లీ
    crew = Crew(
        agents=[research_agent, writer_agent, linkedin_agent],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential,
        memory=False, # స్ట్రీమ్‌లిట్ స్థిరత్వం కోసం ప్రస్తుతానికి False
        verbose=True,
        cache=True
    )

    return crew.kickoff()

# 3. స్ట్రీమ్‌లిట్ GUI ఎలిమెంట్స్
topic_input = st.text_input("Project Objective:", "The Emergence of Agent-First Architecture")

if st.button("🚀 RUN ORCHESTRATION"):
    if topic_input:
        with st.status("Neural agents are coordinating...", expanded=True) as status:
            try:
                st.write("🔍 Identifying industry-standard statistics...")
                # వర్క్‌ఫ్లో ప్రారంభం
                result = run_agentic_workflow(topic_input)
                
                status.update(label="✅ Intelligence Generated!", state="complete", expanded=False)
                
                # అవుట్‌పుట్ ప్రదర్శన
                st.divider()
                st.subheader("Your Upgraded LinkedIn Post")
                
                # స్ట్రీమ్‌లిట్ మార్క్‌డౌన్ మీ బోల్డ్ యూనికోడ్‌ను పర్ఫెక్ట్‌గా చూపిస్తుంది
                st.markdown(result.raw)
                
                # ఈజీ కాపీ సెక్షన్
                st.divider()
                st.write("📋 **Copy the content below:**")
                st.text_area(label="", value=result.raw, height=450)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a project objective.")
