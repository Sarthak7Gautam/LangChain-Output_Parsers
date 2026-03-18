from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional,Literal
from comments import comment

load_dotenv()

model = ChatGroq(model_name="llama-3.3-70b-versatile")


class Review(TypedDict):
    key_themes: Annotated[list[str], "Give the key themes of the review in a list"]
    summary: Annotated[str, "Generate the summary of the Review in short"]
    sentiment: Annotated[
        Literal["pos","neg","neutral"], "Give the Sentiment of the Review"
    ]
    pros: Annotated[Optional[list[str]], "List down all the Pros"]
    cons: Annotated[Optional[list[str]], "List down all the Cons"]
    name:Annotated[Optional[str],"Write the name of the reviewer"]


structured_model = model.with_structured_output(Review)


result = structured_model.invoke(comment, max_tokens=200)

print(f"The key themes of the review are : {result['key_themes']}")
print(f"The summary of the review is : {result['summary']}")
print(f"The sentiment of the review is : {result['sentiment']}")
print(f"The pros of the review are : {result['pros']}")
print(f"The name of the reviewer is : {result['name']}")
