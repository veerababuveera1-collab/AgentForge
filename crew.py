import os
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

# 1. పర్యావరణ వేరియబుల్స్ లోడ్ చేయడం
load_dotenv()

# --- LLM CONFIGURATIONS ---

# High-Performance Model (70b) - క్వాలిటీ రైటింగ్ కోసం
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096
)

# High-Speed Model (8b) - వేగవంతమైన రీసెర్చ్ కోసం
fast_llm = LLM(
    model="groq/llama-3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

def run_crew(topic):
    """
    ఈ ఫంక్షన్ Hybrid సెటప్‌ను రన్ చేస్తుంది:
    - రీసెర్చ్: 8b మోడల్ (Speed & Saving)
    - రైటింగ్: 70b మోడల్ (Quality)
    """
    
    # ఏజెంట్లకు మోడల్స్ కేటాయించడం
    research_agent.llm = fast_llm   
    writer_agent.llm = smart_llm     
    linkedin_agent.llm = smart_llm   

    # Crew అసెంబ్లీ
    crew = Crew(
        agents=[research_agent, writer_agent, linkedin_agent],
        tasks=[
            create_research_task(research_agent, topic),
            create_writing_task(writer_agent),
            create_linkedin_task(linkedin_agent)
        ],
        process=Process.sequential,
        
        # 🚨 ఎర్రర్ రాకుండా ఇక్కడ Embedder ని తీసివేసి డిఫాల్ట్ సెట్ చేశాం
        memory=False, 
        verbose=True,
        cache=True,
        planning=False # OpenAI కీ అవసరం లేకుండా చేస్తుంది
    )

    return crew.kickoff()
