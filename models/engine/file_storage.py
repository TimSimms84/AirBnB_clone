#!/usr/bin/python3
"""
This module contains the class: FileStorage
"""
import json
import models


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    # path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    @classmethod
    def clear(cls):
        FileStorage.__objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """
         deserializes the JSON file to __objects if it exist
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
                for key in jo:
                    self.__objects[key] = getattr(
                        models, jo[key]['__class__'])(**jo[key])
        except Exception:
            pass
