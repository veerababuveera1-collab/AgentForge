from crewai import Task

def create_research_task(agent, topic):
    """టాపిక్‌పై లోతైన మరియు గణాంక ఆధారిత పరిశోధన చేసే టాస్క్"""
    return Task(
        description=(
            f"Conduct a deep-dive investigation into '{topic}'. "
            "Go beyond the surface: find 'Golden Nuggets' of information, "
            "surprising statistics, and future-forward predictions. "
            "Focus on finding specific data points that make the content authoritative."
        ),
        expected_output=(
            "A high-impact Research Dossier containing: \n"
            "1. The 'Big Idea' (2-sentence executive summary)\n"
            "2. 5 Mind-blowing Statistics or Industry Facts\n"
            "3. Key Challenges & Future Outlook\n"
            "4. A list of 4 'Click-worthy' blog headings."
        ),
        agent=agent
    )

def create_writing_task(agent):
    """పరిశోధనను ఒక అద్భుతమైన కథనంగా (Blog) మార్చే టాస్క్"""
    return Task(
        description=(
            "Transform the research dossier into a 'Masterclass' blog post. "
            "The tone should be 'Sophisticated yet Conversational'. "
            "Use storytelling to make complex data easy to digest. "
            "Ensure you use a 'Pattern Interrupt' hook in the first paragraph to grab attention."
        ),
        expected_output=(
            "A publication-ready Markdown masterpiece featuring: \n"
            "- # [A Magnetic, Catchy H1 Title]\n"
            "- ## The Hook (Introduction that creates curiosity)\n"
            "- ## Deep Dive (Well-structured insights using H2 headers)\n"
            "- ## Strategic Implications (The 'So What?' factor)\n"
            "- ## Final Verdict (Conclusion with a strong Call to Action)"
        ),
        agent=agent
    )

def create_linkedin_task(agent):
    """బ్లాగ్ నుండి వైరల్ అయ్యే LinkedIn పోస్ట్‌ను సిద్ధం చేసే టాస్క్"""
    return Task(
        description=(
            "Distill the soul of the blog post into a viral-potential LinkedIn update. "
            "Use the 'Hook-Value-CTA' framework. Make it visually airy with plenty of white space. "
            "Use professional emojis strategically to guide the reader's eye. "
            "IMPORTANT: The total text MUST be strictly under 2800 characters to prevent errors."
        ),
        expected_output=(
            "A high-conversion LinkedIn post featuring: \n"
            "- ⚡ A 'Scroll-Stopping' first line (The Hook)\n"
            "- 💡 3-5 Actionable 'Pro-Tips' or insights\n"
            "- 📊 1 Powerful statistic to build trust\n"
            "- 🚀 A punchy Call to Action (CTA) that encourages comments\n"
            "- 🏷️ 5 Trending hashtags (format: #AI #Tech - do not include the word 'hashtag')."
        ),
        agent=agent
    )
