from crewai import Task

def create_research_task(agent, topic):
    return Task(
        description=(
            f"Conduct a visionary investigation into '{topic}'. "
            "Identify 5 'Immutable Truths' and include one critical industry statistic. "
            "Focus on high-value data to avoid unnecessary filler text."
        ),
        expected_output="A Strategic Dossier with: 1. Historical Context, 2. 5 Data-backed facts, 3. Signal vs Noise Analysis.",
        agent=agent
    )

def create_writing_task(agent):
    return Task(
        description=(
            "Transform the dossier into a 'Legacy-Grade' article. Tone: Wise and Authoritative. "
            "Every technical insight should follow with a 'So what?' explanation. "
            "Keep paragraphs tight to prevent output truncation."
        ),
        expected_output="A Markdown masterpiece with deep industry wisdom and H1/H2 headers.",
        agent=agent
    )

def create_linkedin_task(agent):
    return Task(
        description=(
            "Transform the research into an elite LinkedIn 'Cheat-Sheet'. \n"
            "1. FORMATTING: Use bold unicode (𝐀𝐁𝐂) ONLY for headers (𝐇𝐄𝐀𝐃𝐈𝐍𝐆, 𝐈𝐧𝐭𝐫𝐨, 𝐁𝐨𝐝𝐲). Keep regular text standard for readability.\n"
            "2. LIMIT CONTROL: Be extremely concise to ensure the full post is generated without being cut off.\n"
            "3. STRUCTURE: Use Roman numerals (Ⅰ, Ⅱ, Ⅲ) for main points with a blank line between each.\n"
            "4. SO WHAT? FACTOR: Each point must explain the practical impact for an Engineer.\n"
            "5. CTA: Include a clean, vertical signature with 'Repost' and 'Follow'."
        ),
        expected_output=(
            "─── ⚡ ───\n"
            "𝐇𝐄𝐀𝐃𝐈𝐍𝐆: [Bold Title]\n\n"
            "𝐈𝐧𝐭𝐫𝐨: [2-line Hook]\n\n"
            "𝐁𝐨𝐝𝐲:\n"
            "Ⅰ. **[Subheading]**: Insight + So what? (Keep it brief)\n\n"
            "Ⅱ. **[Subheading]**: Data + So what? (Keep it brief)\n\n"
            "Ⅲ. **[Subheading]**: Strategy + So what? (Keep it brief)\n\n"
            "─── ⚡ ───\n\n"
            "𝐓𝐡𝐞 𝐏𝐬𝐲𝐜𝐡𝐨𝐥𝐨𝐠𝐢𝐜𝐚𝐥 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧: [Question]? \n\n"
            "♻️ **𝐑𝐞𝐩𝐨𝐬𝐭** to spread the vision.\n"
            "➕ **𝐅𝐨𝐥𝐥𝐨𝐰** **Veera Babu Veera** for more AI Engineering insights.\n\n"
            "🏷️ #AIEngineering #AgenticAI #VeeraBabuVeera"
        ),
        agent=agent
    )
