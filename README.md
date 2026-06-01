# 🎬 Agentic RAG Anime Recommender System

> Enterprise-Grade Multi-Agent Recommendation Engine powered by RAG, Semantic Search, Vector Databases, and LLM Reasoning.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge\&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Agentic_AI-green?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-Llama_3.1-orange?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-purple?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge\&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-K8s-blue?style=for-the-badge\&logo=kubernetes)
![MIT License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

# 📖 Overview

Traditional recommendation systems rely heavily on tags, ratings, and predefined categories. These approaches often fail to capture emotions, atmosphere, themes, and nuanced user intent.

The Agentic RAG Anime Recommender System addresses this challenge by combining:

* Agentic AI
* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Large Language Models
* Explainable Recommendations

Users can search naturally:

> "Suggest an anime that feels like a lonely evening in a cyberpunk city."

Instead of keyword matching, the platform understands the semantic meaning behind the query and provides intelligent recommendations with reasoning.

---

# 🎯 Key Features

### 🧠 Semantic Search

Discover anime using natural language instead of genres or tags.

### 🤖 Agentic AI Workflow

Multi-stage reasoning pipeline for understanding user intent and generating recommendations.

### 📚 Retrieval-Augmented Generation

Grounded recommendations generated using retrieved context from a vector database.

### 🔍 Explainable Recommendations

Every recommendation includes AI-generated reasoning.

### ⚡ High-Speed Inference

Powered by Groq LPU acceleration for ultra-fast response generation.

### 📊 Observability Dashboard

Built-in monitoring, system logs, and performance tracking.

### ☁️ Production Deployment Ready

Supports Docker, Kubernetes, CI/CD pipelines, and cloud deployment.

---

# 🏗️ System Architecture

## High-Level Workflow

User Query
↓
Query Understanding Agent
↓
Embedding Generation
↓
ChromaDB Retrieval
↓
Context Ranking
↓
Reasoning Agent
↓
Recommendation Generation
↓
Explainable Response

---

## Multi-Agent Architecture

### 1️⃣ Query Understanding Agent

Responsibilities:

* User intent extraction
* Query enhancement
* Context expansion
* Search optimization

---

### 2️⃣ Retrieval Agent

Responsibilities:

* Vector similarity search
* Metadata filtering
* Top-K retrieval
* Context ranking

Technologies:

* ChromaDB
* Sentence Transformers
* MiniLM Embeddings

---

### 3️⃣ Reasoning Agent

Responsibilities:

* Context analysis
* Recommendation generation
* Explainability generation
* Hallucination reduction

Technologies:

* Groq
* Llama 3.1

---

### 4️⃣ Response Agent

Responsibilities:

* Formatting output
* Confidence scoring
* Recommendation presentation
* User-facing explanations

---

# 🧩 Technology Stack

| Category         | Technologies     |
| ---------------- | ---------------- |
| LLM              | Llama 3.1        |
| Inference        | Groq             |
| Framework        | LangChain        |
| Vector Database  | ChromaDB         |
| Embeddings       | all-MiniLM-L6-v2 |
| Frontend         | Streamlit        |
| Language         | Python           |
| Containerization | Docker           |
| Orchestration    | Kubernetes       |
| Monitoring       | Grafana          |
| CI/CD            | GitHub Actions   |

---

# 📊 Performance Metrics

| Metric                | Performance            |
| --------------------- | ---------------------- |
| Vector Search Latency | < 15 ms                |
| LLM Response Time     | ~1.2 sec               |
| Embedding Dimensions  | 384                    |
| Dataset Size          | 14,000+ Records        |
| Retrieval Method      | Semantic Vector Search |
| Deployment            | Docker + Kubernetes    |
| Monitoring            | Grafana                |
| Scalability           | Production Ready       |

---

# 🚀 Engineering Achievements

✅ Built a complete Agentic RAG pipeline

✅ Implemented semantic search using vector embeddings

✅ Integrated Groq-powered LLM reasoning

✅ Reduced search latency below 15 milliseconds

✅ Designed explainable recommendation generation

✅ Built production-ready Docker deployment

✅ Added Kubernetes orchestration

✅ Integrated observability and monitoring

✅ Developed premium Streamlit dashboard

✅ Implemented persistent vector database storage

---

# 📂 Project Structure

```text
Agentic-RAG-Anime-Recommender-System/
│
├── Code/
│   ├── app/
│   ├── agents/
│   ├── retrieval/
│   ├── embeddings/
│   ├── ui/
│   └── utils/
│
├── Dataset/
│
├── assets/
│   ├── architecture/
│   ├── screenshots/
│   └── branding/
│
├── chroma_db/
│
├── llmops-k8s.yaml
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

---

# 🔄 RAG Pipeline

## Step 1: Data Ingestion

Anime metadata is loaded from CSV files.

## Step 2: Embedding Generation

Text descriptions are converted into dense vectors using:

all-MiniLM-L6-v2

## Step 3: Vector Indexing

Embeddings are stored inside ChromaDB using HNSW indexing.

## Step 4: Retrieval

Top-K semantically similar records are retrieved.

## Step 5: LLM Reasoning

Groq Llama 3.1 generates recommendations based on retrieved context.

## Step 6: Response Generation

Final recommendations are displayed with explanations.

---

# 📱 Application Modules

## 🎬 Demo Project

Core recommendation engine interface.

Features:

* Quick Search Categories
* Semantic Search
* Query History
* AI Explanations
* Download Results

---

## 📖 About Project

Project goals, architecture, and problem statement.

---

## 🛠️ Tech Stack

Technology breakdown and live system metrics.

---

## 🏗️ Architecture

Detailed HLD and LLD diagrams.

---

## 📋 System Logs

Real-time backend logs and monitoring.

---

# ☁️ Deployment Architecture

## Docker

```bash
docker build -t anime-rag .
docker run -p 8501:8501 anime-rag
```

## Kubernetes

```bash
kubectl apply -f llmops-k8s.yaml
```

## Streamlit Cloud

Automatic deployment through GitHub integration.

---

# 📈 Monitoring & Observability

Grafana integration provides:

* CPU Usage
* Memory Usage
* API Latency
* Request Tracking
* Error Monitoring
* Container Health

---

# 🛠️ Local Setup

## Clone Repository

```bash
git clone https://github.com/neekuujii2/Agentic-RAG-Anime-Recommender-System.git

cd Agentic-RAG-Anime-Recommender-System
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Linux / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

```env
GROQ_API_KEY=your_api_key
```

## Launch Application

```bash
streamlit run Code/app/premium_dashboard.py
```

---

# 💼 Skills Demonstrated

## AI / GenAI

* Agentic AI
* Retrieval-Augmented Generation
* Semantic Search
* Prompt Engineering
* Vector Databases
* LLM Integration
* Explainable AI

## Frameworks

* LangChain
* HuggingFace
* Streamlit

## LLMOps

* Docker
* Kubernetes
* CI/CD
* Monitoring
* Grafana
* GitHub Actions

## Backend

* Python
* REST APIs
* Data Processing
* Vector Search

---

# 🔮 Future Enhancements

* Multi-Agent LangGraph Workflow
* Hybrid Search (BM25 + Vector Search)
* User Memory Layer
* Recommendation Feedback Loop
* MCP Tool Integration
* Multimodal Search
* Image-Based Recommendations
* Streaming Responses
* Reinforcement Learning Ranking
* Agent-to-Agent Communication

---

# 👨‍💻 Author

## Neeraj Kumar 

AI/ML Engineer | Data Scientist | Agentic AI Developer

### Connect

LinkedIn:
[https://www.linkedin.com/in/Neeraj kumar](https://www.linkedin.com/in/neeraj-kumar-b12-datascienecist/)

GitHub:
https://github.com/neekuujii2


Kaggle:
[https://www.kaggle.com/neerajkumar75260](https://www.kaggle.com/neerajkumar75260)

Portfolio:
https://neeraj-kumar-aidevportfolio.vercel.app/

---

# ⭐ If you found this project useful

Please consider starring the repository and sharing feedback.

---

# 📜 License

This project is licensed under the MIT License.
