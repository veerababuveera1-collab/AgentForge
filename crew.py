from crewai import Crew
from agents import create_research_agent, create_writer_agent
from tasks import create_research_task, create_writing_task
import os


def run_crew(topic: str) -> str:

    research_agent = create_research_agent()
    writer_agent = create_writer_agent()

    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)

    crew = Crew(
        agents=[research_agent, writer_agent],
        tasks=[research_task, writing_task],
        verbose=True,
        llm={
            "provider": "groq",
            "model": "llama3-70b-8192",
            "api_key": os.getenv("GROQ_API_KEY")
        }
    )

    result = crew.kickoff()
    return result
