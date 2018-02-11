#!/usr/bin/python3
""" Base clas for Hbnb cmd line Proj """
import uuid
from datetime import datetime

class BaseModel:
    """
        Base Model
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        tmpDict = self.__dict__
        tmpDict['created_at'] = tmpDict['created_at'].isoformat()
        tmpDict['updated_at'] = tmpDict['updated_at'].isoformat()
        tmpDict['__class__'] = self.__class__.__name__
        return tmpDict