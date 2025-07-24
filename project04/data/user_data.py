

# from data_schema.user_schema import UserSchema
from pydantic import BaseModel



class UserSchema(BaseModel):
    name: str
    age: int


user_data = UserSchema(name="John", age=20)

# print(user_data)







