#!/usr/bin/env python3
"""
"""
import json


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
        FileStorage.__objects[new_name] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
	        new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_dict, f)
        print(new_dict)

    def reload(self):
        """deserializes the JSON file to __objects"""
        new_data = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                data_dict = json.load(f)
                print()
            for key, value in data_dict.items():
                new_data = f"{key} : {value}"
                return new_data
        except FileNotFoundError:
            return []
