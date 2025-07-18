from agents import set_tracing_disabled, Runner
from my_agents.hepler_agent import agent
from my_agents.handoff_agnet import triage_agent
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

set_tracing_disabled(True)
# result = Runner.run_sync(agent, "plus karo 200 ko 100 se")
# result = Runner.run_sync(triage_agent, 
#          input="mujhe next js ki routin k hawlay se help chahiye complete answer roman english m dena"
#          )

async def main():
 result = Runner.run_streamed(triage_agent, 
         input="what is next js in one line"
         )

 async for event in result.stream_events():
     if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
        print("output",event.data.delta)
    
asyncio.run(main())

# print("last agent===>",result.last_agent)
# print("final output",result.final_output)


# runner k teeno method dekhne hain
# Runner.run_sync
# Runner.run
# Runner.run_streamed