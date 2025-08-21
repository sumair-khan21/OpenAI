from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    set_default_openai_api,
    set_default_openai_client,
    RunConfig,
    ModelSettings,
    function_tool,
)
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
import os
import asyncio

load_dotenv(find_dotenv(), override=True)
set_tracing_disabled(True)
set_default_openai_api("chat_completions")
api_key = os.getenv("GEMINI_API_KEY")
base_path = os.getenv("GEMINI_BASE_PATH")
model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(api_key=api_key, base_url=base_path)
set_default_openai_client(client)
# model = OpenAIChatCompletionsModel(openai_client=client, model=str(model_name))

# math_agent: Agent = Agent(
#     name="Math Agent",
#     instructions="""
#     - You are a Math Agent and your task is to solve math problems. 
#     - define your solution step by step.
#     - DO NOT reply if the question is not related to math.
#     - Do NOT generate answer if question are other then math problems or you can simply say I don't know about this".
#     """,
# )



@function_tool(name_override="get_weather_info", description="Get the current weather for a specified city.")
def get_weather(city):
    # This function would contain logic to get weather information for the given city
    return f"The weather in {city} is sunny with a high of 25°C and a low of 15°C."

@function_tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


math_agent: Agent = Agent(
    name="HelpFul General Agent",
    instructions="""
    You are a helpful general agent, you can use tools to get the weather of city .
    """,
    model="gemini-2.0-flash",
    model_settings=ModelSettings(tool_choice="auto"),
    tools=[get_weather, add],
)

# physics_agent: Agent = Agent(
#     name="Physics Agent",
    # instructions="Physics Agent is a physics tutor who can solve physics problems.",
# )

config = RunConfig(
    model="gemini-2.0-flash",
)
prompt = input("Enter your question : ")
result = Runner.run_sync(math_agent, prompt, run_config=config)
print(result.final_output)


# Example usage of the get_weather function




print(Agent.tools[0])

# city_name = input("Enter the city name: ")
# weather_info = get_weather(city_name)
# print(f"Weather information for {city_name}: {weather_info}")