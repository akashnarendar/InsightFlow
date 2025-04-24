from langgraph.graph import StateGraph, END
from app.agents.planner import get_planner_chain
from app.agents.researcher import get_research_tool
from app.agents.synthesizer import get_synthesizer_chain
from app.agents.reporter import get_reporter_chain
from typing import TypedDict


class ResearchState(TypedDict):
    question: str
    plan: str
    research_notes: str
    summary: str
    report: str

def build_research_flow():
    planner = get_planner_chain()
    researcher = get_research_tool()
    synthesizer = get_synthesizer_chain()
    reporter = get_reporter_chain()
    
    graph = StateGraph(ResearchState)   # 👈 Provide the state schema
    graph.add_node("Plan", planner)
    graph.add_node("Research", researcher)
    graph.add_node("Synthesize", synthesizer)
    graph.add_node("Report", reporter)

    graph.set_entry_point("Plan")
    graph.add_edge("Plan", "Research")
    graph.add_edge("Research", "Synthesize")
    graph.add_edge("Synthesize", "Report")
    graph.add_edge("Report", END)

    return graph.compile()

