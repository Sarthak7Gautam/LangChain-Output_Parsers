from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    temperature=1, model_name="llama-3.3-70b-versatile", max_tokens=200
)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 lines summary on the topic \n {text}", input_variables=["text"]
)

prompt1 = template1.invoke({"topic": "Black Hole"})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result1.content})

result2 = model.invoke(prompt2)

print(result2.content)
