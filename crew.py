import os
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task
from dotenv import load_dotenv

# .env ఫైల్ నుండి API Keys లోడ్ చేయడం కోసం
load_dotenv()

# 1. LLM Configuration
# Groq వంటి మోడల్స్ వాడేటప్పుడు temperature మరియు max_tokens సెట్టింగ్స్ కీలకం
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096,  # కంటెంట్ కట్ అవ్వకుండా ఉండటానికి పెద్ద లిమిట్
    max_retries=5
)

def run_agentic_workflow(topic):
    # 2. Assign LLM to Agents (Before Task Creation)
    # ఏజెంట్లు టాస్క్‌లను ప్రాసెస్ చేయడానికి ముందే LLM ని సెట్ చేయాలి
    research_agent.llm = smart_llm
    writer_agent.llm = smart_llm
    linkedin_agent.llm = smart_llm

    # 3. Task Initialization
    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)
    linkedin_task = create_linkedin_task(linkedin_agent)

    # 4. Crew Assembly
    # CrewAI లో 'memory' ఫీచర్ వాడాలంటే 'embedder' కాన్ఫిగరేషన్ అవసరం ఉండొచ్చు, 
    # ఒకవేళ ఎర్రర్ వస్తే memory=False చేసి చూడండి.
    crew = Crew(
        agents=[research_agent, writer_agent, linkedin_agent],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential,
        memory=True,     # పాత సమాచారాన్ని గుర్తుంచుకోవడానికి
        verbose=True,    # టెర్మినల్‌లో ప్రాసెస్ చూడటానికి
        cache=True
    )

    return crew.kickoff()

if __name__ == "__main__":
    # ఎగ్జిక్యూషన్ స్టార్ట్
    target_topic = "The Emergence of Agent-First Architecture"
    
    try:
        result = run_agentic_workflow(target_topic)
        print("\n\n" + "="*50)
        print("🚀 FINAL ELITE POST GENERATED SUCCESSFULLY:")
        print("="*50 + "\n")
        print(result)
    except Exception as e:
        print(f"❌ An error occurred: {e}")
