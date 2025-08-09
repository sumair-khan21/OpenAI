from pydantic import BaseModel



class MyDataType(BaseModel):
    is_query_about_hotel_sannata:bool
    is_query_about_account_and_text: bool
    reason:str