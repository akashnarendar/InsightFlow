from langchain.agents import Tool

def get_research_tool():
    return Tool(
        name="Web Search",
        func=lambda q: {"research_notes": f"Searching for: {q}"},  # ✅ return dict with correct key
        description="Useful for searching facts online."
    )
