from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

DATABASE_URL = "mysql+mysqlconnector://admin:mypassword@localhost:3306/recsys"

engine = create_engine(DATABASE_URL)

SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

