from agents import Agent
from my_confg.gemini_confg import MODEL  # Import the model configuration
from my_tools.weather_tool import fetch_weather  # Import the weather fetching tool

weather_agent = Agent(
    name = "Weather Assistant",
    instructions = "You are a helpful assistant that provides weather information.", # persona
    model = MODEL,  # Specify the model you want to use
    tools = [fetch_weather]
)


# hellosenation means k khud se hi LLM data de deta hay