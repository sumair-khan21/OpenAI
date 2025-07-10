# yaha per tool banega
# agr mujhe openai ka algotithum use nhi rkna toh ye ap  na custom tool bana sakte ho
# tool ek function hay LLM k zarye apna tasks complete krna
# agr mai agents se tool hata dun toh isko btana parega k k ap apne LLM se bhi ans kr sakhte ho agr instraution m nhi btaya toh agent ka tool answer nhi dega





from agents import function_tool



@function_tool
def plus(n1: int, n2: int) -> int:
    """
    Adds two numbers together.
    
    Args:
        n1 (int): The first number.
        n2 (int): The second number.
        
    Returns:
        int: The sum of the two numbers.
    """
    return n1 + n2

@function_tool
def multiply(n1: int, n2: int) -> str:
    """
    Multiplies two numbers together.
    
    Args:
        n1 (int): The first number.
        n2 (int): The second number.
        
    Returns:
        int: The product of the two numbers.
    """
    return n1 * n2