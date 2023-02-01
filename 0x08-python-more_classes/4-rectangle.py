#!/usr/bin/python3
"""Simply rectangle"""


class Rectangle:
    """__init__ - initialize a rectangle class
    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter function for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimter"""

        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return perimeter
        perimeter = 2 * self.__width + 2 * self.__height
        return perimeter

    def __str__(self):
        """Prints the rectangle based on the width and height with '#'"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for height in range(self.__height):
            for width in range(self.__width):
                rect += "#"
            if height < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Representation of the rectangle object"""

        return f"Rectangle({self.__width}, {self.__height})"
