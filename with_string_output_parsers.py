from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.parsers import StrOutputParser

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b", task="text-generation"
)

llm = ChatHuggingFace(llm=model)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 lines summary on the topic /n {text}", input_variables=["text"]
)

parser = StrOutputParser()

chains = template1 | model | parser | template2 | model | parser

result = chains.invoke({'topic':'Black Hole'})

print(result.content)
