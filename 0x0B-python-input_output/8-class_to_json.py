#!/usr/bin/python3
"""Returns dictionary descrition of data structure"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure,
    for JSON serialization of an object"""
    return obj.__dict__
