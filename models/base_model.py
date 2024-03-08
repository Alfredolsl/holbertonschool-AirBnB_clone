#!/usr/bin/python3
"""Defines a BaseModel class"""

from uuid import uuid4
from datetime import datetime

import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeformat)
                elif k != "__class__":
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Saves updated attributes and saves time of update in
        updated_at."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Represents instance in dictionary"""
        todict = self.__dict__.copy()
        todict["created_at"] = self.created_at.isoformat()
        todict["updated_at"] = self.updated_at.isoformat()
        todict["__class__"] = self.__class__.__name__
        return todict

    def __str__(self):
        """Prints representation of class or inherited class."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)
