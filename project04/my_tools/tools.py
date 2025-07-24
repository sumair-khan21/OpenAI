from agents import function_tool, RunContextWrapper
from datetime import datetime
from data.user_data import user_data
from data_schema.user_schema import UserSchema


# @function_tool
# def get_current_time(city: str, context: RunContextWrapper) -> str:
#     print("tool function called")
#     print(context.user_data.name)
#     return f"The current time in {city} is {datetime.now().strftime('%H:%M:%S')}"




@function_tool
def get_user_age(ctx: RunContextWrapper[UserSchema]) -> str:
    print("tool function called")
    print(ctx.user_data.name)
    return f"user age is {ctx.user_data.age}    "








