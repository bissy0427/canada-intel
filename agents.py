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
# BASE AGENT FUNCTION
# =========================
def run_agent(role, data, question):
    """
    Generic AI agent using Gemini
    """

    prompt = f"""
You are a professional financial analyst.

ROLE: {role}

DATA:
{data}

QUESTION:
{question}

TASK:
- Analyze the data
- Give clear insights
- Focus on risk, trend, opportunity
- Be concise but professional
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text


# =========================
# SPECIALIZED AGENTS
# =========================
def bank_agent(data, question):
    return run_agent("BANKING ANALYST", data, question)


def energy_agent(data, question):
    return run_agent("ENERGY ANALYST", data, question)


def tech_agent(data, question):
    return run_agent("TECH ANALYST", data, question)


def infra_agent(data, question):
    return run_agent("INFRASTRUCTURE ANALYST", data, question)
