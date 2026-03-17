import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_headline(headline: str):

    prompt = f"""
You are an AI system that evaluates news headlines.

Classify the headline into ONE of these:
Reliable
Suspicious
Potentially Misleading

Return STRICTLY in this format:

Classification: <category>
Explanation: <short explanation>

Headline: {headline}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    result = response.choices[0].message.content

    lines = result.split("\n")

    classification = lines[0].split(":")[1].strip()
    explanation = lines[1].split(":")[1].strip()

    return classification, explanation