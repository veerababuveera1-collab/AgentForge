import os
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

# 1. పర్యావరణ వేరియబుల్స్ లోడ్ చేయడం
load_dotenv()

# --- LLM CONFIGURATIONS ---

# High-Performance Model (70b)
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096,
    max_retries=3
)

# High-Speed Backup Model (8b)
fast_llm = LLM(
    model="groq/llama-3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

def run_crew(topic):
    """
    ఈ ఫంక్షన్ అత్యంత సురక్షితమైనది. 
    1. మొదట రీసెర్చ్ కోసం చిన్న మోడల్‌ను వాడుతుంది (Tokens ఆదా చేయడానికి).
    2. క్రియేటివ్ రైటింగ్ కోసం పెద్ద మోడల్‌ను ట్రై చేస్తుంది.
    3. ఒకవేళ పెద్ద మోడల్ Rate Limit ఎర్రర్ ఇస్తే, ఆటోమేటిక్‌గా చిన్న మోడల్‌కి మారుతుంది.
    """
    
    # ప్రాథమిక కేటాయింపు
    research_agent.llm = fast_llm   # స్పీడ్ కోసం
    writer_agent.llm = smart_llm     # క్వాలిటీ కోసం
    linkedin_agent.llm = smart_llm   # క్వాలిటీ కోసం

    try:
        # Crew అసెంబ్లీ
        crew = Crew(
            agents=[research_agent, writer_agent, linkedin_agent],
            tasks=[
                create_research_task(research_agent, topic),
                create_writing_task(writer_agent),
                create_linkedin_task(linkedin_agent)
            ],
            process=Process.sequential,
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
            planning=False 
        )
        return crew.kickoff()

    except Exception as e:
        # ఒకవేళ Rate Limit ఎర్రర్ వస్తే, అన్ని ఏజెంట్లను Fast LLM కి మార్చి మళ్ళీ రన్ చేస్తుంది
        if "rate_limit_exceeded" in str(e).lower() or "429" in str(e):
            print("🚨 Smart LLM Limit Reached. Switching to Backup Fast LLM...")
            writer_agent.llm = fast_llm
            linkedin_agent.llm = fast_llm
            # మళ్ళీ ప్రయత్నం
            return crew.kickoff()
        else:
            raise e
