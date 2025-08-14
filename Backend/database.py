from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, Text, PrimaryKeyConstraint, DateTime, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
import sqlite3

DB_URL = 'sqlite:///./Test.db'
engine = create_engine(DB_URL)
Base = declarative_base()
Base.metadata.create_all(engine)  

class Banner(Base):
    __tablename__ = 'banner'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    description = Column(String(64), nullable=False)
    linkpath = Column(Text, nullable=False)
    imgpath = Column(Text, nullable=False)

