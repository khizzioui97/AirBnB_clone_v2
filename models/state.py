#!/usr/bin/python3
"""State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from os import getenv
import models

class State(BaseModel, Base):
    """ State class """	    """ State class """
    name = ""	    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref='state',
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """
            returns list of city instances with state_id ==
            current State.id
            """
            city_instance = storage.all("City").values()
            return [city for city in city_instance if city.state_id == self.id]
 Empty file modified0  
models/user.py
 100644 → 100755
