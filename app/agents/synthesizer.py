from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_synthesizer_chain():
    prompt = PromptTemplate.from_template("""
    Synthesize the following research notes into a clear, concise summary:
    {research_notes}
    """)
    chain = LLMChain(llm=ChatOpenAI(), prompt=prompt)

    def wrapped(inputs):
        output = chain.run(inputs)  # returns a string
        return {"summary": output}  # ✅ wrap it in a dict!

    return wrapped
