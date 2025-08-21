from agents import Runner,set_tracing_disabled
from all_agents.helper_agent import helper_agent


set_tracing_disabled(True)
res =  Runner.run_sync(starting_agent=helper_agent,input="What is the capital of Pakistan?")
print(res.final_output)