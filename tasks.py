from crewai import Task
from agents import research_agent, writer_agent

def get_tasks(topic):

    research_task = Task(
        description=f"Research the topic: {topic}. Provide detailed bullet-point insights.",
        expected_output="Structured research insights in bullet points.",
        agent=research_agent
    )

    writing_task = Task(
        description="Using the research provided, write a complete blog article with introduction, body, and conclusion.",
        expected_output="A well-structured blog post.",
        agent=writer_agent
    )

    return [research_task, writing_task]

