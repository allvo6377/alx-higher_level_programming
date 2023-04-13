#!/usr/bin/python3
"""A modules that defines an object creating function"""


import json


def load_from_json_file(filename):
    """Creates an Object from a json file"""
    with open(filename, "r") as f:
        return json.load(f)
