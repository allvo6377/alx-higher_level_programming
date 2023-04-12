#!/usr/bin/python3
"""Defines a module that reads a text file"""


def read_file(filename=""):
    """A text file reading function"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
