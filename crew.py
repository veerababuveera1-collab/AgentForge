import os
import sys

# 🚨 IMPORTANT: సిగ్నల్/టెలిమెట్రీ ఎర్రర్లను ఆపడానికి ఈ లైన్ ఇంపోర్ట్స్ కంటే ముందే ఉండాలి
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"

from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

# ఎన్విరాన్మెంట్ వేరియబుల్స్ లోడ్ చేయడం
load_dotenv()

# --- LLM CONFIGURATIONS ---

# 1. High-Performance Model (70b) - ఫైనల్ కంటెంట్ క్వాలిటీ కోసం
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096
)

# 2. High-Speed Model (8b) - వేగవంతమైన రీసెర్చ్ కోసం
fast_llm = LLM(
    model="groq/llama-3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

def run_crew(topic):
    """
    హైబ్రిడ్ మోడల్ లాజిక్: 
    రీసెర్చ్ కోసం 8b ని, ప్రొఫెషనల్ రైటింగ్ కోసం 70b ని వాడుతుంది.
    """
    
    # ఏజెంట్లకు మోడల్స్ అసైన్ చేయడం
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
        
        # ఎర్రర్లు రాకుండా ఎంబెడ్డర్ కాన్ఫిగరేషన్ తీసివేసాము
        memory=False, 
        verbose=True,
        cache=True,
        planning=False 
    )

    # టాస్క్ ఎగ్జిక్యూషన్ స్టార్ట్ చేయడం
    return crew.kickoff()
