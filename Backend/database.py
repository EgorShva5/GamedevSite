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

class GameDeepInfo(Base):
    __tablename__ = 'game_deep_info'
    
    game_id = Column(Integer, nullable = False)
    r_bad = Column(Integer, nullable = False)
    r_good = Column(Integer, nullable = False)
    screens = Column(Text, nullable = False)
    developer_id = Column(Integer, nullable = False)
    all_rating = Column(Text, nullable = False)
    tags = Column(Text, nullable=False)
    info_id = Column(Integer, primary_key = True)

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key = True)
    username = Column(Text, nullable = False)
    password = Column(Text, nullable = False)
    account_type = Column(Text, nullable = False)
