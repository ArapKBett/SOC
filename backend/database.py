from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Threat(Base):
    __tablename__ = 'threats'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    timestamp = Column(String)

def init_db():
    engine = create_engine('sqlite:///dashboard.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()

db_session = init_db()