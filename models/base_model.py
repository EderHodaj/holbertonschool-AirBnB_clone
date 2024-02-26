#!/usr/bin/python3
import uuid
import datetime
'''Create Base Classe'''


class BaseModel:
    '''Createing the class attributes'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now().isoformat())
        self.updated_at = str(datetime.datetime.now().isoformat())

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        self.__dict__['__class__'] = 'BaseModel'
        return self.__dict__
