from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel

my_key = config('GEMINI_API_KEY')
base_url = config('BASE_URL')

client = AsyncOpenAI(api_key=my_key, base_url= base_url)

MODEL = OpenAIChatCompletionsModel(model='gemini-2.0-flash', openai_client=client)

MODEL2 =  OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client)    