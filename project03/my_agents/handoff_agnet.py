
# handoff

# iska mtlb koi kam handover krna
# ek agent dosray agent ko apna kam de deta hai.
# is k ander ek main aget hota hai traif agent hota
# is k ander ek sub agent hota hay

from agents.extensions import handoff_filters
from agents import Agent, handoff, function_tool
from my_confg.gemini_confg import MODEL
# general agent hota hay
# speacilist agent
# next_js_assistant = Agent(
#     name="Next js Assistant",
#     instructions="You are helpful next js assistant",
#     model=MODEL,
# )


@function_tool
async def fetch_weather(city:str):
    return f"The weather in {city} is sunny"



    

next_js_assistant = Agent(
    name="Supabase Assistant",
    instructions="You are helpful supabase assistant",
    model=MODEL,
)

python_assistant = Agent(
    name = "Python Assistant",
    instructions="you are helpful python assistant",
    model=MODEL
)


def on_handoff_function(context):
    print("hey kem cho!",context)

# Agnet Name - Python Assistant
# hand off name = transfer_to_python_assistant
python_handoff = handoff(
   agent=python_assistant,
   tool_name_override="handoff_to_python_assistant",
   on_handoff=on_handoff_function,
   input_filter=handoff_filters.remove_all_tools    # ek agent se dosray egnt per histroy pas ho jati hay hostroy ko filter krne k liye
    
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You are heplful assiatant handoff the request to the correct agent according to query",
    model=MODEL,
    handoffs=[next_js_assistant,
              python_handoff
    ],
    tools=[fetch_weather]
)