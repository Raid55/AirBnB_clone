#!/usr/bin/python3
"""review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """takes values as strings"""
    place_id = ""
    user_id = ""
    text = ""
