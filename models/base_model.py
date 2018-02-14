#!/usr/bin/python3
""" Base clas for Hbnb cmd line Proj """
import uuid
import models
from datetime import datetime
from copy import deepcopy

class BaseModel:
    """
        Base Model
    """
    def __init__(self, *args, **kwargs):
        # print(kwargs == {}, "wHAWS")
        if kwargs != {}:
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, val)
            # print(self, "lol")
            # print(self, "lolthereturn")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        # print(self, "lol???")

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Saves object """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Turns to dict """
        tmpDict = deepcopy(self.__dict__)
        # print(tmpDict)
        tmpDict['created_at'] = tmpDict['created_at'].isoformat()
        tmpDict['updated_at'] = tmpDict['updated_at'].isoformat()
        tmpDict['__class__'] = self.__class__.__name__
        return tmpDict