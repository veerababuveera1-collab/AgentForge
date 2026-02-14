from crewai import Crew
from agents import create_research_agent, create_writer_agent
from tasks import create_research_task, create_writing_task


def run_crew(topic: str) -> str:
    """
    Creates agents, assigns tasks, runs the crew,
    and returns the final generated output.
    """

    # Create Agents
    research_agent = create_research_agent()
    writer_agent = create_writer_agent()

    # Create Tasks
    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)

    # Create Crew
    crew = Crew(
        agents=[research_agent, writer_agent],
        tasks=[research_task, writing_task],
        verbose=True
    )

    # Execute Workflow
    result = crew.kickoff()

    return result

