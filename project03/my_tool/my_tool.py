from agents import function_tool


@function_tool
def plus(n1: int, n2:int):
    print("plus tool fire howa hay")
    """
    adds two numbers together!

    Returns:
    the sum of two numbers.
    """

    return n1 + n2

@function_tool
def multiply(n1:int, n2:int):
    """
    multiply two numbes together.

    Returns:
    the multiply of two numbers.
    """

    return n1 * n2



@function_tool
def subtract(n1:int, n2:int):
    print("subtract tool fire ----->")
    return n1 - n2