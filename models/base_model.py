#!/usr/bin/env python3
"""
uuid module - create a unique id for BaseModel
datetime module - create current time
"""
import uuid
from datetime import datetime


class BaseModel():
    def __init__(self, name=None, my_number=None):
        """ initialize public instance attributes"""
        self.my_number = my_number
        self.name = name
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        """return string representation for the object of the class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id,
                                      self.__dict__))

    def save(self):
        """update the updated_at with the last save"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary with keys/values of an instance"""
        return ({"my_number": self.my_number,
                 "name": self.name,
                 "__class__": self.__class__.__name__,
                 "updated_at": self.updated_at.isoformat(),
                 "id": self.id,
                 "created_at": self.created_at.isoformat()})
