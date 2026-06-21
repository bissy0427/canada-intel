import pandas as pd
import numpy as np

def risk_score(df):
    df = df.copy()

    returns = df["close"].pct_change()

    volatility = returns.std()
    avg_volume = df["volume"].mean()

    score = volatility * 100 + (avg_volume / 1e6)

    return round(score, 2)
