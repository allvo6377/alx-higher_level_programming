#!/usr/bin/python3
"""A module defining the class student"""


class Student:
    """Defines a student by first_name, last_name and age"""
    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
