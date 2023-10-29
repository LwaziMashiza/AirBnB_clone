#!/usr/bin/python3
""" Defines the Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the Review class that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""