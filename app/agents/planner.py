from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
import app.config  # 👈 Ensures .env is loaded

llm = ChatOpenAI(temperature=0.2)

def get_planner_chain():
    template = """
    You are a research planner. Break down the research question into 3-5 subtopics.
    Question: {question}
    """
    prompt = PromptTemplate.from_template(template)
    return LLMChain(llm=llm, prompt=prompt)
