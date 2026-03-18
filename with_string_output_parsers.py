from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(temperature=1, model_name="llama-3.3-70b-versatile", max_tokens=200)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 points summary on the topic /n {text}", input_variables=["text"]
)

parser = StrOutputParser()

chains = template1 | model | parser | template2 | model | parser

result = chains.invoke({"topic": "LangChain Vs LangGraph"})

print(result)
