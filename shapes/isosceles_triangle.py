#!/usr/bin/env python

"""
Author: Jakub
File: isosceles_triangle.py
Purpose: Defines a Isosceles Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape
from math import sqrt

class IsoscelesTriangle(Shape):
    """
    Represents a Isosceles Triangle shape, and contains a side length value.
    """

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """
        Compute the area using the formula 1/2 * base * height
        """
        return (self.base * self.height) / 2

    def perimeter(self):
        """
        Compute the perimeter using the formula base length + 2 times frame length
        """
        return self.base + 2 * self.get_frame_length()

    def get_frame_length(self):
        """
        Calculate a frame length of Isosceles triangle based on Pythagoras's theorem
        """
        return sqrt((self.base / 2)**2 + h**2)

    def is_isosceles_right_triangle(self):
        """
        Determine if a isosceles triangle is right by comparing 
        base length to formula a*sqrt(2)
        """
        return sqrt(self.base) == self.get_frame_length() * sqrt(2)

