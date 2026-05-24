#!/usr/bin/python3
"""FileStorage module"""
import json


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set obj in __objects with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        json_objects = {}
        for key, obj in FileStorage.__objects.items():
            json_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserialize the JSON file to __objects, if the file exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_objects = json.load(f)
            for key, value in json_objects.items():
                cls_name = value.get("__class__")
                if cls_name in classes:
                    obj = classes[cls_name](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
