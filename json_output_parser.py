from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(temperature=1, model_name="llama-3.3-70b-versatile", max_tokens=200)

parser = JsonOutputParser()

template1 = PromptTemplate(
    template="Give 5 facts about {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables= {'format_instructions':parser.get_format_instructions()}
) 

## Either use these 
# prompt = template1.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

## Or

chain = template1 | model | parser

result = chain.invoke({'topic':'Australia'})

print(result)