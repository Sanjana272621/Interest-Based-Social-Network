from sqlalchemy import Column, Integer, String
from .database import Base 

class User(Base):
    __tablename__ = "user"

    uid = Column(Integer, primary_key = True, autoincrement = True, index = True) 
    name = Column(String(100), nullable = False)
    email = Column(String(100), nullable = False, index = True) 
    password = Column(String(100), nullable = False) #hashing needs to be added


