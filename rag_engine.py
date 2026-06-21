import os
import pandas as pd

try:
    from google import genai
except ImportError:
    genai = None


def ask_ai(question, df, ticker=None):

    df = df.copy()
    df.columns = [str(c).lower() for c in df.columns]

    latest = df.tail(10)

    context = latest.to_string(index=False)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return (
            "GEMINI_API_KEY not configured.\n\n"
            f"Ticker: {ticker}\n\n"
            f"Latest Data:\n{context}"
        )

    if genai is None:
        return "google-genai package is not installed."

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
You are a professional financial analyst.

Ticker: {ticker}

Stock Data:
{context}

Question:
{question}

Provide:
1. Trend analysis
2. Risk analysis
3. Key observations
4. Conclusion
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"
