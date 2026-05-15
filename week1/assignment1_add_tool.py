from langchain.tools import tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain.agents import create_agent
load_dotenv()

@tool
def best_food(city:str)->str:
    """
    Get the best food for a city.

    Args:
        city:The name of the city
    """
    #Mock implementation
    weather_data={
        "Bangalore":"Masala Dosa",
        "Mumbai":"Vada Pav",
        "Delhi":"Chaat",
        "Mysore":"Mysore Pak"
    }
    return weather_data.get(city.lower(),"Weather data not available")


llm = ChatOpenAI(model="gpt-4.1-nano")

agent = create_agent(model=llm,
                     tools=[best_food],
                     system_prompt="You are a helpful assistant that can answer questions in funny manner")
response1 = agent.invoke({"messages":[{"role":"user","content":"What is the best food in Banglore?"}]})
print(response1)

