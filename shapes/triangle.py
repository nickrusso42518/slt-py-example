#!/usr/bin/env python

"""
Author: Shashank Garg
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains all three side lengths for the
    triangle
    """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise ValueError("The sides don't form a triangle")

    def is_valid(self):
        """
        Checks if the sides of the triangle form a valid triangle
        """
        return 2 * max(self.a, self.b, self.c) < sum([self.a, self.b, self.c])

    def area(self):
        """
        Compute the area using the Heron's formula
        sqrt(s*(s-a)*(s-b)*(s-c))
        s : semi perimeter
        a: side1 length
        b: side2 length
        c: side3 length
        """
        sp = self.perimeter() / 2
        return (sp * (sp - self.a) * (sp - self.b) * (sp - self.c)) ** 0.5

    def perimeter(self):
        """
        Compute the perimeter using the sum of all sides
        """
        return sum([self.a, self.b, self.c])

    def type(self):
        """
        Computes the type of triangle
        * Equilateral
        * Isosceles
        * Right
        * Scalene
        """

        def all_sides_equal():
            return self.a == self.b == self.c

        def two_sides_equal():
            return (self.a == self.b or
                    self.b == self.c or
                    self.a == self.c)

        def pythagorean():
            sides = sorted([self.a, self.b, self.c])
            return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2

        return ("Equilateral" if all_sides_equal() else
                "Isosceles" if two_sides_equal() else
                "Right" if pythagorean() else
                "Scalene")
