from agents import input_guardrail,RunContextWrapper,GuardrailFunctionOutput, Runner
from all_agents.guadrial_agent import guadrial_agent
from data_schema.myDataSchema import MyDataType

@input_guardrail
async def guadrial_input_function(ctx:RunContextWrapper,agent,input):
    
    result = await Runner.run(guadrial_agent,input=input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_query_about_hotel_sannata
    )
    