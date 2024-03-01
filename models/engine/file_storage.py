#!/usr/bin/python3
'''
Module for file storage
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''
    Class for file storage
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        function that returns the dict of objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        function to set obj in objects
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        return True

    def save(self):
        '''
        function to serialize objects to the json file
        '''
        obj_dictionary = {}
        for key, value in FileStorage.__objects.items():
            obj_dictionary[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dictionary, f)
        return True

    def reload(self):
        '''
        functiont to deserialize json files to objects
        '''
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    obj = eval(cls_name)(**value)
                    self.new(obj)
            return True
        except Exception as e:
            return False

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }