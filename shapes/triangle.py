"""
Author: Dmytro Iurchuk
File triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from math import sqrt
from heapq import nsmallest
from shapes.shape import Shape

class Triangle(Shape):
    """
    Represents a Triangle shape, and contains three sides length values
    and number of decimal places to use when computing values.
    """
    decimal_places = 2

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def area(self):
        """
        Compute the area using Heron's formula sqrt(s * (s - a) * (s - b) * (s - c))
        where s is semi-perimeter and a, b and c - corresponding sides
        """
        s = self.perimeter() / 2
        return round(sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)), self.decimal_places)

    def perimeter(self):
        """
        Compute the perimeter using the formula a + b + c
        """
        return self.a + self.b + self.c

    def is_eqilateral(self):
        """
        Determine if the triangle is a equilateral by comparing the length
        of each side for equality. If all three sides are equal - triangle called equilateral.
        """
        return (self.a == self.b) and (self.a == self.c) and (self.b == self.c)

    def is_isosceles(self):
        """
        Determine if the triangle is a isosceles by comparing sides lengths.
        If at least two sides are equal - triangle called isosceles.
        """
        return (self.a == self.b) or (self.a == self.c) or (self.b == self.c)

    def is_right(self):
        """
        Determine if the triangle is a right using Pythagorean theorem.
        If one of angles is right - triangle called right.
        """
        sides_squared = [x ** 2 for x in (self.a, self.b, self.c)]
        return max(sides_squared) == sum(nsmallest(2, sides_squared))
