from decouple import config
from agents import OpenAIChatCompletionsModel, Runner, Agent, AsyncOpenAI



my_Key = config("GEMINI_API_KEY")
base_url = config("BASE_URL")
# print(my_Key)

client = AsyncOpenAI(api_key=my_Key, base_url=base_url)

MODEL =  OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)

MODEL2 =  OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client)


# openai ki 3 api hoti hain
# 1. chat completions
# 2. responsis api by default openai use karta hai
# 3. assisstant api