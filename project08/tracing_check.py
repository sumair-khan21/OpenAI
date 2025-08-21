# from decouple import config
# from agents import AsyncOpenAI, OpenAIChatCompletionsModel,Agent,set_tracing_disabled,Runner,set_trace_processors
# from agents.tracing.processors import ConsoleSpanExporter, BatchTraceProcessor, default_processor
# from agents.tracing.processor_interface import TracingExporter
# from agents.tracing.spans import Span
# from agents.tracing.traces import Trace


# # custom class for tracing 
# # class CustomConsoleSpanExporter(TracingExporter):
# #     def export(self, items: list[Trace | Span]):
# #         for item in items:
# #             if isinstance(item, Trace):
# #                 print(f"[Trace] ID: {item.trace_id} | Name: {item.name}")
# #             elif item.span_data.type == "generation":
# #                 usage = item.span_data.usage or {}
# #                 model = item.span_data.model
# #                 user_input = item.span_data.input or []
# #                 output = item.span_data.output or []

# #                 print("🧠 Model Used:", model)
# #                 print("📥 Input Tokens:", usage.get("input_tokens", "N/A"))
# #                 print("📤 Output Tokens:", usage.get("output_tokens", "N/A"))

# #                 if user_input:
# #                     print("🙋 User Asked:", user_input[-1].get("content", "N/A"))
# #                 if output:
# #                     print("🤖 Bot Replied:", output[0].get("content", "N/A"))







# exporter = ConsoleSpanExporter()
# # exporter = CustomConsoleSpanExporter()
# processor = BatchTraceProcessor(exporter)

# # set_tracing_disabled(True)
# set_trace_processors([processor,default_processor()])

# my_key1 = config('GEMINI_API_KEY')
# my_key = config('OPENAI_API_KEY')
# base_url = config('BASE_URL')

# client = AsyncOpenAI(
#     api_key=my_key1,
#     base_url=base_url)
# MODEL = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)

# helper_agent = Agent(
#     name = "Helper Agent",
#     instructions="Your are the helper agent yo help out any of the query.",
#     model=MODEL
# )

# res =  Runner.run_sync(starting_agent=helper_agent,input="What is the capital of Pakistan?")
# print(res.final_output)











from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, set_trace_processors, Runner
from agents.tracing.processors import ConsoleSpanExporter, BatchTraceProcessor, default_processor
import os

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
console_exporter = ConsoleSpanExporter()
processor = BatchTraceProcessor(console_exporter)

set_trace_processors([processor, default_processor()])

client = AsyncOpenAI(api_key=config("GEMINI_API_KEY"), base_url=config("BASE_URL"))
model = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)

agent = Agent(
    name="Helper Agent",
    instructions="Your are the helper agent yo help out any of the query.",
    model=model
)

res = Runner.run_sync(starting_agent=agent, input="What is the capital of Pakistan?")
print("Final:", res.final_output)
