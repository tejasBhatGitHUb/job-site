import os
from dotenv import load_dotenv
from sqlalchemy import  create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
load_dotenv()

def initialize_db():
    engine = create_engine(os.getenv("connection_string"))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
