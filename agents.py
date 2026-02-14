from crewai import Agent


def create_research_agent(llm):
    return Agent(
        role="Research Specialist",
        goal="Gather accurate and structured information about a given topic.",
        backstory="You are a professional AI researcher.",
        verbose=True,
        llm=llm
    )


def create_writer_agent(llm):
    return Agent(
        role="Content Writer",
        goal="Create a well-structured and engaging blog post based on research.",
        backstory="You are an expert content writer.",
        verbose=True,
        llm=llm
    )
