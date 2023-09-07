from sqlalchemy import Column,Integer,String,UUID4,ForeignKey
from models.base import BaseModel
from sqlalchemy import relationship

class user(BaseModel):
    __tablename__='User'
    __args__={'schema':'public'}
    id_user=Column(str,primary_key=True,nullable=False)
    name=Column(str,nullable=False)
    email=Column(str,nullable=False)
    password=Column(str,nullable=False)
    