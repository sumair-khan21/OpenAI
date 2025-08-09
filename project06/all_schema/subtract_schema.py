from pydantic import BaseModel, Field


class SubtractSchema(BaseModel):
    n1: int = Field(..., description="The first integer to subtract.")
    n2: int = Field(..., description="The second integer to subtract.")
    
    
