# from decouple import config
# from agents import AsyncOpenAI, OpenAIChatCompletionsModel,Agent,Runner,set_tracing_export_api_key,RunContextWrapper,GuardrailFunctionOutput,InputGuardrail
# from all_agents.general_agent import general_asssiatant_agent  
# from pydantic import BaseModel
# import asyncio

# my_key = config('GEMINI_API_KEY')
# base_url = config('BASE_URL')



# client = AsyncOpenAI(api_key=my_key, base_url=base_url)
# MODEL = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)


# set_tracing_export_api_key(my_key)


# class MathOutput(BaseModel):
#     is_math:bool
#     reason:str 
    
    
    
    
    
# def check_input(ctx:RunContextWrapper,agent:Agent,input_data:str)->GuardrailFunctionOutput:
#     return GuardrailFunctionOutput(output_info="hello world", tripwire_triggered=True)

# input_agent = Agent("InputGuadrailAgent", instructions="check and verify if input is related to math", 
# model=MODEL,
# output_type=MathOutput
#                     )



# class CountryOutPut(BaseModel):
#     country:str
#     province:str
#     major_cities:list[str]
#     population:str
    










# general_asssiatant_agent = Agent(
#     name="General Assistant",
#     instructions="A general assistant that can help with a wide range of tasks.",
#     model=MODEL,
#     # output_type=CountryOutPut
#     output_type=MathOutput
    
# )


# math_agent = Agent(
#     name="Math Agent",
#     instructions="An agent that can help with mathematical calculations and problems.",
#     model=MODEL,
#     input_guardrails=[InputGuardrail(guardrail_function=check_input)]
# )







# async def main():
#     try:
#         result = await Runner.run(starting_agent=math_agent, input="what is the output of 2 + 2?",
#        )
#     except Exception as ex:
#         print("Invalid prompt")
        
    
      
#     # print(result)
    

# asyncio.run(main())
    
    
    
    
    
    
    
    
    
    
    
    
    
# # res = Runner.run_sync(starting_agent=math_agent, input="what is the output of 2 + 2?",
# #     output_type=CountryOutPut)














from decouple import config
from agents import (
    AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner,
    set_tracing_export_api_key, RunContextWrapper, GuardrailFunctionOutput,
    InputGuardrail, OutputGuardrail
)
from pydantic import BaseModel
import asyncio

# ====== API Keys & Model Setup ======
my_key = config('GEMINI_API_KEY')
base_url = config('BASE_URL')

client = AsyncOpenAI(api_key=my_key, base_url=base_url)
MODEL = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)

set_tracing_export_api_key(my_key)

# ====== Output Schemas ======
class MathOutput(BaseModel):
    is_math: bool
    reason: str

class CountryOutput(BaseModel):
    country: str
    province: str
    major_cities: list[str]
    population: str

# ====== Input Guardrail Function ======
def math_input_guardrail(ctx: RunContextWrapper, agent: Agent, input_data: str) -> GuardrailFunctionOutput:
    # Simple check: agar input me +, -, *, / ya "math" shabd hai to block kare
    restricted_keywords = ["+", "-", "*", "/", "math", "solve", "="]
    if any(kw in input_data.lower() for kw in restricted_keywords):
        return GuardrailFunctionOutput(
            output_info="Math related query detected. Blocking as per policy.",
            tripwire_triggered=True
        )
    return GuardrailFunctionOutput(
        output_info="Input is safe.",
        tripwire_triggered=False
    )

# ====== Output Guardrail Function ======
def country_output_guardrail(ctx: RunContextWrapper, agent: Agent, output_data: CountryOutput) -> GuardrailFunctionOutput:
    # Agar country name missing ho ya population data empty ho, block kare
    if not output_data.country or not output_data.population:
        return GuardrailFunctionOutput(
            output_info="Invalid country data: Missing required fields.",
            tripwire_triggered=True
        )
    return GuardrailFunctionOutput(
        output_info="Output is valid.",
        tripwire_triggered=False
    )

# ====== Agents ======
general_assistant_agent = Agent(
    name="General Assistant",
    instructions="A general assistant that can help with a wide range of tasks.",
    model=MODEL,
    output_type=CountryOutput,
    output_guardrails=[OutputGuardrail(guardrail_function=country_output_guardrail)]
)

math_agent = Agent(
    name="Math Agent",
    instructions="An agent that can help with mathematical calculations and problems.",
    model=MODEL,
    input_guardrails=[InputGuardrail(guardrail_function=math_input_guardrail)],
    output_type=MathOutput
)

# ====== Runner ======
async def main():
    try:
        # Input Guardrail Test
        print("=== Testing Math Agent (with Input Guardrail) ===")
        result_math = await Runner.run(
            starting_agent=math_agent,
            input="what is the output of 2 + 2?"
        )
        print("Math Agent Output:", result_math)

    except Exception:
        print("Math Agent blocked due to input guardrail.")

    try:
        # Output Guardrail Test
        print("\n=== Testing General Assistant (with Output Guardrail) ===")
        result_country = await Runner.run(
            starting_agent=general_assistant_agent,
            input="Tell me about Pakistan."
        )
        print("General Assistant Output:", result_country)

    except Exception:
        print("General Assistant blocked due to output guardrail.")

# Run Async
asyncio.run(main())
