#!/usr/bin/python3
"""city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """takes state_id as string"""
    state_id = ""
    """takes name as string"""
    name = ""
