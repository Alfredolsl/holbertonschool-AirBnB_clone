#!/usr/bin/python3
"""Defines the file storage class."""
import json


class FileStorage:
    """Representes a storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj
        with key <obj class name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Seralizes __objects to the
        JSON File."""
        objdict = FileStorage.__objects
        dict_to_json = {obj: objdict[obj].to_dict() for obj in objdict.keys()}
        with open(self.__file_path, "w", encoder="utf-8") as f:
            json.dump(dict_to_json)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    clsname = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
