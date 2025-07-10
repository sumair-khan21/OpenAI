from agents import Agent
from my_confg.gemini_confg import MODEL
from my_tools.my_tool import plus,multiply  # Import the custom tool

agent = Agent(name= "Ratan Lal", instructions= "You are a helpful assistant. Answer the user's questions to the best of your ability.", model=MODEL,tools=[plus,multiply], tool_use_behavior= "stop_on_first_tool")  # Add tools if needed

# tool_use_behavior= "run_llm_again" # will run the LLM again if no tool is used

# tool_use_behavior= "stop_on_first_tool" # will stop after the first tool is used
