
# handoff

# iska mtlb koi kam handover krna
# ek agent dosray agent ko apna kam de deta hai.
# is k ander ek main aget hota hai traif agent hota
# is k ander ek sub agent hota hay


from agents import Agent
from my_confg.gemini_confg import MODEL
# general agent hota hay
# speacilist agent
next_js_assistant = Agent(
    name="Next js Assistant",
    instructions="You are helpful next js assistant",
    model=MODEL,
)

python_assistant = Agent(
    name = "Python Assistant",
    instructions="you are helpful python assistant",
    model=MODEL
)



triage_agent = Agent(
    name="Triage Agent",
    instructions="You are heplful assiatant handoff the request to the correct agent according to query",
    model=MODEL,
    handoffs=[next_js_assistant,python_assistant]
)