from agents import function_tool, RunContextWrapper,FunctionTool,Runner,Agent
from tool_type.subtract_tool import SubtractSchema
from instruction.dynamic_instruction import en
from dataclasses import dataclass
from pydantic import BaseModel
import asyncio

@dataclass
class User(BaseModel):
    name:str
    id: int
    age:int

# ye custom tool hai
async def subtract(ctx:RunContextWrapper,args):
    """subtract ka functions"""
    # print("subtract tool fire =========>")
    # print("ctx======>", ctx.context["name"])
    obj = SubtractSchema.model_validate_json(args)
    return f"your answer is {obj.n1-obj.n2}"




# ye function tool hai
subtract = FunctionTool(
    name="subtract",
    description="subtract ka functions",
    params_json_schema=SubtractSchema.model_json_schema(), # model_json_schema ye paydantic ki waja se aaya hy 
    # on_invoke_tool ye tool ko invoke karega ya function ko invoke karega
    on_invoke_tool=subtract, 
    # is_enabled=False # ye tool ko enable karega ya disable karega
    is_enabled=en # ye tool ko enable karega ya disable karega
)



@function_tool
# simple hum yaha runcontextwrapper ki waja se main se data le rahe hain parameter mai
def plus(ctx:RunContextWrapper,n1,n2):
    """plus ka functions"""
    print("tool fire =========>")
    print("ctx======>", ctx.context["name"])
    return f"your answer is {n1+n2}"


# =========================================================================

# sir bilal ka code





# @function_tool
# def get_weather(city):
#     """get the weather of a city"""
#     return f"the weather of {city} is sunny"

# agent = Agent(
#         name="weather_agent",
#         instructions="you are a weather agent",
#         tools=[get_weather]
#     )


# async def main():
#     res = Runner.run_sync(agent, "what is the weather of delhi")
#     print(res)


# if __name__ == "__main__":
#     asyncio.run(main())

