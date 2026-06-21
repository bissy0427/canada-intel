import os
import google.generativeai as genai

# Load API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not set in environment")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


def explain_stock(ticker, df):
    """
    AI analysis of stock movement using Gemini
    """

    df = df.tail(10).copy()

    # safety check for required columns
    required_cols = ["date", "close", "volume"]
    for col in required_cols:
        if col not in df.columns:
            return f"Missing column: {col}"

    latest = df[required_cols].to_string(index=False)

    prompt = f"""
You are a professional financial analyst.

Analyze the stock: {ticker}

Recent market data:
{latest}

Return:
1. Simple summary
2. Why price may be moving
3. Risk level (low / medium / high)
4. 3 insights (not financial advice)
"""

    response = model.generate_content(prompt)
    return response.text
