"""
Author: Nick Russo
File: circle_test.py
Purpose: Unit tests for the Circle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Circle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.a4b5c7 = Triangle(4, 5, 7)
        self.a5b5c5 = Triangle(5, 5, 5)
        self.a3b5c5 = Triangle(3, 5, 5)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.a4b5c7.area(), 9.8)
        self.assertEqual(self.a5b5c5.area(), 10.83)
        self.assertEqual(self.a3b5c5.area(), 7.15)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.a4b5c7.perimeter(), 16)
        self.assertEqual(self.a5b5c5.perimeter(), 15)
        self.assertEqual(self.a3b5c5.perimeter(), 13)

    def test_diameter(self):
        """
        Compare the test triangle types to the actual values.
        """
        self.assertEqual(self.a4b5c7.get_triangle_type(), "Scalene")
        self.assertEqual(self.a5b5c5.get_triangle_type(), "Equilateral")
        self.assertEqual(self.a3b5c5.get_triangle_type(), "Isosceles")
