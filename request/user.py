from pydantic import BaseModel,Field,UUID4

class user(BaseModel):
    id_user=UUID4
    name:str
    email:str
    password:str