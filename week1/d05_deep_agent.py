from langchain.tools import tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain.agents import create_agent
from deepagents import create_deep_agent
from tavily import TavilyClient
from typing import Literal
import os
load_dotenv()



llm = ChatOpenAI(model="gpt-4.1-nano",seed=6)

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )

agent = create_deep_agent(model=llm,
                    tools = [internet_search],
                    system_prompt = "You are a helpful assistant that can answer questions in a funny manner. You can use the internet to search for information.")


response3 = agent.invoke({"messages": [
    {"role": "user", "content": "Who won the recent F1 race that happened on March 29, 2026"}
]})

print("--------------------------------")
print(response3)
