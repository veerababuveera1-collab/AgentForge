from crewai import Crew
from crewai.llm import LLM
import os

from agents import create_research_agent, create_writer_agent
from tasks import create_research_task, create_writing_task


def run_crew(topic: str) -> str:

    llm = LLM(
        model="groq/llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY")
    )

    research_agent = create_research_agent(llm)
    writer_agent = create_writer_agent(llm)

    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)

    crew = Crew(
        agents=[research_agent, writer_agent],
        tasks=[research_task, writing_task],
        verbose=True
    )

    result = crew.kickoff()
    return result
