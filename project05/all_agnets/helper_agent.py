from agents import Agent
from my_confg.gemini_confg import MODEL
# from all_tools.my_tools import plus,subtract
from instruction.dynamic_instruction import dynamic_instruction



agent = Agent(
    name= "helper Agent",
    instructions= dynamic_instruction,  
    model= MODEL,
    # tools = [subtract]
)



# pata krte hain ki agent kis tool ko use karega
print(agent.tools)