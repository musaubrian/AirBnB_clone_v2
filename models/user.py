#!/usr/bin/python3
"""This module defines a class User"""
import models
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if models.storage_t == 'db':
        __table_name__ = 'Users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
                "Place", backref="user",
                passive_deletes=True,
                cascade="all,delete"
                )
        reviews = relationship(
                "Review", backref="user"
                cascade="all, delete"
                passive_deletes=True
                )
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
