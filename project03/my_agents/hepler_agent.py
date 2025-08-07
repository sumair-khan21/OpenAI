
from agents import Agent,ModelSettings
from my_confg.gemini_confg import MODEL
from my_tool.my_tool import multiply,subtract,plus
from my_schema.agent_output import MyDataOutput
from dataclasses import dataclass
from agents.agent import StopAtTools



       
math_agent = Agent(name = "Gulzari Lal",
instructions="You are a helpful assistant. Answer the user's questions to the best of your ability.",
model=MODEL,
tools=[plus,subtract],
model_settings=ModelSettings(tool_choice="required"),
)


agent = Agent(name = "Ratan Lal",
instructions="You are a helpful assistant. Answer the user's questions to the best of your ability.",
model=MODEL,
# tools = [multiply,subtract], tool_use_behavior= "stop_on_first_tool",
# tools = [multiply,subtract,plus], 
# tool_use_behavior= StopAtTools(stop_at_tool_names=["subtract"]),
# model_settings=ModelSettings(tool_choice   ="required"), # teen setting hoti hain auto, none,required
# output_type=MyDataOutput
# output_type=MyData
tools=[math_agent.as_tool(tool_name="math_agent",tool_description="you are the math teacher")],
)

 
# LLM se jo bhi answer ata hy wo string m hota hay
# tool setting means k isko batate hain k tool call krna hay ya nhi






