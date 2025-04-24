# 🔍 InsightFlow – Autonomous LLM Research Assistant

**InsightFlow** is a production-ready research automation tool powered by **LangGraph** and **LangChain**. It uses multi-agent orchestration, stateful workflows, and Retrieval-Augmented Generation (RAG) to autonomously generate comprehensive research reports from user prompts.

---

## 🧠 Key Features

- 🔁 **LangGraph-Powered Workflows** – Orchestrates autonomous research steps using stateful DAGs.
- 🤖 **Multi-Agent System** – Planner, Researcher, Synthesizer, and Reporter agents collaborate to perform deep research.
- 📚 **Retrieval-Augmented Generation (RAG)** – Incorporates information from documents, web search, and vector databases (FAISS/Pinecone).
- 🌐 **FastAPI Backend** – Exposes endpoints for research automation, deployable via Docker and AWS ECS.
- 📊 **Cloud-Ready** – Built with modularity and AWS-native deployment in mind (Lambda, ECS, CloudWatch, S3).
- 🧾 **Structured Output** – Generates well-formatted reports with summaries, references, and insights.

---

## 🚀 Architecture Overview

```
User Prompt
   ↓
[Planner Agent] → Breaks question into subtopics
   ↓
[Researcher Agent] → Queries web & vector DB
   ↓
[Synthesizer Agent] → Summarizes and combines info
   ↓
[Reporter Agent] → Formats final report
   ↓
Structured Report Output
```

---

## 🛠️ Tech Stack

- **LangGraph** – Agent coordination and memory/state control
- **LangChain** – LLM abstraction, tool & agent integration
- **OpenAI API** – Foundation LLM (e.g., GPT-4)
- **FAISS** – Local vector storage (or Pinecone for cloud)
- **FastAPI** – RESTful API interface
- **Docker** – Containerized deployment
- **AWS ECS / Lambda** – Scalable deployment options

---

## 📦 Installation

```bash
git clone https://github.com/your-username/insightflow.git
cd insightflow
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧪 Run Locally

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧰 API Endpoint

```http
GET /research?topic="The impact of AI on healthcare"
```

---

## 🔜 Coming Soon

- Streamlit Frontend
- Long-term Memory with LangGraph
- Airflow DAGs for Scheduled Research
- AWS Cloud Deployment (ECS + S3 + CloudWatch)
- Slack/Discord Bot Integration

---

## 📄 License

MIT License

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork this repo and propose improvements.

---

## 📬 Contact

For questions or collaboration:
- [Narendar Punithan](akashnarendar2013@gmail.com)
- [LinkedIn Profile](https://www.linkedin.com/in/narendar-punithan-758658126/)
