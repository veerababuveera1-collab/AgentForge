import os
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

# 1. పర్యావరణ వేరియబుల్స్ లోడ్ చేయడం
load_dotenv()

# 2. LLM కాన్ఫిగరేషన్
# max_tokens=4096 వల్ల మీ కంటెంట్ మధ్యలో ఆగిపోదు
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096, 
    max_retries=5
)

def run_crew(topic):
    """
    ఈ ఫంక్షన్‌ను app.py పిలుస్తుంది. 
    ఇది ఏజెంట్లను మరియు టాస్క్‌లను సమన్వయం చేసి ఫైనల్ రిపోర్ట్ ఇస్తుంది.
    """
    # ఏజెంట్లకు అప్‌గ్రేడ్ చేసిన LLMని కేటాయించడం
    research_agent.llm = smart_llm
    writer_agent.llm = smart_llm
    linkedin_agent.llm = smart_llm

    # టాస్క్‌లను ఇనిషియలైజ్ చేయడం
    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)
    linkedin_task = create_linkedin_task(linkedin_agent)

    # Crew అసెంబ్లీ
    # Sequential process వల్ల ఒక ఏజెంట్ అవుట్‌పుట్ మరొకరికి పర్ఫెక్ట్‌గా అందుతుంది
    crew = Crew(
        agents=[research_agent, writer_agent, linkedin_agent],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential,
        memory=False, # Streamlit stability కోసం ప్రస్తుతానికి False
        verbose=True,
        cache=True
    )

    return crew.kickoff()
