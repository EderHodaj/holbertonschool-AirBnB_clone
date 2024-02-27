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
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
