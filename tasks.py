from crewai import Task


def create_research_task(agent, topic):
    return Task(
        description=f"Research the topic: {topic}. Provide detailed bullet-point insights.",
        expected_output="Structured research insights in bullet points.",
        agent=agent
    )


def create_writing_task(agent):
    return Task(
        description=(
            "Using the research provided, write a complete blog article "
            "with introduction, body, and conclusion."
        ),
        expected_output="A well-structured blog post.",
        agent=agent
    )
