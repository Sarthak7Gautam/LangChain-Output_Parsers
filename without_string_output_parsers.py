from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = HuggingFaceEndpoint(repo_id="openai/gpt-oss-20b", task="text-generation",max_new_tokens=200)

llm = ChatHuggingFace(llm=model)

template1 = PromptTemplate(template = 'Write a detailed report on {topic}',
                           input_variables = ['topic'])

template2 = PromptTemplate(template = "Write a 5 lines summary on the topic \n {text}",
                           input_variables = ['text'])

prompt1 = template1.invoke({'topic':'Black Hole'})

result1 = llm.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})

result2 = llm.invoke(prompt2)

print(result2.content)









