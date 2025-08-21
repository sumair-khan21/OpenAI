from agents import Agent
from confg.gemini_confg import MODEL


helper_agent = Agent(
    name = "Helper Agent",
    instructions="Your are the helper agent yo help out any of the query.",
    model=MODEL
)


