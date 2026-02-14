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
    llm = LLM(
        model="groq/llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7,
        max_tokens=4096
    )

    # 2. ఏజెంట్ల తయారీ (Initializing Agents)
    researcher = create_research_agent(llm)
    writer = create_writer_agent(llm)
    linkedin_manager = create_linkedin_manager_agent(llm)

    # 3. టాస్క్‌ల తయారీ (Initializing Tasks)
    # గమనిక: టాస్క్‌లు ఒకదానిపై ఒకటి ఆధారపడి ఉంటాయి (Contextual flow)
    research_task = create_research_task(researcher, topic)
    writing_task = create_writing_task(writer)
    linkedin_task = create_linkedin_task(linkedin_manager)

    # 4. Crew Formation (The Orchestrator)
    # Sequential process అంటే ఒక ఏజెంట్ పని పూర్తి చేసాకే మరొకరు మొదలుపెడతారు.
    crew = Crew(
        agents=[researcher, writer, linkedin_manager],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential, 
        verbose=True,                # టెర్మినల్‌లో ఏజెంట్ల ఆలోచనలు కనిపిస్తాయి
        memory=True,                 # ఏజెంట్లు మునుపటి పనులను గుర్తుంచుకుంటారు
        cache=True                   # ఒకే రకమైన సమాచారాన్ని వేగంగా ప్రాసెస్ చేస్తుంది
    )

    try:
        # 5. Execution (Kickoff the process)
        print(f"🚀 Launching Crew for topic: {topic}")
        result = crew.kickoff()
        
        # CrewAI 0.28+ వెర్షన్లలో 'raw' అవుట్‌పుట్‌ను పంపుతాము
        # ఇది నేరుగా LinkedIn లో పోస్ట్ చేయడానికి సిద్ధంగా ఉన్న కంటెంట్
        return result.raw if hasattr(result, 'raw') else str(result)
        
    except Exception as e:
        return f"Error in Crew Execution: {str(e)}"

# లోకల్‌గా టెస్ట్ చేయడానికి (Optional)
if __name__ == "__main__":
    test_topic = "Future of AI Agents"
    print(run_crew(test_topic))
