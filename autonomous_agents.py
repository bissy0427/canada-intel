import os
from google import genai

# =========================
# GEMINI CLIENT (NEW SDK)
# =========================
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY missing")

client = genai.Client(api_key=api_key)

MODEL = "gemini-2.5-flash"


# =========================
# AUTONOMOUS AGENT CLASS
# =========================
class AutonomousAgent:
    def __init__(self, role):
        self.role = role

    def decide(self, context):
        prompt = f"""
You are an autonomous financial AI agent.

ROLE:
{self.role}

CONTEXT:
{context}

TASK:
- Analyze market situation
- Make decision
- Provide reasoning
- Be concise and professional
"""

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text
