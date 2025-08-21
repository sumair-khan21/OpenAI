from agents import set_tracing_disabled, Runner,ItemHelpers
from my_agents.hepler_agent import agent
from my_agents.handoff_agnet import triage_agent
import asyncio
from openai.types.responses import ResponseTextDeltaEvent



set_tracing_disabled(True)
# result = Runner.run_sync(agent, "plus karo 200 ko 100 se")
# result = Runner.run_sync(triage_agent, 
#          input="mujhe next js ki routin k hawlay se help chahiye complete answer roman english m dena"
#          )

# async def main():
#  result = Runner.run_streamed(triage_agent, 
#          input="what is supabase database?"
#          )

#     result = await Runner.run_sync(
#         starting_agent= triage_agent,
#         input="what is the weather in delhi? and what is python?")


# print("last agent===>",result.last_agent)
# print("final output",result.final_output)




# #  async for event in result.stream_events():
# #      if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
# #         # print("output",event.data.delta)

# #         continue
# #      elif event.type == "agent_updated_stream_event":
# #         print(event)
# #         continue
            #  jb koi pora action perform hoga ya events
# #      elif event.type == "run_item_stream_event":
# #         # print(event)
# #         if event.item.type == "message_output_item":
# #                 print(ItemHelpers.text_message_output(event.item))

    
#           asyncio.run(main())

# print("last agent===>",result.last_agent)
# print("final output",result.final_output)


# runner k teeno method dekhne hain
# Runner.run_sync
# Runner.run
# Runner.run_streamed











import asyncio
import nest_asyncio
nest_asyncio.apply()

async def main():
    # Option 1: Streamed output (commented)
    result = Runner.run_streamed(triage_agent, input="what is supabase database?")

    # Option 2: Sync-style run (used here)
    # result = Runner.run_sync(
    #     starting_agent=triage_agent,
    #     input="what is the weather in delhi? and what is python?"
    # )

    print("last agent ===>", result.last_agent)
    print("final output:", result.final_output)

    # Optional: Streamed events (if you want to show intermediate outputs)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            continue
        elif event.type == "agent_updated_stream_event":
            print(event)
            continue
        elif event.type == "run_item_stream_event":
            if event.item.type == "message_output_item":
                print(ItemHelpers.text_message_output(event.item))

# Run main safely
asyncio.get_event_loop().run_until_complete(main())
