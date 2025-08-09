from openai import FunctionTool
from all_schema.subtract_schema import SubtractSchema


async def subtract(n1: int, n2: int) -> int:
    print("Subtracting tool fire ==========>")
    return f"your answer is {n1 - n2}"

@FunctionTool(
    name="subtract",
    description="Subtracts two integers.",
    schema=SubtractSchema.model_json_schema(),
    tool_name_override="Subtract Numbers",
    tool_description_override="Use this tool to perform subtraction.",
    input_filter="math",
    invoke_function=subtract    
)

def subtract(n1: int, n2:int) -> int:
    return n1 - n2