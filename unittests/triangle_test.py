"""
Author: Dmytro Iurchuk
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
        self.sides345 = Triangle(3,4,5)
        self.sides333 = Triangle(3,3,3)
        self.sides8810 = Triangle(8,8,10)
        self.sides71210 = Triangle(7,12,10)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.sides345.area(), 6)
        self.assertEqual(self.sides333.area(), 3.9)
        self.assertEqual(self.sides8810.area(), 31.22)
        self.assertEqual(self.sides71210.area(), 34.98)

    def test_perimeter(self):
        """
        Compare the test rectangle perimeter computations to the actual values.
        """
        self.assertEqual(self.sides345.perimeter(), 12)
        self.assertEqual(self.sides333.perimeter(), 9)
        self.assertEqual(self.sides8810.perimeter(), 26)
        self.assertEqual(self.sides71210.perimeter(), 29)

    def test_is_eqilateral(self):
        """
        Confirm or deny if the triangle is eqilateral.
        """
        self.assertFalse(self.sides345.is_eqilateral())
        self.assertTrue(self.sides333.is_eqilateral())
        self.assertFalse(self.sides8810.is_eqilateral())
        self.assertFalse(self.sides71210.is_eqilateral())

    def test_is_isosceles(self):
        """
        Confirm or deny if the triangle is isosceles.
        """
        self.assertFalse(self.sides345.is_isosceles())
        self.assertTrue(self.sides333.is_isosceles())
        self.assertTrue(self.sides8810.is_isosceles())
        self.assertFalse(self.sides71210.is_isosceles())

    def test_is_right(self):
        """
        Confirm or deny if the triangle is right.
        """
        self.assertTrue(self.sides345.is_right())
        self.assertFalse(self.sides333.is_right())
        self.assertFalse(self.sides8810.is_right())
        self.assertFalse(self.sides71210.is_right())
