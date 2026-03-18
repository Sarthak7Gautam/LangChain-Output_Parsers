from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import Optional, Literal
from comments import comment
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(model_name="llama-3.3-70b-versatile")


class Review(BaseModel):
    key_themes: list[str] = Field(description="Give the key themes of the review")
    summary: str = Field(description="Summarize the review in short")
    sentiment: Literal["pos", "neg", "neutral"] = Field(
        description="Provide the sentiment of the review"
    )
    pros: Optional[list[str]] = Field(
        default=None, description="Add the pros of the review in a list"
    )
    cons: Optional[list[str]] = Field(
        default=None, desciption="Add the cons of the description in a list"
    )


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(comment, max_tokens=200)

print(f"The key themes of the review are : {result.key_themes}")
print(f"The summary of the review is : {result.summary}")
print(f"The sentiment of the review is : {result.sentiment}")
print(f"The pros of the review are : {result.pros}")
print(f"The cons of the reviewer is : {result.cons}")
