from sqlalchemy import Column, Integer, String,ForeignKey,UUID
from models.base import BaseModel
from sqlalchemy import relationship 
class profile(BaseModel):
    __tablename__='Profile'
    __args__={'schema':'public'}
    id_profile=Column(int,primary_key=True,nullable=False)
    name=Column(str,nullable=False)
    lastname=Column(str,nullable=False)
    phonenumber=Column(str,nullable=False)
    age=Column(int,nullable=False)
    gender=Column(str,nullable=False)
    nacionality=Column(str,nullable=False)
    profile=(relationship("user",backpopulates=[id_user]))

    