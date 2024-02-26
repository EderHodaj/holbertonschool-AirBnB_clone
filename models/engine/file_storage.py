#!/usr/bin/python3
import json
'''
Create FileStorage class
'''


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
  
    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["BaseModel.id"] = "obj"

    def save(self):
        with open(self.__file_path, "w") as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        if self.__file_path:
            with open(self.__file_path, "r") as json_file:
                json.load(json_file)
        else:
            pass

