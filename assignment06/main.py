import os
from decouple import config
from agents.tracing.processors import default_processor
from agents import set_trace_processors, AsyncOpenAI,OpenAIChatCompletionsModel,Agent, Runner,function_tool,input_guardrail,RunContextWrapper,TResponseInputItem,GuardrailFunctionOutput,InputGuardrailTripwireTriggered,ModelSettings
from pydantic import BaseModel
from typing import Any
import asyncio

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
set_trace_processors([default_processor()])

client = AsyncOpenAI(api_key=config('GEMINI_API_KEY'), base_url=config('BASE_URL'))
model = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)


class OrderOutput(BaseModel):
    is_order: bool
    
    
@function_tool(is_enabled=lambda input:"order" in input.lower())
async def get_order_status(order_id: str) -> str:
    if order_id == "123":
        return "Your order 123 is delivered."
    else:
        raise ValueError("Order not found")


@input_guardrail
async def check_input(ctx:RunContextWrapper[Any], agent:Agent[Any], input_data: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    # print("input data ============>", input_data)



    input_agent = Agent(
        name="Input Guardrial Agent",
        instructions="Check if the input has offensive or negative words. Return is_order=False if offensive.",
        model=model,
        output_type=OrderOutput
    )
    result = await Runner.run(input_agent, input_data, context=ctx.context)
    final_output = result.final_output
    print(final_output)
    
    return GuardrailFunctionOutput(output_info=final_output, tripwire_triggered=not final_output.is_order)
    
    
    

human_agent = Agent(
    name="HumanAgent",
    instructions="You are a human support agent. Take over when bot cannot handle.",
    model=model
)


order_agent = Agent(
    name="OrderAgent",
    instructions="You are the helpful order agent",
    model=model,
    input_guardrails=[check_input],
    model_settings=ModelSettings(tool_choice="auto")
)




async def main():
    try:
        msg = input("Enter your question: ")
        result = await Runner.run(order_agent, msg)
        print("last agent", result.last_agent)
        print("final output", result.final_output)
    except InputGuardrailTripwireTriggered as ex:
        print("Error : invalid prompt", ex)
        


asyncio.run(main())