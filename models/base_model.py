#!/usr/bin/python3
"""Defines a BaseModel class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods
    for other classes.
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        todict = {k: v for k, v in self.__dict__.items()}
        todict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        todict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        todict["__class__"] = self.__class__.__name__
        return todict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__class__.__dict__)
