from dotenv import load_dotenv
load_dotenv()


#os is used to access environment variables and perform file system operations
import os
#requests is used to make HTTP requests
import requests
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool 
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

#Now we willl build some tools

#weather tool


def get_weather(city : str) -> str:
    """
    Get the weather for a given city.
    """
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    print("Debug", data)

    if str(data.get("cod")) != "200":
        return f"Could not retrieve weather data for {city}. Please check the city name and try again."

    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    
    return f"The weather in {city} is {description} with a temperature of {temperature}°C."

print(get_weather("Bangalore"))