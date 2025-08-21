from agents import SQLiteSession,set_tracing_disabled,Runner
from all_agents.math_agent import math_agent
import asyncio


set_tracing_disabled(True)

async def main():
    my_session = SQLiteSession("mysession.1234", "my_conversation.db")
    prompt = input("Enter your question: ")
    res = await Runner.run(
        math_agent,
        prompt,
        session = my_session
    )
    print("Final Output", res.final_output)
    
    
    prompt = input("Enter your next Qus: ")
    res = await Runner.run(
        math_agent,
        prompt,
        session = my_session
    )
    print("Final Output", res.final_output)
    
    
asyncio.run(main())
    
    
    

