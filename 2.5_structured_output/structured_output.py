from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model = 'llama3.2'
)



class Country(BaseModel):
    """Information about country"""

    name : str = Field(description="name of the country")
    language : str = Field(description="laguage of the country")
    capital : str = Field(description="capital of the country")

# print(llm.invoke("what is obama skin color?"))

structured_llm = llm.with_structured_output(Country)
print(structured_llm.invoke("France"))