#!/usr/bin/python3
"""Defines a BaseModel class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods
    for other classes.
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def save(self):
        updated_at = datetime.now()

    def to_dict(self):
        todict = {k: v for k, v in self.__dict__.items()}
        todict["id"] = self.id
        todict["__class__"] = self.__class__.__name__
        todict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        todict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return todict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__class__.__dict__)
