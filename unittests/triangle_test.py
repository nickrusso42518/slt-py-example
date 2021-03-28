"""
Author: Shashank Garg
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase

from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.equilateral = Triangle(7, 7, 7)
        self.isosceles = Triangle(4, 6, 6)
        self.right = Triangle(5, 4, 3)
        self.scalene = Triangle(5, 4, 6)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(round(self.equilateral.area(), 6), 21.217622)
        self.assertEqual(round(self.isosceles.area(), 6), 11.313708)
        self.assertEqual(round(self.right.area(), 6), 6)
        self.assertEqual(round(self.scalene.area(), 6), 9.921567)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.equilateral.perimeter(), 21)
        self.assertEqual(self.isosceles.perimeter(), 16)
        self.assertEqual(self.right.perimeter(), 12)
        self.assertEqual(self.scalene.perimeter(), 15)

    def test_valid(self):
        """
        Confirm or deny if the triangle is a valid configuration.
        """
        with self.assertRaises(ValueError):
            Triangle(5, 1, 1)

        with self.assertRaises(ValueError):
            Triangle(5, 1, 4)

        self.assertTrue(self.equilateral.is_valid())
        self.assertTrue(self.scalene.is_valid())
        self.assertTrue(self.isosceles.is_valid())
        self.assertTrue(self.right.is_valid())

    def test_type(self):
        """
        Compare the test triangle type computations to the actual values.
        """
        self.assertEqual(self.equilateral.type(), "Equilateral")
        self.assertEqual(self.isosceles.type(), "Isosceles")
        self.assertEqual(self.right.type(), "Right")
        self.assertEqual(self.scalene.type(), "Scalene")
