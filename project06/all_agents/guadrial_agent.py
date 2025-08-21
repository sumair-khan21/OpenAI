from agents import Agent
from confg.gemini_confg import MODEL
from data_schema.myDataSchema import MyDataType

guadrial_agent = Agent(
    name="Guaddrial Agent for Hotel sannata",
    instructions="Check queris for hotel sannata",
    model= MODEL,
    output_type=MyDataType
)