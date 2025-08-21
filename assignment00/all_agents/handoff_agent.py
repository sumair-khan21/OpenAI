from agents import Agent,handoff
from confg.gemini_confg import MODEL
from agents.extensions import handoff_filters


javascript_agent = Agent(
    name= "javascript Agent",
    instructions="you are a javascript agent, you are designed to assist with javascript programming tasks and provide solutions.",
    model=MODEL
)



python_agent = Agent(
    name= "Python Agent",
    instructions="you are a Python agent, you are designed to assist with Python programming tasks and provide solutions.",
    model=MODEL
)



def on_handoff_function(context):
    print("on_handoff_function===================> ")
    print(context)
    
    
    
python_handoff = handoff(
    agent = python_agent,
    tool_name_override="handoff_to_python_agent",
    input_filter=handoff_filters.remove_all_tools,
    on_handoff=on_handoff_function   
)


triage_agent = Agent(
    name="triage Agent",
    instructions = "you are a triage agent, you are designed to triage the user's request and determine which agent to hand off to.",
    model=MODEL,
    handoff=[javascript_agent,python_handoff],
)
