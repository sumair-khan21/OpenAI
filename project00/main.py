# print("Hello world!")


# AGENT
# aj agent banana hay.

# ek agent ko ek kaam diya jata hai.# agent ko kaam karne ke liye kuch tools diye jate hain.
# agent ek temporary memory rakhta hai.# agent ko ek goal diya jata hai.
# agent ko ek plan banana hota hai.
# LLM means large language model.
# hum jo LLM use karege wo openAI ka SDK use karenge

# UV kia hy?
# UV ek package manager hay jis tarha npm hota hay.
# UV ko install karne ke liye hum pip use karte hain.
# UV ko install karne ke liye hum command prompt ya terminal me ye command likhte hain:
# pip install uv
# uv init install ho jayega
# uv pip list packages ka command hota hai. k btata k k kitne packages install hain.
# .venv ye esa hy jese node_modules hote hain uv ko run krne k liye kuch important files
# openAi install krne ki command 
# uv add openai-agents
# python-decouple 3.8 ye python ki library hy  iska kam just itna hay k .env se credentials ko read kar sake.
# uv add python-decouple command
# llm abi hum ai studio se use karenge.
# .env file me hum apne credentials rakhte hain.
# GEMINI_API_KEY ye ishi naam se rahegi api ka naam kyun k hum isko use karenge.
# ab gemini ka model lena hay 2.0
# AsyncOpenAI ye isliye import kiya hy k open AI synchronous hai hame asynchronous kam krna hy.
# base url ye google ka base url hai jahan se hum gemini ka model use karenge.
# OpenAIChatCompletionsModel ye agent ka model hai jo hum use karenge.







# ======================================================================
from agents import Runner
import asyncio
from my_agents.teachers import math_teacher_agent, english_teacher_agent, python_teacher_agent

# enable_verbose_stdout_logging()

async def main():
    # Runner ye class hy ye agent ko run karne ke liye use hoti hai.
    result = await Runner.run(python_teacher_agent, "write a table using javascript just give me the table of number 5. do not give me the explaination of the code. just give me the code.",)
    print(result.final_output)


asyncio.run(main())





