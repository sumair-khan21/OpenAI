import chainlit as cl
from agents import Runner
from my_agent.general_agent import agent  # Import the agent from your general_agent module

@cl.on_message
async def main(message: cl.Message):
    prompt = message.content
    
    
    res  = Runner.run_sync(agent, prompt)  # Run the agent with the user's input
    await cl.Message(content=res.final_output).send()
    

# uv run chainlit run chatbot.py  phle chainlit run hogi phr chatbot ki file run hogi





# new project aye toh 3 cheezen hongi
# input , output, prosessing 