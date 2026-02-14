from crewai import Task

def create_research_task(agent, topic):
    """టాపిక్‌పై లోతైన పరిశోధన చేసే టాస్క్"""
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
    """పరిశోధన ఆధారంగా ప్రొఫెషనల్ బ్లాగ్ రాసే టాస్క్"""
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

def create_linkedin_task(agent):
    """బ్లాగ్ నుండి వైరల్ LinkedIn పోస్ట్‌ను తయారు చేసే టాస్క్"""
    return Task(
        description=(
            "Extract the most impactful insights from the blog post and transform them into "
            "a viral-ready LinkedIn post. Use a strong hook, clean bullet points, and "
            "professional emojis. Ensure the tone is authoritative yet engaging."
            "IMPORTANT: The entire post MUST be strictly under 2800 characters to fit LinkedIn's limits."
        ),
        expected_output=(
            "A ready-to-publish LinkedIn post featuring: \n"
            "- A compelling headline/hook\n"
            "- 3-5 high-value bullet points\n"
            "- Strategic professional emojis (🚀, 📈, 💡)\n"
            "- A call to action (CTA)\n"
            "- 5 relevant trending hashtags."
        ),
        agent=agent
    )
