# oop/polymorphism_demo.py

import math


class Shape:
    """
    Base class representing a generic shape.
    Contains an abstract area method meant to be overridden.
    """

    def area(self):
        """
        Raises an error because subclasses must implement this method.
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """
    Rectangle shape that inherits from Shape.
    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    """

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """
        Returns the area of the rectangle.
        Formula: length × width
        """
        return self.length * self.width


class Circle(Shape):
    """
    Circle shape that inherits from Shape.
    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        Formula: π × radius²
        """
        return math.pi * (self.radius ** 2)
