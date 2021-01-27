#!/usr/bin/env python

"""
Author: Jakub
File: equilateral_triangle.py
Purpose: Defines a Equilateral Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape
from math import sqrt

class EquilateralTriangle(Shape):
    """
    Represents a Equilateral Triangle shape, and contains a side length value.
    """

    def __init__(self, side):
        self.side = side

    def area(self):
        """
        Compute the area using the formula sqrt(4)/2 * side length to second power
        """
        return sqrt(4)/2 * (self.side**2)

    def perimeter(self):
        """
        Compute the perimeter using the formula 3 * side length
        """
        return self.side * 3

    def get_height(self):
        """
        Calculate a height of Equilateral Triangle
        """
        return  (self.side * sqrt(3))/2
