from pydantic import BaseModel, Field


class SubtractSchema(BaseModel):
    """
    Pydantic model ensures validated input for the subtract tool.
    - required integers n1 and n2
    - Pydantic will parse/validate incoming data and raise clear errors if invalid.
    """
    n1: int = Field(..., description="The first integer to subtract.")
    n2: int = Field(..., description="The second integer to subtract.")
    
    
