from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def get_reporter_chain():
    prompt = PromptTemplate.from_template("""
    Format this research into a professional report with title, sections, and conclusion.
    Research Summary: {summary}
    """)
    chain = LLMChain(llm=ChatOpenAI(), prompt=prompt)

    # 🔧 Wrap output so LangGraph state gets updated correctly
    def wrapped(inputs):
        output = chain.run(inputs)
        return {"report": output}

    return wrapped
