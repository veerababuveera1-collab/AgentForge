from crewai import Task

def create_research_task(agent, topic):
    return Task(
        description=(
            f"Conduct a comprehensive investigation into '{topic}'. "
            "Identify the latest trends, key challenges, and future predictions. "
            "Focus on finding data-backed insights and expert opinions."
        ),
        expected_output=(
            "A comprehensive research brief containing: \n"
            "1. Executive Summary\n"
            "2. Key Findings (Bullet points)\n"
            "3. Relevant Statistics/Data points\n"
            "4. List of potential sub-headings for the blog."
        ),
        agent=agent
    )

def create_writing_task(agent):
    return Task(
        description=(
            "Using the research brief, compose a high-authority blog post. "
            "The content should be professional, insightful, and formatted using Markdown. "
            "Ensure you include a catchy title, sub-headers, and a call to action."
        ),
        expected_output=(
            "A complete, publication-ready blog post in Markdown format. "
            "Structure: \n"
            "- # [Catchy H1 Title]\n"
            "- ## Introduction\n"
            "- ## Key Trends/Insights (using H2 headers)\n"
            "- ## Strategic Implications\n"
            "- ## Conclusion & Summary"
        ),
        agent=agent
    )
