from dotenv import load_dotenv,find_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled,output_guardrail,RunContextWrapper,Agent,TResponseInputItem,GuardrailFunctionOutput,Runner,OutputGuardrailTripwireTriggered
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
    
@output_guardrail
async def check_output(ctx:RunContextWrapper[Any], agent:Agent[Any], output_data: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    print("output Data", output_data)


# agent to check output
    output_agent = Agent(
        name="output agent",
        instructions="Check and verify if output is related to math",
        model=model,
        output_type=MathOutput,
    )
    result = await Runner.run(output_agent, output_data, context=ctx.context)
    final_output= result.final_output
    print(final_output)

    return GuardrailFunctionOutput(
        output_info=final_output, tripwire_triggered=not final_output.is_math
    )
    
    
# main math agent
math_agent = Agent(
        name= "Math Agent",
        instructions="You are a math agent. Always answer with a math solution.",
        model=model,
        output_guardrails=[check_output]
    )


async def main():
    try:
        msg = input("Enter your questoin: ")
        result = await Runner.run(math_agent, msg)
        print(f"\n\n final output : {result.final_output}")
    except OutputGuardrailTripwireTriggered as ex:
        print("Error : Output not allowed by guardrail", ex)


asyncio.run(main())
