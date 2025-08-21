from agents import Agent
from my_confg.gemini_confg import MODEL
from agents import function_tool



@function_tool
def get_weather(city: str) -> str:
    print("tool fire =============>")
    """Get the weather of a city"""
    return f"The weather of {city} is sunny"



general_agent = Agent(
    name = "General Agent",
    instructions = "You are the general agent that can answer questions and help with tasks",
    model= MODEL
)



python_agent = Agent(
    name = "Python Agent",
    instructions = "You are the python agent that can answer questions and help with tasks",
    model= MODEL
)



javascript_agent = Agent(
    name = "Javascript Agent",
    instructions = "You are the javascript agent that can answer questions and help with tasks",
    model= MODEL
)





triage_agent = Agent(
    name = "Triage Agent",
    instructions= "You are helpfull assiatnt handoff the request to the correct agent accoriding to the query",
    model=MODEL,
    handoffs=[python_agent,javascript_agent,general_agent],
    tools=[get_weather],
    tool_use_behavior="run_llm_again"
)





