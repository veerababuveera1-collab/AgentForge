from crewai import Agent

research_agent = Agent(
    role="Research Specialist",
    goal="Gather accurate and structured information about a given topic.",
    backstory="You are a professional AI researcher who provides detailed and organized insights.",
    verbose=True
)

writer_agent = Agent(
    role="Content Writer",
    goal="Create a well-structured and engaging blog post based on research.",
    backstory="You are a skilled AI content writer who transforms research into readable content.",
    verbose=True
)

