from langchain_ollama import ChatOllama
from langchain.agents import initialize_agent, tool
from langchain_community.tools import TavilySearchResults

from dotenv import load_dotenv
load_dotenv()

search_tool = TavilySearchResults()

@tool
def get_time(format: str = "%Y-%m-%d") -> str:
    """Get the current time."""
    return "2023-10-01"

llm = ChatOllama(
    model = "llama3.2"
)

agent = initialize_agent(
    tools=[get_time],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

agent.invoke("what time is it now?")