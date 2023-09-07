from pydantic import BaseModel,Field

class user(BaseModel):
    id_user:str=Field(min_length=1)
    name:str=Field(min_length=1,max_length=10)
    email:str=Field(min_length=3,max_length=320)
    password:str=Field(min_length=8,max_length=16)