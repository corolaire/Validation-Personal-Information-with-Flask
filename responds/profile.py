from pydantic import BaseModel,Field

class profile(BaseModel):
    id_profile:str=Field(min_length=1)
    id_user:str=Field(min_length=1)
    name:str=Field(min_length=1,max_length=20)
    lastname:str=Field(min_length=1,max_length=20)
    phonenumber:int=Field(min_length=11,max_length=15)
    age:int=Field(gt=18,lt=99)
    gender:str=Field(min_length=1)
    nacionality=Field(min_length=1)