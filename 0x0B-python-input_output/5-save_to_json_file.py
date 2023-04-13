#!/usr/bin/python3
"""Defines a function that saves object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """A function that writes an object to text file using,
    json representation"""
    with open(filename, "w") as f:
        j.dump(my_obj, f)
