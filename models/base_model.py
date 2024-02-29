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
        dict_instance = {k: v for k, v in self.__dict__.items()}
        dict_instance["id"] = self.id
        dict_instance["__class__"] = self.__class__.__name__
        dict_instance["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_instance["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dict_instance

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__class__.__dict__)


basemodel = BaseModel()
basemodel.name = "My First Model"
basemodel.my_number = 89

#print(basemodel)

basemodel.save()

#print(basemodel)

print("JSON of my model:")
basemodel_json = basemodel.to_dict()
for key in basemodel_json.keys():
    print("\t{}: ({}) - {}".format(key, type(basemodel_json[key]), basemodel_json[key]))
