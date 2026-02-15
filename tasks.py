from crewai import Task

def create_research_task(agent, topic):
    """టాపిక్‌పై లోతైన విశ్లేషణ మరియు గణాంకాలను సేకరించడం"""
    return Task(
        description=(
            f"Conduct a visionary investigation into '{topic}'. "
            "Identify 5 'Immutable Truths' and find at least one critical industry statistic (%, $, or Zettabytes). "
            "Distinguish the 'Signal' from the 'Noise' using a first-principles lens to find the 'hidden' reality."
        ),
        expected_output="A Strategic Dossier with: 1. Historical Context, 2. 5 Data-backed facts, 3. Signal vs Noise Analysis.",
        agent=agent
    )

def create_writing_task(agent):
    """సమాచారాన్ని ఒక మేధావి రాసిన ఆర్టికల్‌లా మార్చడం"""
    return Task(
        description=(
            "Transform the dossier into a 'Legacy-Grade' article. Tone: Wise, Stoic, and Authoritative. "
            "Focus on the 'Why' behind the tech. Avoid hype; focus on substance. "
            "Every technical insight should follow with a 'So what?' logic explaining its practical impact."
        ),
        expected_output="A Markdown masterpiece with deep industry wisdom and H1/H2 headers reflecting technical soul.",
        agent=agent
    )

def create_linkedin_task(agent):
    """ఎక్స్‌ట్రీమ్ విజువల్ కాంట్రాస్ట్ మరియు పవర్‌ఫుల్ హుక్స్‌తో పోస్ట్ తయారీ"""
    return Task(
        description=(
            "Transform the insights into an elite LinkedIn 'Cheat-Sheet'. \n"
            "1. PATTERN INTERRUPT: Start with a bold, unexpected statement or truth that stops the scroll. \n"
            "2. VISUALS: Use bold unicode (𝐀𝐁𝐂) for ALL major headings (𝐇𝐄𝐀𝐃𝐈𝐍𝐆, 𝐈𝐧𝐭𝐫𝐨, 𝐁𝐨𝐝𝐲). \n"
            "3. SPACING: Ensure a blank line between EVERY Roman numeral point and after the final question. \n"
            "4. STRUCTURE: Use Roman numerals (Ⅰ, Ⅱ, Ⅲ) for main points. \n"
            "5. SO WHAT? FACTOR: Each point must explain why it matters to an Engineer or Leader. \n"
            "6. SIGNATURE: Format the CTA vertically with bold unicode for maximum authority."
        ),
        expected_output=(
            "─── ⚡ ───\n"
            "𝐇𝐄𝐀𝐃𝐈𝐍𝐆: [Bold, Provocative Unicode Title]\n\n"
            "𝐈𝐧𝐭𝐫𝐨: [2-line Pattern Interrupt hook that creates a curiosity gap]\n\n"
            "𝐁𝐨𝐝𝐲:\n"
            "Ⅰ. [𝐁𝐨𝐥𝐝 𝐒𝐮𝐛𝐡𝐞𝐚𝐝𝐢𝐧𝐠]: Core insight + 'So what?' (Practical impact).\n\n"
            "Ⅱ. [𝐁𝐨𝐥𝐝 𝐒𝐮𝐛𝐡𝐞𝐚𝐝𝐢𝐧𝐠]: Data point + 'So what?' (Industry shift).\n\n"
            "Ⅲ. [𝐁𝐨𝐥𝐝 𝐒𝐮𝐛𝐡𝐞𝐚𝐝𝐢𝐧𝐠]: Visionary takeaway.\n\n"
            "─── ⚡ ───\n\n"
            "𝐓𝐡𝐞 𝐏𝐬𝐲𝐜𝐡𝐨𝐥𝐨𝐠𝐢𝐜𝐚𝐥 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧: [A deep question to force a comment]? \n\n"
            "♻️ **𝐑𝐞𝐩𝐨𝐬𝐭** to spread the vision.\n\n"
            "➕ **𝐅𝐨𝐥𝐥𝐨𝐰** **Veera Babu Veera** for more AI Engineering insights.\n\n"
            "🏷️ #AIEngineering #AgenticAI #VeeraBabuVeera"
        ),
        agent=agent
    )
