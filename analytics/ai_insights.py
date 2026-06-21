import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not set")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def explain_stock(ticker, df):
    df = df.tail(10)

    latest = df[["date", "close", "volume"]].to_string(index=False)

    prompt = f"""
You are a senior financial analyst.

Analyze this stock: {ticker}

Recent market data:
{latest}

Provide:
1. Simple summary
2. Price movement explanation
3. Risk level (low/medium/high)
4. 3 bullet insights (not financial advice)
"""

    response = model.generate_content(prompt)
    return response.text
