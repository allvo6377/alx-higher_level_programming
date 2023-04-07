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
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".:?":
            print("\n")
            if i != len(text) - 1:
                print("\n")
        i += 1
