#!/usr/bin/python3
"""Defines the file storage class."""
import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Representes a storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        ocname = obj.__class__.__name__
        self.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Seralizes __objects to the
        JSON File."""
        dict_save = {}
        with open(self.__file_path, "w+", encoding="UTF-8") as f:
            for key, value in self.__objects.items():
                dict_save[key] = value.to_dict()
            json.dump(dict_save, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r+") as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    clsname = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(clsname)(**obj))
        except FileNotFoundError:
            return
