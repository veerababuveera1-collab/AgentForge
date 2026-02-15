import os
from crewai import Crew, Process, LLM
from agents import research_agent, writer_agent, linkedin_agent
from tasks import create_research_task, create_writing_task, create_linkedin_task

# 1. LLM Configuration with Increased Limits
# max_tokens పెంచడం వల్ల కంటెంట్ మధ్యలో కట్ అవ్వదు
smart_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=4096,  # Higher limit for complete posts
    max_retries=5
)

# 2. Assign LLM to Agents
# ప్రతి ఏజెంట్‌కు అప్‌గ్రేడ్ చేసిన LLMని అనుసంధానించడం
research_agent.llm = smart_llm
writer_agent.llm = smart_llm
linkedin_agent.llm = smart_llm

def run_agentic_workflow(topic):
    # 3. Task Initialization
    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent)
    linkedin_task = create_linkedin_task(linkedin_agent)

    # 4. Crew Assembly
    # memory=True మరియు verbose=True వల్ల ప్రాసెస్ క్లారిటీగా ఉంటుంది
    crew = Crew(
        agents=[research_agent, writer_agent, linkedin_agent],
        tasks=[research_task, writing_task, linkedin_task],
        process=Process.sequential,  # Sequential execution for logical flow
        memory=True,                 # Context retention across tasks
        verbose=True,                # Better debugging logs
        cache=True
    )

    return crew.kickoff()

if __name__ == "__main__":
    topic = "The Emergence of Agent-First Architecture"
    result = run_agentic_workflow(topic)
    print("\n\n" + "-"*30)
    print("FINAL ELITE POST:")
    print("-"*30 + "\n")
    print(result)
