#!/usr/bin/env python3
"""
"""
import json


class FileStorage():
    """serialize instances to a JSON and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns th dictionary"""
        return self.__objects

    def new(self, obj):
        """ sets in objects"""
        new_name = "{}.{}".format(self.__class__.__name__, obj.id)
        self.__objects[new_name] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            if self.__objects is None:
                f.write("[]")
            else:
                json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data_dict = json.load(f)
            for key, value in data_dict.items():
                new_data = f"{key} : {value}"
                return new_dat
        except FileNotFoundError:
            return []
