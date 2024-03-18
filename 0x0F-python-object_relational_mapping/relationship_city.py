#!/usr/bin/python3
'''This module defines a class named City for SQLAlchemy'''
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    ''' This defines a class/table named City '''

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
