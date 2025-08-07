from agents import function_tool, RunContextWrapper,FunctionTool,Runner,Agent,set_tracing_disabled, SQLiteSession
import asyncio
from my_confg.gemini_confg import MODEL

set_tracing_disabled(True)

@function_tool
def get_weather(city):
    """get the weather of a city"""
    return f"the weather of {city} is sunny"


agent = Agent(
        name="helper_agent",
        instructions="you are a helper agent",
        # tools=[get_weather]
        tools=[get_weather],
        tool_use_behavior="stop_tool_use",
        model=MODEL,
        # context={"name":"atma raam"}
    )



# ==================================================================================
#  ye code ko run krne k liye ye code ko uncomment krne hai ye old tareeka hay  

# async def main():
    # res = await Runner.run(agent, "what is the weather of delhi")
    # print(res.final_output)
    # print("last_agent===========>",res.last_agent)
    # print("res.to_input_list()===========>",res.to_input_list())


#     prompt = input("enter your prompt: ")
#     res = await Runner.run(agent, prompt)
#     print(res.final_output)

#     prompt = input("enter your prompt: ")
#     new_prompt = res.to_input_list() + [{"role":"user", "content":prompt}]
#     res = await Runner.run(agent, new_prompt)
#     print(res.final_output)


# if __name__ == "__main__":
#     asyncio.run(main())


# ==================================================================================


# state manage kr rha hai  means k porana code isko yd rahega
async def main():
                                            #   my_conversation ab ye db mai save hoga 
    my_session = SQLiteSession("mysession.123", "my_conversation.db")
    prompt = input("enter your prompt: ")
    res = await Runner.run(agent, prompt,session=my_session)
    print(res.final_output)

    prompt = input("enter your prompt: ")
    res = await Runner.run(agent, prompt,session=my_session)
    print(res.final_output)


if __name__ == "__main__":
    asyncio.run(main())

