from dotenv import load_dotenv,find_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled,input_guardrail,RunContextWrapper,Agent,TResponseInputItem,GuardrailFunctionOutput,Runner,InputGuardrailTripwireTriggered,WebSearchTool

from pydantic import BaseModel
from typing import Any
import asyncio



load_dotenv(find_dotenv(), override=True)
api_key= os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")
model_name= os.getenv("GEMINI_MODEL_NAME")


client = AsyncOpenAI(api_key=api_key, base_url=base_url)
model = OpenAIChatCompletionsModel(openai_client=client, model=model_name)

set_tracing_disabled(True)


class MathOutput(BaseModel):
    is_math: bool
    reason: str
    

@input_guardrail
async def check_input(ctx:RunContextWrapper[Any], agent:Agent[Any], input_data: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    print("input_data =======>", input_data)
    
    
    input_agent = Agent(
        name= "Input Guardrail Agent",
        instructions="Check and verify if input is related to math",
        model=model,
        output_type=MathOutput   
    )
    result = await Runner.run(input_agent, input_data, context=ctx.context)
    final_output = result.final_output
    print(final_output)
    
    return GuardrailFunctionOutput(
        output_info=final_output, tripwire_triggered=not final_output.is_math
    )


math_agent = Agent(
    "MathAgent",
    instructions="You are a math agent",
    model=model,
    input_guardrails=[check_input],
    # input_guardrails=[InputGuardrail(guardrail_function=check_input)]
)

general_agent = Agent(
    "GeneralAgent",
    instructions="You are a helpful agent",
    model=model,
    #output_guardrails=
)


async def main():
    try:
        msg = input("Enter you Question: ")
        result = await Runner.run(math_agent, msg)
        print(f"\n\n final output : {result.final_output}")
    except InputGuardrailTripwireTriggered as ex:
        print("Error : invalid prompt", ex)


asyncio.run(main())


    
    
    