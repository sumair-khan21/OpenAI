from agents import Runner, set_tracing_disabled
from my_agents.helper_agent import helper_agent, math_agent
from my_agents.agnet import agent
from data.user_data import user_data



set_tracing_disabled(True)
# result = Runner.run_sync(math_agent, "What is the square root of 16?")
# # result = Runner.run_sync(helper_agent, "mujhe pakistan ka map batao")
# print(result.final_output)

res = Runner.run_sync(agent, "user ki age batao?", context=user_data)
print(res.final_output)
