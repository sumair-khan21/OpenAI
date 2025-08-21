from agents import Agent  
from confg.gemini_confg import MODEL  
from guadrial_function.guadrial_input_function import guadrial_input_function


general_asssiatant_agent = Agent(
    name="General Assistant",
    instructions="A general assistant that can help with a wide range of tasks.",
    model=MODEL
)

math_agent = Agent(
    name="Math Agent",
    instructions="An agent that can help with mathematical calculations and problems.",
    model=MODEL
)



hotel_asssiatant = Agent(
    name="hotel asssiatant",
    instructions="An agent that can help with hotel asssiatant sannata agent and problems.  hotel owner name ratan lal and the room availale is 200",
    model=MODEL,
    input_guardrails=[guadrial_input_function],
    
)
