#!/usr/bin/env python3
"""
"""
import json
import ast


class FileStorage():
    """serialize instances to a JSON and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in objects"""
        new_name = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[new_name] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(FileStorage.__file_path, "r") as f:
                data_dict = json.load(f)
                for key, value in data_dict.items():
                    """safely evaluate the string back into a Python object"""
                    FileStorage.__objects[key] = ast.literal_eval(
                                                 str(data_dict))
        except FileNotFoundError:
            pass
