#!/usr/bin/python3
"""Defines a module that creates a class rectangle"""


class Rectangle:
    """
    class that represents a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle with a width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Deletes a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """Returns a printable string representation of the # character"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return ((str(self.print_symbol) * self.width + "\n") *
                    self.height)[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        """Gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

