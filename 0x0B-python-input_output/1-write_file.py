#!/usr/bin/python3
"""Defines a string writing module"""


def write_file(filename="", text=""):
    """A line writing printing function"""
    with open(filename, mode="w", encoding="utf-8") as a_file:
        print(a_file.write(), end="")
