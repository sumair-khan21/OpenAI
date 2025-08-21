

from agents import Agent
from my_confg.gemini_confg import MODEL
from my_tools.tools import get_user_age
agent = Agent(
    name="my_agent",
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
    model=MODEL,
    tools=[get_user_age],
)







