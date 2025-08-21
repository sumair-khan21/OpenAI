# class UserSchema:
#     def __init__(self, name: str, age: int, ):
#         self.name = name
#         self.age = age



# from dataclasses import dataclass
# @dataclass
# class UserSchema:
#     name: str
#     age: int


from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    age: int