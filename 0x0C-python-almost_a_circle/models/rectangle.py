#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    Class rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    """*********************"""
    @property
    def width(self):
        """get width"""
        return self.width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    """*********************"""
    @property
    def height(self):
        """get height"""
        return self.height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value
    """*********************"""
    @property
    def x(self):
        """Get x"""
        return self.x

    @x.setter
    def x(self, value):
        """Ser x"""
        self.__x = value
    """*********************"""
    @property
    def y(self):
        """Get y"""
        return self.y

    @y.setter
    def y(self, value):
        """Set y"""
        self.__y = value
