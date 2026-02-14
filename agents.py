from crewai import Agent


def create_research_agent():
    return Agent(
        role="Research Specialist",
        goal="Gather accurate and structured information about a given topic.",
        backstory=(
            "You are a professional AI researcher skilled in collecting "
            "clear, structured insights."
        ),
        verbose=True
    )


def create_writer_agent():
    return Agent(
        role="Content Writer",
        goal="Create a well-structured and engaging blog post based on research.",
        backstory=(
            "You are an expert content writer who transforms research "
            "into compelling blog articles."
        ),
        verbose=True
    )
