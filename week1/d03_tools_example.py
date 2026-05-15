from langchain.tools import tool
@tool
def get_weather(city:str)->str:
    """Get the current weather for a city.
    
    Args:
        city:The name of the city
    """

    #Mock implementation
    weather_data={
        "bangalore":"Sunny, 28 C",
        "mumbai":"Rainy, 26 C",
        "delhi":"cloudy, 22 C"
    }
    return weather_data.get(city.lower(),"Weather data not available")

weather = get_weather.invoke("bangalore")
print(weather)