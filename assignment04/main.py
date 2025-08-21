import os
from decouple import config
from agents.tracing.processors import ConsoleSpanExporter, BatchTraceProcessor, default_processor
from agents import set_trace_processors, AsyncOpenAI,OpenAIChatCompletionsModel,Agent, Runner,function_tool


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# console_exporter = ConsoleSpanExporter()
# processor = BatchTraceProcessor(console_exporter)


set_trace_processors([default_processor()])

client = AsyncOpenAI(api_key=config('GEMINI_API_KEY'), base_url=config('BASE_URL'))
model = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)




@function_tool
def get_weather(city:str):
    print("tool fire ============>")
    return f"the weather of {city} is 20 degree celsius"



helper_agent = Agent(
    name="helper Agent",
    instructions=(
        "You are a helpful agent. "
        "If the user asks about weather in any city, always call the tool `get_weather(city)`."
    ),    model=model,
    tools=[get_weather],
)


res = Runner.run_sync(
    starting_agent=helper_agent,
    input="what is the weather of karachi?"
)

# print("last agent ",res.last_agent)
print("final answer:=======================> ", res.final_output)
