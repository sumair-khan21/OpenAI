import os
from decouple import config
from agents.tracing.processors import default_processor
from agents import set_trace_processors, AsyncOpenAI,OpenAIChatCompletionsModel,Agent, Runner, function_tool

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

set_trace_processors([default_processor()])

client = AsyncOpenAI(api_key=config('GEMINI_API_KEY'), base_url=config('BASE_URL'))
model = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)


@function_tool
def add(a:int, b:int):
    print("tool fire ============>")
    f"you are addition tool"
    return a + b


helper_agent = Agent(
    name="helper Agent",
    instructions="you are the helper agent and solve out all  query.",
    model=model,
    tools=[add]
)


res = Runner.run_sync(
    starting_agent=helper_agent,
    input="2 minus 2?"
)

print("last agent ",res.last_agent)
print("final answer: ", res.final_output)
