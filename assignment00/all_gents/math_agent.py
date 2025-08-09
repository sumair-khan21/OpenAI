from agents import Agent
from confg.gemini_confg import MODEL
from all_tools.subtarct_tool import subtract






math_agent = Agent(
        name="Math Agent",
        description="An agent that can help with mathematical calculations and problems.",
        model=MODEL,
        tools=[subtract],
        input_type="math",
         )