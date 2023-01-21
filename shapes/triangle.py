#!/usr/bin/env python

"""
Author: Oleksandr Moskaliuk
File: triangle.py
Purpose: Defines a triangle object, inherited from the abstract class Shape.
"""

from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains values for 3 sides,
    number of decimal places
    and a list, which contains triangle types
    """

    decimal_places = 2
    triangle_type = ["Scalene", "Isosceles", "Equilateral"]

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """
        Compute the area, using the Heron's formula math.sqrt(p * (p - a) * (p - b) * (p - c))
        """
        p = self.half_perimeter()
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), self.decimal_places)

    def perimeter(self):
        """
        Compute the perimeter using formula a + b + c
        """
        return self.a + self.b + self.c

    def half_perimeter(self):
        """
        Compute the half perimeter using the formula (a + b + c) / 2
        This calculation will then be used for area calculation, using Heron's formula
        """
        return round(((self.a + self.b + self.c) / 2), self.decimal_places)

    def get_triangle_type(self):
        """
        Determine whether triangle is Scalene or Isosceles or Equilateral
        """
        if self.a == self.b and self.b == self.c and self.a == self.c:
            return self.triangle_type[2]
        elif self.a != self.b and self.b != self.c and self.a != self.c:
            return self.triangle_type[0]
        else:
            return self.triangle_type[1]
