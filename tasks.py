from crewai import Task

def create_research_task(agent, topic):
    """టాపిక్‌పై దశాబ్దాల అనుభవంతో కూడిన లోతైన పరిశోధన"""
    return Task(
        description=(
            f"Conduct a visionary investigation into '{topic}'. "
            "Don't just find news; identify 'First Principles' and 100-year patterns. "
            "Find 5 'Immutable Truths' and distinguish the 'Signal' from the 'Noise'. "
            "Look for specific data points that challenge the current status quo."
        ),
        expected_output=(
            "A 'Master-Level' Strategic Dossier containing: \n"
            "1. Historical Context (How we got here)\n"
            "2. 5 Immutable Truths (Hard Data Points)\n"
            "3. The 'Signal vs Noise' Analysis\n"
            "4. 4 Provocative headings for high-authority content."
        ),
        agent=agent
    )

def create_writing_task(agent):
    """రీసెర్చ్‌ను ఒక ప్రొఫెషనల్ మాస్టర్‌క్లాస్ ఆర్టికల్‌గా మార్చడం"""
    return Task(
        description=(
            "Transform the dossier into a 'Legacy-Grade' article. "
            "Tone: Timeless, Wise, and Stoic. Avoid hype; focus on substance. "
            "Use sophisticated metaphors to explain complex AI shifts. "
            "Write as if you are a visionary leader passing wisdom to future generations."
        ),
        expected_output=(
            "A publication-ready Markdown masterpiece: \n"
            "- # [A Deep, Thought-Provoking H1 Title]\n"
            "- ## The Evolution (Contextual Intro)\n"
            "- ## The Core Pillars (H2 Sections with depth)\n"
            "- ## The Human Element (Intersection of Tech & Soul)\n"
            "- ## A Call to Leadership (Visionary Conclusion)"
        ),
        agent=agent
    )

def create_linkedin_task(agent):
    """మీ పేరు మరియు ఎక్స్‌ట్రీమ్ విజువల్ కాంట్రాస్ట్‌తో కూడిన పోస్ట్ తయారీ"""
    return Task(
        description=(
            "Transform the blog into an elite LinkedIn 'Cheat-Sheet'. \n"
            "1. VISUAL CONTRAST: Use bold unicode (𝐀𝐁𝐂) for ALL headings.\n"
            "2. STRUCTURE: Use Roman numerals (Ⅰ, Ⅱ, Ⅲ) for main points.\n"
            "3. DIVIDERS: Use ─── ⚡ ─── to separate sections.\n"
            "4. PSYCHOLOGICAL HOOK: Start with a 'Pattern Interrupt' and end with a 'Binary Question'.\n"
            "5. MANDATORY SIGNATURE: End with: '➕ Follow Veera Babu Veera for more AI Engineering insights.'\n"
            "Keep the total text under 2800 characters."
        ),
        expected_output=(
            "A high-authority LinkedIn post formatted as: \n"
            "─── ⚡ ───\n"
            "𝐇𝐄𝐀𝐃𝐈𝐍𝐆: A bold, high-contrast title using symbols.\n"
            "𝐈𝐧𝐭𝐫𝐨: A 2-line hook that creates a 'Curiosity Gap'.\n"
            "𝐁𝐨𝐝𝐲: 3-5 points (Ⅰ, Ⅱ, Ⅲ...) with bold subheadings and wide spacing.\n"
            "𝐓𝐡𝐞 𝐏𝐬𝐲𝐜𝐡𝐨𝐥𝐨𝐠𝐢𝐜𝐚𝐥 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧: A deep question to force comments.\n"
            "𝐂𝐓𝐀: ♻️ Repost to spread the vision | ➕ Follow Veera Babu Veera for more AI Engineering insights.\n"
            "🏷️ 3-5 high-reach hashtags."
        ),
        agent=agent
    )
