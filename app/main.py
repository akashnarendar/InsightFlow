from fastapi import FastAPI, Query
from app.chains.research_flow import build_research_flow
import app.config

app = FastAPI()
workflow = build_research_flow()

@app.get("/research")
def research(topic: str):
    result = workflow.invoke({"question": topic})
    return {
        "question": result.get("question"),
        "plan": result.get("plan"),
        "research_notes": result.get("research_notes"),
        "summary": result.get("summary"),
        "report": result.get("report"),  # ✅ Add this line to include final report!
    }
