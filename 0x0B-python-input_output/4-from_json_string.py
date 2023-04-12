#!/usr/bin/python3
"""Defines a module that converts from json string to object"""


import json


def from_json_string(my_str):
    """A function that returns an object represented by json string"""
    return json.loads(my_str)
