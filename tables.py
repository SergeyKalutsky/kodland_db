from sqlalchemy import Column, Integer, String
from .db import Base


class Users(Base):

    __tablename__ = 'users'

    login = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    price = Column(Integer)


class Ordesr(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer)
    amount = Column(Integer)
