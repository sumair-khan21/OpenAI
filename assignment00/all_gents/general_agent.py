from agnets import Agent
from confg.gemini_confg import MODEL



generatl_asssiatant_agent = Agent(
        name="General Assistant",
       description="A general assistant that can help with a wide range of tasks.",
       model=MODEL
       )

math_agent = Agent(
        name="Math Agent",
        description="An agent that can help with mathematical calculations and problems.",
        model=MODEL 
         )