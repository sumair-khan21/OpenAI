from agents import Runner, set_tracing_disabled,InputGuardrailTripwireTriggered
from all_agents.general_agent import general_asssiatant_agent, hotel_asssiatant  
from all_agents.guadrial_agent import guadrial_agent 
from confg.gemini_confg import my_key
from pydantic import BaseModel





set_tracing_disabled(True)
# set_tracing_export_api_key(my_key)




# class CountryOutPut(BaseModel):
#     country:str
#     province:str
#     major_cities:list[str]
#     population:str
    

# res = Runner.run_sync(starting_agent=general_asssiatant_agent, input="What is the first name of JavaScript? and give me details answer why?",
#     output_type=CountryOutPut)
# print(res.final_output)





try:
    
    res = Runner.run_sync(
    starting_agent=guadrial_agent, 
    # starting_agent=hotel_asssiatant, 
    input="what is the owner name of hotel sareena?",
    )
    print(res.final_output)
except InputGuardrailTripwireTriggered as e:
    print(e)
    