from pydantic import BaseModel

# type hanting k liye use ki jati
# ye ek schema hay ta k ek proper table mai answer kare
# ek library ya package hay ek type handling k liye use hota hay
# ye hint hay hame is type me data return karo
# koi class define krni hay toh dataclass se kr sakhte hain
# agr pydantic k zarye karoge toh koi validation bhi ho jayegi
class MyDataOutput(BaseModel):
    n1:int
    n2:int
    # agr answer nhi mila
    response:str = "Thank you"


# data classes
# @dataclass
# class MyData:
#     n1:int
#     n2:int
#     res:int
    
    
    