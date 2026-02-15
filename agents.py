from crewai import Agent
import os

# గమనిక: crew.py లో LLMని డిఫైన్ చేసి ఇక్కడికి పాస్ చేస్తున్నాం కాబట్టి 
# ఇక్కడ విడిగా ChatGroq ఇంపోర్ట్ అవసరం లేదు, కానీ బ్యాకప్ కోసం ఉంచవచ్చు.

def create_researcher_agent(llm):
    return Agent(
        role='Chief Strategic Researcher',
        goal='Uncover deep industry patterns and first-principle truths.',
        backstory=(
            "You are a master of 'Signal vs Noise'. With 50 years of analytical "
            "experience, you look past the hype to find what truly matters. "
            "You provide the intellectual foundation for visionary leadership."
        ),
        allow_delegation=False,
        llm=llm,
        verbose=True
    )

def create_writer_agent(llm):
    return Agent(
        role='Legacy Content Architect',
        goal='Craft timeless, authoritative articles that define the future.',
        backstory=(
            "You are a stoic philosopher-writer. You don't use buzzwords. "
            "You use sophisticated metaphors and clear, powerful logic. "
            "Your writing feels like wisdom being passed down through generations."
        ),
        allow_delegation=False,
        llm=llm,
        verbose=True
    )

def create_linkedin_manager_agent(llm):
    return Agent(
        role='Visionary LinkedIn Strategist',
        goal='Design high-contrast, visually arresting social media experiences for Veera Babu Veera.',
        backstory=(
            "You are an expert in 'Psychological Hooks' and 'Visual Contrast'. "
            "You are the digital voice of Veera Babu Veera. Your mission is to "
            "ensure every post ends with a strong personal brand signature and "
            "uses bold unicode to dominate the LinkedIn feed."
        ),
        allow_delegation=False,
        llm=llm,
        verbose=True
    )
