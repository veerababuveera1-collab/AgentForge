import os
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

# 1. పర్యావరణ వేరియబుల్స్ లోడ్ చేయడం
load_dotenv()

# --- LLM CONFIGURATIONS ---

# High-Performance Model (70b) - ఫైనల్ కంటెంట్ రైటింగ్ & ప్రొఫెషనల్ టచ్ కోసం
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096
)

# High-Speed Model (8b) - రీసెర్చ్ & అనాలిసిస్ కోసం (ఇది టోకెన్లు మరియు రేట్ లిమిట్ ఆదా చేస్తుంది)
fast_llm = LLM(
    model="groq/llama-3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

def run_crew(topic):
    """
    హైబ్రిడ్ మోడల్ లాజిక్: 
    రీసెర్చ్ కోసం వేగవంతమైన 8b ని, క్రియేటివ్ రైటింగ్ కోసం పవర్‌ఫుల్ 70b ని వాడుతుంది.
    """
    
    # ఏజెంట్లకు స్మార్ట్ మోడల్ కేటాయింపు
    research_agent.llm = fast_llm   # వేగం & ఎకానమీ
    writer_agent.llm = smart_llm     # క్వాలిటీ & డెప్త్
    linkedin_agent.llm = smart_llm   # ప్రొఫెషనల్ అవుట్‌పుట్

    # Crew అసెంబ్లీ
    crew = Crew(
        agents=[research_agent, writer_agent, linkedin_agent],
        tasks=[
            create_research_task(research_agent, topic),
            create_writing_task(writer_agent),
            create_linkedin_task(linkedin_agent)
        ],
        process=Process.sequential,
        
        # 🚨 ముఖ్యం: ఎర్రర్ ఇచ్చే 'embedder' కాన్ఫిగరేషన్‌ను ఇక్కడ తీసివేసి సింప్లిఫై చేశాం
        # దీనివల్ల Pydantic Validation ఎర్రర్స్ రావు.
        memory=False, 
        verbose=True,
        cache=True,
        
        # OpenAI కోసం వెతకకుండా ఆపుతుంది
        planning=False 
    )

    return crew.kickoff()
