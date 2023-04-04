#!/usr/bin/python3
"""Defines a function that prints 2 new lines after ., ? and :"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of this characters: ., ? and :.

    Args:
         text: Text to print

    Raises:
         TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    lines = text.split("\n")
    for line in lines:
        print(line.strip())
