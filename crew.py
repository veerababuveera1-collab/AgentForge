import os
from crewai import Crew, Process, LLM
from agents import create_researcher_agent, create_writer_agent, create_linkedin_manager_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

def run_crew(topic):
    """
    Veera Babu Veera's Elite AI Crew 
    Groq Llama-3.3-70B మోడల్‌ను ఉపయోగించి రన్ అవుతుంది.
    """
    
    # Groq LLM Configuration
    # ఇక్కడ temperature 0.3 గా ఉంచాం, దీనివల్ల సమాధానాలు సీరియస్‌గా మరియు ప్రొఫెషనల్‌గా వస్తాయి.
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3, 
        max_tokens=2000,
        max_retries=5  # API Rate limit వస్తే 5 సార్లు ఆటోమేటిక్‌గా మళ్ళీ ప్రయత్నిస్తుంది.
    )

    # ఏజెంట్లను క్రియేట్ చేస్తున్నాం
    researcher = create_researcher_agent(llm)
    writer = create_writer_agent(llm)
    linkedin_manager = create_linkedin_manager_agent(llm)

    # టాస్క్‌లను ఏజెంట్లకు అసైన్ చేస్తున్నాం
    research_task = create_research_task(researcher, topic)
    writing_task = create_writing_task(writer)
    linkedin_task = create_linkedin_task(linkedin_manager)

    # క్రూ (Crew) ఫార్మేషన్
    # Process.sequential అంటే ఒక ఏజెంట్ పని ముగించాకే రెండో ఏజెంట్ మొదలుపెడుతుంది.
    crew = Crew(
        agents=[researcher, writer, linkedin_manager],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential,
        verbose=True
    )

    # ప్రక్రియను ప్రారంభించడం (Kickoff)
    return crew.kickoff()
