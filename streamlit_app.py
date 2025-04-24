import streamlit as st
from app.chains.research_flow import build_research_flow

# Build the workflow once
workflow = build_research_flow()

st.set_page_config(page_title="InsightFlow Research Assistant", layout="centered")
st.title("🔍 InsightFlow")
st.markdown("""
Welcome to **InsightFlow** — your intelligent research companion powered by a LangGraph-based LLM agent framework.

Simply enter a research topic or complex question, and InsightFlow will:

1. 🧩 **Break it down** into manageable subtopics using an autonomous planner agent  
2. 🔍 **Conduct targeted research** for each subtopic (web search or RAG-ready)  
3. ✍️ **Summarize findings** using advanced LLM synthesis  
4. 📰 **Generate a structured research report** — clear, concise, and insightful

This tool demonstrates multi-agent LLM orchestration, real-time tracing (LangSmith), and modular AI reasoning.

> Built with LangChain, LangGraph, OpenAI, and Streamlit.
""")

topic = st.text_input("Enter your research topic:")

if st.button("Run Research") and topic:
    with st.spinner("Running multi-agent research..."):
        result = workflow.invoke({"question": topic})
        
        st.subheader("🧠 Question")
        st.write(result.get("question"))

        st.subheader("📋 Plan")
        st.write(result.get("plan"))

        st.subheader("🔎 Research Notes")
        st.write(result.get("research_notes"))

        st.subheader("🧾 Summary")
        st.write(result.get("summary"))

        st.subheader("📄 Final Report")
        st.markdown(result.get("report"))
