#!/usr/bin/python3
"""Defines a function that saves object to a file"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w") as f:
        return j.dumps(my_obj, f)
