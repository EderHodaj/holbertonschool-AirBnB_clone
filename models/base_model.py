#!/usr/bin/python3
import uuid
import datetime
import models
'''Create Base Classe'''


class BaseModel:
    '''Createing the class attributes'''
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(
                        value,
                        '%Y-%m-%dT%H:%M:%S.%f'
                        )
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
