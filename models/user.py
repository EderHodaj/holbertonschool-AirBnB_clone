#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        dictionary = super().to_dict()
        dictionary['__class__'] = 'User'  # set the __class__ attribute to 'User'
        return dictionary