#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, relationships
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel, Base):
    """
    inherits from BaseModel and Base
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable = False)
    places_amenities = relationship(
            "Place",
            secondary="places_amenities"
            )
