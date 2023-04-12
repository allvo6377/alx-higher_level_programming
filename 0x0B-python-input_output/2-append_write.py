#!/usr/bin/python3
"""Defines a module that appends text to a file"""


def append_write(filename="", text=""):
    """A function that append text to file"""
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
