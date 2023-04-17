#!/usr/bin/python3
"""A base module for Other classes in this project."""
import json
import csv
import turtle


class Base:
    """A base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """A class constructor that initializes the id attribute."""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries
        If list_dictionaries is None or empty, return "[]"
        """

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string
        If json_string is None or empty, return an empty list
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to CSV format"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from CSV format"""
        filename = cls.__name__ + ".csv"
        list_objs = []
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    dict_obj = {}
                    if cls.__name__ == "Rectangle":
                        keys = ["id", "width", "height", "x", "y"]
                    elif cls.__name__ == "Square":
                        keys = ["id", "size", "x", "y"]
                    for i, key in enumerate(keys):
                        dict_obj[key] = int(row[i])
                    obj = cls.create(**dict_obj)
                    list_objs.append(obj)
            return list_objs
        except FileNotFoundError:
            return []


@staticmethod
def draw(list_rectangles, list_squares):
    """Draws all rectangles and squares"""
    t = turtle.Turtle()
    t.speed(0)
    for r in list_rectangles:
        t.fillcolor("red")
        t.penup()
        t.goto(r.x, r.y)
        t.pendown()
        t.begin_fill()
        for i in range(2):
            t.forward(r.width)
            t.left(90)
            t.forward(r.height)
            t.left(90)
        t.end_fill()
    for s in list_squares:
        t.fillcolor("blue")
        t.penup()
        t.goto(s.x, s.y)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.forward(s.size)
            t.left(90)
        t.end_fill()
    t.hideturtle()
    turtle.done()
