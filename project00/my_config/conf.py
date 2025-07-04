from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

my_Key = config("GEMINI_API_KEY")
# print(my_Key)

client = AsyncOpenAI(api_key=my_Key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

MODEL =  OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)

MODEL2 =  OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client)