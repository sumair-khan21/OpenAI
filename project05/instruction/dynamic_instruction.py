from agents import  RunContextWrapper

# yaha per apko do parameter pass karna hai
# 1. ctx:RunContextWrapper
# 2. agent:Agent
def dynamic_instruction(ctx:RunContextWrapper,agent):
    return f"User Name is {ctx.context["name"]}, you are helpful assistant"




async def en(ctx:RunContextWrapper,agent):
    # print("enable_tool fire =========>")
    if ctx.context["age"] >= 18:
        return True
    return False


