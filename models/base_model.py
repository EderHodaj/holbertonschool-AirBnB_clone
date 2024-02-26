#!/usr/bin/python3
import uuid
import datetime
'''Create Base Classe'''


class BaseModel:
    '''Createing the class attributes'''
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self,key,value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        self.__dict__['__class__'] = 'BaseModel'
        return self.__dict__

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)