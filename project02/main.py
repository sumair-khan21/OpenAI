from agents import  Runner, set_tracing_disabled, enable_verbose_stdout_logging
from my_agent.general_agent import agent
from my_agent.weather_agent import weather_agent

# uv add openai-agents
# Hosted tools bane banaye tools hay isko just call krna hy wo kam kr k dega bht saray tools hote hain lie websearching, filesearching, etc.

# tools
# OpenAI offers a few built-in tools when using the OpenAIResponsesModel:
# The WebSearchTool lets an agent search the web.
# The FileSearchTool allows retrieving information from your OpenAI Vector Stores.
# The ComputerTool allows automating computer use tasks.
# The CodeInterpreterTool lets the LLM execute code in a sandboxed environment.
# The HostedMCPTool exposes a remote MCP server's tools to the model.
# The ImageGenerationTool generates images from a prompt.
# The LocalShellTool runs shell commands on your machine.



# from agents import Agent, FileSearchTool, Runner, WebSearchTool

# agent = Agent(
#     name="Assistant",
#     tools=[
#         WebSearchTool(),
#         FileSearchTool(
#             max_num_results=3,
#             vector_store_ids=["VECTOR_STORE_ID"],
#         ),
#     ],
# )

# async def main():
#     result = await Runner.run(agent, "Which coffee shop should I go to, taking into account my preferences and the weather today in SF?")
#     print(result.final_output)



# https://openai.github.io/openai-agents-python/tools/


# =====================================================================================
# simple agents run
# set_tracing_disabled(True)  # Disable tracing if not needed
# enable_verbose_stdout_logging()  # Enable verbose logging to stdout
# result = Runner.run_sync(agent, "plus karo 2 or 3 ka")  # Example input to the agent

# print(result.final_output) 


# =====================================================================================
# weather agent run

# Runner.run_sync means synchronous line by line chalega
# result hamaray pas object return karega jisme final_output hoga
# final_output isliye use krte hain just final output ko print karne ke liye

set_tracing_disabled(True)
result = Runner.run_sync(weather_agent, "What is the weather like in Karachi today?")  # Example input to the weather agent

print(result.final_output)  # Print the final output from the weather agent



























# ye tools se answer gya LLM k pas phr LLM ne modify kr k wapas hame answer dia abhi ye answer tool se aya hay

# v run main.py
# Tracing is disabled. Not creating trace Agent workflow
# Setting current trace: no-op
# Tracing is disabled. Not creating span <agents.tracing.span_data.AgentSpanData object at 0x00000241B5C78A00>
# Running agent Ratan Lal (turn 1)
# Tracing is disabled. Not creating span <agents.tracing.span_data.GenerationSpanData object at 0x00000241B5C4D370>
# [
#   {
#     "content": "You are a helpful assistant. Answer the user's questions to the best of your ability.",
#     "role": "system"
#   },
#   {
#     "role": "user",
#     "content": "plus karo 2 or 3 ka"
#   }
# ]
# Tools:
# [
#   {
#     "type": "function",
#     "function": {
#       "name": "plus",
#       "description": "Adds two numbers together.",
#       "parameters": {
#         "properties": {
#           "n1": {
#             "description": "The first number.",
#             "title": "N1",
#             "type": "integer"
#           },
#           "n2": {
#             "description": "The second number.",
#             "title": "N2",
#             "type": "integer"
#           }
#         },
#         "required": [
#           "n1",
#           "n2"
#         ],
#         "title": "plus_args",
#         "type": "object",
#         "additionalProperties": false
#       }
#     }
#   },
#   {
#     "type": "function",
#     "function": {
#       "name": "multiply",
#       "description": "Multiplies two numbers together.",
#       "parameters": {
#         "properties": {
#           "n1": {
#             "description": "The first number.",
#             "title": "N1",
#             "type": "integer"
#           },
#           "n2": {
#             "description": "The second number.",
#             "title": "N2",
#             "type": "integer"
#           }
#         },
#         "required": [
#           "n1",
#           "n2"
#         ],
#         "title": "multiply_args",
#         "type": "object",
#         "additionalProperties": false
#       }
#     }
#   }
# ]
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN

# LLM resp:
# {
#   "content": null,
#   "refusal": null,
#   "role": "assistant",
#   "annotations": null,
#   "audio": null,
#   "function_call": null,
#   "tool_calls": [
#     {
#       "id": "",
#       "function": {
#         "arguments": "{\"n1\":2,\"n2\":3}",
#         "name": "plus"
#       },
#       "type": "function"
#     }
#   ]
# }

# Tracing is disabled. Not creating span <agents.tracing.span_data.FunctionSpanData object at 0x00000241B4587200>
# Invoking tool plus with input {"n1":2,"n2":3}
# Tool call args: [2, 3], kwargs: {}
# Tool plus returned 5
# Running agent Ratan Lal (turn 2)
# Tracing is disabled. Not creating span <agents.tracing.span_data.GenerationSpanData object at 0x00000241B609CC50>
# [
#   {
#     "content": "You are a helpful assistant. Answer the user's questions to the best of your ability.",      
#     "role": "system"
#   },
#   {
#     "role": "user",
#     "content": "plus karo 2 or 3 ka"
#   },
#   {
#     "role": "assistant",
#     "tool_calls": [
#       {
#         "id": "",
#         "type": "function",
#         "function": {
#           "name": "plus",
#           "arguments": "{\"n1\":2,\"n2\":3}"
#         }
#       }
#     ]
#   },
#   {
#     "role": "tool",
#     "tool_call_id": "",
#     "content": "5"
#   }
# ]
# Tools:
# [
#   {
#     "type": "function",
#     "function": {
#       "name": "plus",
#       "description": "Adds two numbers together.",
#       "parameters": {
#         "properties": {
#           "n1": {
#             "description": "The first number.",
#             "title": "N1",
#             "type": "integer"
#           },
#           "n2": {
#             "description": "The second number.",
#             "title": "N2",
#             "type": "integer"
#           }
#         },
#         "required": [
#           "n1",
#           "n2"
#         ],
#         "title": "plus_args",
#         "type": "object",
#         "additionalProperties": false
#       }
#     }
#   },
#   {
#     "type": "function",
#     "function": {
#       "name": "multiply",
#       "description": "Multiplies two numbers together.",
#       "parameters": {
#         "properties": {
#           "n1": {
#             "description": "The first number.",
#             "title": "N1",
#             "type": "integer"
#           },
#           "n2": {
#             "description": "The second number.",
#             "title": "N2",
#             "type": "integer"
#           }
#         },
#         "required": [
#           "n1",
#           "n2"
#         ],
#         "title": "multiply_args",
#         "type": "object",
#         "additionalProperties": false
#       }
#     }
#   }
# ]
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN

# LLM resp:
# {
#   "content": "2 aur 3 ka yog 5 hai.\n",
#   "refusal": null,
#   "role": "assistant",
#   "annotations": null,
#   "audio": null,
#   "function_call": null,
#   "tool_calls": null
# }

# Resetting current trace
# 2 aur 3 ka yog 5 hai.