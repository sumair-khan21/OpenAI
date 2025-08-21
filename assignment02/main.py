import os
from decouple import config
from agents.tracing.processors import ConsoleSpanExporter, BatchTraceProcessor, default_processor
from agents import set_trace_processors, AsyncOpenAI,OpenAIChatCompletionsModel,Agent, Runner


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# console_exporter = ConsoleSpanExporter()
# processor = BatchTraceProcessor(console_exporter)


set_trace_processors([default_processor()])

client = AsyncOpenAI(api_key=config('GEMINI_API_KEY'), base_url=config('BASE_URL'))
model = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)

faq_context = """
You are a helpful FAQ bot. 
Here are some FAQs you can answer:

Q: What is your name?
A: I am the Helper FAQ Bot.

Q: What can you do?
A: I can answer your common questions.

Q: Who created you?
A: I was created by Sumair for an assignment.

Q: What is the capital of Pakistan?
A: The capital of Pakistan is Islamabad.

Q: How are you?
A: I am just code, but I am working perfectly fine!
"""
agent = Agent(
    name="FAQ Agent",
    instructions=faq_context,
    model=model
)


questions = [
    "What is your name?",
    "What can you do?",
    "Who created you?",
    "What is the capital of Pakistan?",
    "How are you?"
]

for q in questions:
    res = Runner.run_sync(starting_agent=agent, input=q)
    print(f"Q: {q}\nA: {res.final_output}\n")
