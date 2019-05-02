"""
Author: Nick Russo
File: rectangle.py
Purpose: Defines a Rectangle object, inherited from the abstract class Shape.
"""

from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Rectangle shape, and contains a length value
    and width value.
    """
    decimal_places = 2

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        """
        Compute the area using Heron's formula
        """
        s = self.perimeter() / 2
        try:
            return round(sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)), self.decimal_places)
        except ValueError:
            print('Please enter 3 valid sides')
            raise

    def perimeter(self):
        """
        Compute the perimeter using the formula a + b + c
        """
        return self.side_a + self.side_b + self.side_c

    def is_equilateral(self):
        """
        Determine if the triangle is equilateral.
        """
        return self.compare() == 2

    def is_isosceles(self):
        """
        Determine if the rectangle is a square by comparing the length
        and width for equality. Only rectangles can be squares.
        """
        return self.compare() == 1

    def compare(self):
        """
        Compare all sides and return the amount of differences
        """
        sides = [self.side_a, self.side_b, self.side_c]
        return len(sides) - len(set(sides))
