import os
from crewai import Crew, Process, LLM
from agents import create_researcher_agent, create_writer_agent, create_linkedin_manager_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

def run_crew(topic):
    # Groq LLM configuration
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3,
        max_tokens=1500,
        max_retries=5 # ఎర్రర్ వస్తే 5 సార్లు ఆటోమేటిక్‌గా ట్రై చేస్తుంది
    )

    # Agents
    researcher = create_researcher_agent(llm)
    writer = create_writer_agent(llm)
    linkedin_manager = create_linkedin_manager_agent(llm)

    # Tasks
    research_task = create_research_task(researcher, topic)
    writing_task = create_writing_task(writer)
    linkedin_task = create_linkedin_task(linkedin_manager)

    # Crew
    crew = Crew(
        agents=[researcher, writer, linkedin_manager],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()
