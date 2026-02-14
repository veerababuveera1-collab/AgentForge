from crewai import Crew, Process
from crewai.llm import LLM
import os
from agents import create_research_agent, create_writer_agent
from tasks import create_research_task, create_writing_task

def run_crew(topic: str) -> str:
    # 1. LLM Configuration - అప్‌గ్రేడ్: థ్రెషోల్డ్ మరియు టైమౌట్ సెట్టింగ్స్
    llm = LLM(
        model="groq/llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7,
        max_tokens=4096
    )

    # 2. ఏజెంట్ల తయారీ
    research_agent = create_research_agent(llm)
    writer_agent = create_writer_agent(llm)

    # 3. టాస్క్‌ల తయారీ
    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)

    # 4. Crew అప్‌గ్రేడ్: Process మరియు Memory జోడింపు
    crew = Crew(
        agents=[research_agent, writer_agent],
        tasks=[research_task, writing_task],
        process=Process.sequential,  # పనులు ఒకదాని తర్వాత ఒకటి క్రమ పద్ధతిలో జరుగుతాయి
        verbose=True,                # లాగ్స్ చూడటానికి
        memory=True,                 # ఏజెంట్లు మునుపటి సమాచారాన్ని గుర్తుంచుకోవడానికి
        cache=True                   # ఒకే రకమైన రిక్వెస్ట్‌లను వేగంగా పూర్తి చేయడానికి
    )

    try:
        # 5. Execution
        result = crew.kickoff()
        
        # CrewAI 0.28+ వెర్షన్లలో result.raw వాడాలి
        return result.raw if hasattr(result, 'raw') else str(result)
        
    except Exception as e:
        return f"Error in Crew Execution: {str(e)}"
