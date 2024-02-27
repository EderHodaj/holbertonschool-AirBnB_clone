#!/usr/bin/python3
import json
from models.base_model import BaseModel
'''
Create FileStorage class
'''


class FileStorage:
    """ class about storing objects to json file"""

    __file_path = "file.json"
    __objects = {}
  
    def all(self):
        """return all key value pairs of the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """adds a new object as a value to the dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to json file"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(json_dict, json_file)

    def reload(self):
        """deserializes dictionaries from json file"""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                from_json = json.load(json_file)
                for key, value in from_json.items():
                    cls_name = globals()[value["__class__"]]
                    FileStorage.__objects[key] = cls_name(**value)
        except FileNotFoundError:
            return
