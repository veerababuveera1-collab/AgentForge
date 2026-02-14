from crewai import Crew, Process
from crewai.llm import LLM
import os

# agents.py మరియు tasks.py నుండి ఫంక్షన్లను ఇంపోర్ట్ చేస్తున్నాము
try:
    from agents import (
        create_research_agent, 
        create_writer_agent, 
        create_linkedin_manager_agent
    )
    from tasks import (
        create_research_task, 
        create_writing_task, 
        create_linkedin_task
    )
except ImportError as e:
    print(f"Error: Make sure agents.py and tasks.py exist in the same folder. {e}")

def run_crew(topic: str) -> str:
    """
    రిసెర్చ్, రైటింగ్ మరియు లింక్డ్‌ఇన్ ఫార్మాటింగ్ ప్రక్రియను నిర్వహిస్తుంది.
    """
    
    # 1. LLM Configuration (Groq Llama 3.1)
    # base_url జోడించడం వల్ల OpenAI ఎర్రర్ రాదు
    llm = LLM(
        model="groq/llama-3.1-8b-instant", # వేగవంతమైన రెస్పాన్స్ కోసం
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1", # ఇది తప్పనిసరి
        temperature=0.5, # టోకెన్ వాడకం తగ్గించడానికి
        max_tokens=2048
    )

    # 2. ఏజెంట్ల తయారీ
    researcher = create_research_agent(llm)
    writer = create_writer_agent(llm)
    linkedin_manager = create_linkedin_manager_agent(llm)

    # 3. టాస్క్‌ల తయారీ
    research_task = create_research_task(researcher, topic)
    writing_task = create_writing_task(writer)
    linkedin_task = create_linkedin_task(linkedin_manager)

    # 4. Crew Formation
    crew = Crew(
        agents=[researcher, writer, linkedin_manager],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential, 
        verbose=True,                
        memory=True,                 
        cache=True                   
    )

    try:
        # 5. Execution
        print(f"🚀 Launching Crew for topic: {topic}")
        result = crew.kickoff()
        
        # CrewAI 0.28+ వెర్షన్లలో 'raw' అవుట్‌పుట్‌ను పంపుతాము
        return result.raw if hasattr(result, 'raw') else str(result)
        
    except Exception as e:
        # Rate limit వస్తే 20 సెకన్లు ఆగమని సూచిస్తుంది
        if "rate_limit" in str(e).lower():
            return "Error: Groq Rate Limit reached. Please wait 20 seconds and try again."
        return f"Error in Crew Execution: {str(e)}"

if __name__ == "__main__":
    test_topic = "Future of AI Agents"
    print(run_crew(test_topic))
