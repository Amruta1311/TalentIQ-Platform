from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    score = Column(Float)
    device = Column(String)