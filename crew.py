from crewai import Crew, Process
from crewai.llm import LLM
import os
# agents.py మరియు tasks.py లో కొత్త ఫంక్షన్లు యాడ్ చేయాలి
from agents import create_research_agent, create_writer_agent, create_linkedin_manager_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

def run_crew(topic: str) -> str:
    # 1. LLM Configuration
    llm = LLM(
        model="groq/llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7,
        max_tokens=4096
    )

    # 2. ఏజెంట్ల తయారీ (LinkedIn Manager ని కలిపి)
    research_agent = create_research_agent(llm)
    writer_agent = create_writer_agent(llm)
    linkedin_manager = create_linkedin_manager_agent(llm) # కొత్త ఏజెంట్

    # 3. టాస్క్‌ల తయారీ (LinkedIn Task ని కలిపి)
    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)
    linkedin_task = create_linkedin_task(linkedin_manager) # కొత్త టాస్క్

    # 4. Crew అప్‌గ్రేడ్: LinkedIn Task ని చివరగా జోడించాం
    crew = Crew(
        agents=[research_agent, writer_agent, linkedin_manager],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential, 
        verbose=True,                
        memory=True,                 
        cache=True                   
    )

    try:
        # 5. Execution
        result = crew.kickoff()
        
        # రిజల్ట్ నేరుగా LinkedIn కి పంపే ఫార్మాట్‌లో ఉంటుంది
        return result.raw if hasattr(result, 'raw') else str(result)
        
    except Exception as e:
        return f"Error in Crew Execution: {str(e)}"
