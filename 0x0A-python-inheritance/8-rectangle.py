#!/usr/bin/python3
class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Class BaseGeometry"""

    def area(self):
        """Raises Exeption """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
