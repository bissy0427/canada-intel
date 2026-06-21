from kafka import KafkaProducer
import yfinance as yf
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TICKERS = ["SHOP.TO", "RY.TO", "TD.TO", "BNS.TO"]

while True:
    for ticker in TICKERS:
        df = yf.download(ticker, period="1d", interval="1m")
        latest = df.tail(1).reset_index().to_dict(orient="records")[0]

        latest["ticker"] = ticker

        producer.send("stock_topic", latest)
        print("sent:", latest)

    time.sleep(60)
