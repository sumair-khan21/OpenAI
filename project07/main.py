from agents import Runner,set_tracing_disabled
from all_agents.general_agent import generatl_asssiatant_agent

set_tracing_disabled(True)
res = Runner.run_sync(
    starting_agent= generatl_asssiatant_agent,
    input="Hello, What is the capital of Pakistan?",
    # output_type="general",

)

print(res.final_output)