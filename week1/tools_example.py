from langchain.tools import tool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent



load_dotenv()
@tool
def best_food(city: str) -> str:
    """Get the best food for a city.
    
    Args:
        city: The name of the city
    """
    # Mock implementation
    food_data = {
        "Bangalore": "Masala Dosa",
        "Mumbai": "Vada Pav",
        "Delhi": "Chaat",
        "Mysore":"Mysore Pak"
    }
    return food_data.get(city,"city data not available")

@tool
def calculate_shipping_cost(weight_kg:float,destination:str,express:bool=False)->dict:
    """calculate the shipping cost for a package.
    Args:
        weight_kg: The weight of the package in kilograms(float)
        destination: The destination of the package (string) (US, UK, Canada, Australia, etc.)
        express: Whether the shipping is express (boolean)
    Returns:
        A dictionary with shipping cost with 'cost_usd' and the estimated delivery time with 'shipping_days'
    """
    base_rate={"india":5,"usa":10,"uk":15}.get(destination.lower().strip(),20)
    express_fee = 10 if express else 0
    cost_usd = base_rate *weight_kg + express_fee
    shipping_days = 5 if express else 7
    return {"cost_usd":cost_usd, "shipping_days":shipping_days}

llm = ChatGroq(model="llama-3.1-8b-instant",temperature=0)

agent= create_agent(model=llm,tools=[best_food,calculate_shipping_cost,],system_prompt="You are a helpful assistant that can answer questions in a funny manner.")

# response1= agent.invoke({"messages":[{"role":"user","content":"What is the best food in delhi?"}]})
# print("<--------------------------------------->")
# print(response1["messages"][-1].content)

response12= agent.invoke({"messages":[{"role":"user","content":"how much will it cost to ship a package of 10 kg to USA?"}]})

print("------------------------------>")
print(response12["messages"][-1])