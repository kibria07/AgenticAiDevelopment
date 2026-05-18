from langgraph.graph import StateGraph, START, END
from typing import TypedDict


# Define the state of the graph
class ExampleState(TypedDict):
    query: str
    weather: str
    booking: str

# define nodes
def check_weather_node(state):
    return {"weather": "sunny"}

def book_flight_node(state):
    print("Current state: ", state)
    return {"booking": "flight booked"}

# Build the graph
workflow = StateGraph(ExampleState)
workflow.add_node("check_weather", check_weather_node)
workflow.add_node("book_flight", book_flight_node)

# add the edges
workflow.add_edge(START, "check_weather")
workflow.add_edge("check_weather", "book_flight")
workflow.add_edge("book_flight", END)

# compile the graph
compiled_graph = workflow.compile()

# run the graph
response = compiled_graph.invoke({"query": "What is the weather in Bangalore?"})
print(response)