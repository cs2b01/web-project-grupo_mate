from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    username = Column(String(12))

class Bussiness(connector.Manager.Base):
    __tablename__ = 'bussiness'
    id = Column(Integer, Sequence('bussiness_id_seq'), primary_key=True)
    bussiness_name = Column(String(30))
    bussiness_email = Column(String(30))
    bussiness_number = Column(String(9))
    bussiness_description = Column(String(100))
