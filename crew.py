import os
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

# 1. పర్యావరణ వేరియబుల్స్ లోడ్ చేయడం
load_dotenv()

# 2. Groq LLM కాన్ఫిగరేషన్
# ఇక్కడ మనం Groqని స్పష్టంగా డిఫైన్ చేస్తున్నాం
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096, 
    max_retries=5
)

def run_crew(topic):
    """
    ఈ ఫంక్షన్ OpenAI కీ అవసరం లేకుండా Groq ద్వారా ఏజెంట్లను నడుపుతుంది.
    """
    # ఏజెంట్లకు మాన్యువల్‌గా Groq LLMని కేటాయించడం
    research_agent.llm = smart_llm
    writer_agent.llm = smart_llm
    linkedin_agent.llm = smart_llm

    # Crew అసెంబ్లీ
    crew = Crew(
        agents=[research_agent, writer_agent, linkedin_agent],
        tasks=[
            create_research_task(research_agent, topic),
            create_writing_task(writer_agent),
            create_linkedin_task(linkedin_agent)
        ],
        process=Process.sequential,
        # 🚨 ముఖ్యం: CrewAI OpenAI కోసం వెతకకుండా ఇక్కడ 'embedder'ని సెట్ చేస్తున్నాం
        # ఒకవేళ మీ దగ్గర Gemini API Key ఉంటే దాన్ని వాడవచ్చు, లేదంటే 'None' చేయవచ్చు.
        embedder={
            "provider": "google",
            "config": {
                "model": "models/embedding-001",
                "api_key": os.getenv("GEMINI_API_KEY") or "na"
            }
        } if os.getenv("GEMINI_API_KEY") else None,
        memory=False, 
        verbose=True,
        cache=True,
        # ఇది OpenAI కి వెళ్లకుండా ఆపుతుంది
        planning=False 
    )

    return crew.kickoff()
