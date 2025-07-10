from agents import function_tool


# ye reaper function_tool banata hay
@function_tool
def fetch_weather(city:str)-> str:
    """
    Fetches the current weather for a given city.
    
    Args:
        city (str): The name of the city to fetch the weather for.
        
    Returns:
        str: The weather in karachi is sunny.
    """
    # This is a placeholder implementation. Replace with actual weather fetching logic.
    return f"The current weather in {city} is sunny with a temperature of 25°C."