from agents import Runner,set_tracing_disabled
# from all_agnets.helper_agent import agent
import chainlit as cl
from all_agnets.handoff_agent import triage_agent
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
import json


set_tracing_disabled(True)


# =======================================================================================
# # chainlit integrated
# @cl.on_chat_start
# async def start():
#     await cl.Message(content="Hello, how can I help you today?").send()





# @cl.on_message
# async def start(Message: cl.Message):

#     res = await Runner.run(triage_agent, Message.content)
#     await cl.Message(content=res.final_output).send()


# =====================================================================================

# result = Runner.run_sync(starting_agent = triage_agent, input= "what is the weather of karachi?")
# print(result.final_output)
# print("last agent============>",result.last_agent)


# result = Runner.run_sync(starting_agent = triage_agent, input= "what is the weather of karachi?")

# print("\n--- Final Result (as JSON) ---")
# print(json.dumps({"output": result.final_output}, indent=2))


# print("\n--- Last Agent (as JSON) ---")
# print(json.dumps(vars(result.last_agent), indent=2, default=str))



# =====================================================================================





# chainlit integration
@cl.on_chat_start
async def start():
    await cl.Message(content="Hello, how can I help you today?").send()

@cl.on_message
async def main(Message: cl.Message):
    res = Runner.run_streamed(
        starting_agent = triage_agent, 
        input= Message.content
    )
    async for event in res.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            # print(event.data.delta)
            await cl.Message(content=event.data.delta).send()

    # print("final output==========>",res.final_output)
    # print("last agent========>",res.last_agent)


asyncio.run(main())






# ==========================================================================================
# today class code

# res = Runner.run_sync(
#     starting_agent = agent,
#     input = "100-20=?",
#     context={"name":"atma raam", "age":2, "role":"teacher"}
# )

# print(res.final_output)



# runner ka loop jb ktm hota jb hame final answer aata hai
# assignment 




































