import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/canada_intel"
)

TICKERS = [
    "SHOP.TO",
    "RY.TO",
    "TD.TO",
    "BNS.TO",
    "ENB.TO",
    "CNR.TO",
    "SU.TO"
]

all_data = []

for t in TICKERS:

    print(f"Downloading {t}...")

    df = yf.download(
        t,
        period="1mo",
        auto_adjust=True
    )

    if df.empty:
        print(f"No data for {t}")
        continue

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    df.columns = [str(c).lower() for c in df.columns]

    df["ticker"] = t

    all_data.append(df)

final_df = pd.concat(all_data)

print(final_df.head())

final_df.to_sql(
    "stock_prices",
    engine,
    if_exists="replace",
    index=False
)

print("ETL Completed Successfully")
