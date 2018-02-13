#!/usr/bin/python3
""" File storage manager """
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """ Class that handles serializing and deserializing instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        self.__objects.update({'{}.{}'.format(obj.__class__.__name__, obj.id): obj})

    def save(self):
        tmpDict = {}
        for key, val in FileStorage.__objects.items():
            tmpDict[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w+') as f:
            json.dump(tmpDict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
            for key, val in FileStorage.__objects.items():
                FileStorage.__objects[key] = eval(val['__class__'])(**val)
        except IOError:
            pass
        except ValueError:
            pass