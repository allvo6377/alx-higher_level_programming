#!/usr/bin/python3
"""Defines a module with a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter for the width attribute"""
        self.__width = value

    @property
    def height(self):
        """The getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter for the height attribute"""
        self.__height = value

    @property
    def x(self):
        """The getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter for the x attribute"""
        self.__x = value

    @property
    def y(self):
        """The getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter for the y attribute"""
        self.__y = value
