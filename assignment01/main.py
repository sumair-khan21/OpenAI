from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, set_trace_processors, Runner
import os
from tavily import TavilyClient



os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["TAVILY_API_KEY"] = config("TAVILY_API_KEY")


client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

query = "What is the weather of Karachi?"
results = client.search(query=query)

for r in results["results"]:
    print(f"Title: {r['title']}")
    print(f"URL: {r['url']}")
    print(f"Snippet: {r['content']}")
    print("="*50)









# console_exporter = ConsoleSpanExporter()
# processor = BatchTraceProcessor(console_exporter)
    
# # **include default_processor()** to keep default dashboard export
# set_trace_processors([processor, default_processor()])

# # Setup Gemini client
# client = AsyncOpenAI(api_key=config("GEMINI_API_KEY"), base_url=config("BASE_URL"))
# model = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)

# agent = Agent(
#     name="Helper Agent",
#     instructions="Your are the helper agent yo help out any of the query.",
#     model=model
# )

# res = Runner.run_sync(starting_agent=agent, input="newton kon ta detail btao?")
# print("Final:", res.final_output)
