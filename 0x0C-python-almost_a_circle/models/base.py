#!/usr/bin/python3
"""A base module for Other classes in this project."""
import json


class Base:
    """A base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """A class constructor that initializes the id attribute."""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries
        If list_dictionaries is None or empty, return "[]"
        """

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string
        If json_string is None or empty, return an empty list
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set
        Create a dummy instance with default values for mandatory attributes
        Use the update method to apply the real values from the dictionary
        Return an updated instance
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
    dummy.update(**dictionary)
    return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            json_string = f.read()
        list_dictionaries = cls.from_json_string(json_string)
        list_instances = []
        for dictionary in list_dictionaries:
            instance = cls.create(**dictionary)
            list_instances.append(instance)
        return list_instances
