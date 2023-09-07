from pydantic import BaseModel,UUID4

class profile(BaseModel):
    id_profile=UUID4
    name:str
    lastname:str
    phonenumber:int
    age:int
    gender:str
    nationality:str