import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-MiniLM-L6-v2")


class MultiStockVectorStore:
    def __init__(self):
        self.index = None
        self.texts = []
        self.metadata = []

    def build(self, df: pd.DataFrame):
        df = df.copy()
        df.columns = [c.lower() for c in df.columns]

        texts = []
        meta = []

        for _, row in df.iterrows():
            text = f"""
Stock: {row['ticker']}
Date: {row['date']}
Close: {row['close']}
Volume: {row['volume']}
"""

            texts.append(text)
            meta.append(row["ticker"])

        self.texts = texts
        self.metadata = meta

        embeddings = encoder.encode(texts)
        embeddings = np.array(embeddings).astype("float32")

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def search(self, query, k=10):
        q = encoder.encode([query]).astype("float32")

        _, idx = self.index.search(q, k)

        results = [self.texts[i] for i in idx[0]]

        return "\n".join(results)
