from agents import Agent
from confg.gemini_confg import MODEL



generatl_asssiatant_agent = Agent(
        name="General Assistant",
       description="A general assistant that can help with a wide range of tasks.",
       model=MODEL,
       input_type="general",
       )
