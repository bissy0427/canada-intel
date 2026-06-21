# 🏦 Canada AI Financial Intelligence Platform

An AI-powered financial intelligence system that transforms Canadian stock market data into **institutional-grade insights** using:

- Retrieval-Augmented Generation (RAG)
- Multi-Agent AI Analysis
- Real-time market data pipelines
- Portfolio risk analytics

This project simulates a ** AI financial terminal** for retail and institutional-style analysis.

---

## 🚀 Key Features

### 📊 Market Intelligence Dashboard
- Live stock tracking (SHOP.TO, RY.TO, TD.TO, BNS.TO, ENB.TO, etc.)
- Interactive Streamlit dashboard
- Real-time filtering by ticker

### 🧠 AI Financial Analyst (RAG System)
- Natural language stock questions
- AI-generated market insights
- Context-aware responses using historical data
- Memory-enhanced reasoning

### 🤖 Multi-Agent AI System
Specialized agents analyze different sectors:
- 🏦 Bank Agent (RY.TO, TD.TO, BNS.TO)
- 💻 Tech Agent (SHOP.TO)
- ⚡ Energy Agent (ENB.TO, SU.TO)
- 🚆 Infrastructure Agent (CNR.TO, CP.TO)

### 📉 Risk Intelligence Engine
- Portfolio risk scoring
- Volatility detection
- Market trend interpretation

### 🗄️ Data Engineering Pipeline
- Yahoo Finance API ingestion
- ETL processing pipeline
- PostgreSQL data warehouse
- Cleaned & normalized stock dataset

---

## 🧠 System Architecture

### 1. Data Layer
- Yahoo Finance (yfinance)
- PostgreSQL database (Dockerized)
- Automated ETL pipeline

### 2. AI Layer
- Gemini AI (Google GenAI)
- RAG-based context retrieval
- Multi-agent reasoning system
- Memory module for past queries

### 3. Application Layer
- Streamlit financial dashboard
- Interactive AI chat interface
- Portfolio analytics UI

---

## 📊 Business Problems Solved

### 1. Financial Data Overload
Investors struggle to interpret large volumes of market data.  
➡️ This system compresses raw financial data into actionable insights.

---

### 2. Slow Decision Making
Traditional analysis is manual and time-consuming.  
➡️ AI agents provide instant sector-based analysis.

---

### 3. Lack of Unified Portfolio Intelligence
Most tools analyze stocks individually.  
➡️ This system performs cross-stock and cross-sector intelligence aggregation.

---

### 4. Retail Investor Disadvantage
Retail investors lack institutional-grade tools.  
➡️ This platform simulates Bloomberg-level intelligence for retail users.

---

### 5. Risk Blind Spots
Investors often fail to detect hidden volatility risks.  
➡️ AI risk engine highlights exposure and instability patterns.

---

## 🏗️ Tech Stack

- Python 3.11+
- Streamlit (Frontend Dashboard)
- PostgreSQL (Database)
- yFinance (Market Data API)
- Google Gemini AI (LLM)
- FAISS (Vector Search)
- Pandas (Data Processing)
- Docker (Database Containerization)

---

## 📁 Project Structure


## 📦 Project Structure

canada-intel/
│
├── app.py # Streamlit dashboard
├── etl.py # Data pipeline (Yahoo Finance → PostgreSQL)
├── rag_engine.py # AI reasoning engine
├── agents.py # Multi-agent system
├── memory.py # Conversation memory layer
├── vector_store.py # FAISS-based retrieval
├── risk.py # Risk scoring engine
├── requirements.txt
└── README.md

📈 Future Improvements
⚡ Real-time Kafka stock streaming
🧠 Autonomous trading AI agents
📊 Portfolio optimizer (Sharpe ratio-based)
📰 Sentiment analysis (news + social media)
🌍 Multi-market expansion (US, Crypto, Forex)
🤖 Fully autonomous Bloomberg-style AI terminal




---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/bissy0427/canada-intel.git
cd canada-intel


⚠️ Disclaimer

This project is for educational and research purposes only.

It does not provide financial advice and should not be used for real trading decisions.

👨‍💻 Author

Built by Bismark Sarpong

Focus areas:

AI Financial Systems
RAG Architecture
Multi-Agent AI Design
Financial Data Engineering
Real-time Analytics Systems
