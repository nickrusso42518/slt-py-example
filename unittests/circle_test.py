'''
Author: Nick Russo
File: circle_test.py
Purpose: Unit tests for the Circle class.
'''

from unittest import TestCase
from shapes.circle import Circle

class CircleTest(TestCase):
    '''
    Defines a test case for the Circle class.
    '''

    def setUp(self):
        '''
        Create a few test objects.
        '''
        self.radius5 = Circle(5)
        self.radius8 = Circle(8)

    def test_area(self):
        '''
        Since we know the radii, we can compute the area
        and ensure the method returns the proper value.
        '''
        self.assertEqual(self.radius5.area(), 78.54)
        self.assertEqual(self.radius8.area(), 201.06)

    def test_perimeter(self):
        '''
        Since we know the radii, we can compute the perimeter
        and ensure the method returns the proper value.
        '''
        self.assertEqual(self.radius5.perimeter(), 31.42)
        self.assertEqual(self.radius8.perimeter(), 50.27)

    def test_diameter(self):
        '''
        Since we know the radii, we can compute the diameter
        and ensure the method returns the proper value.
        '''
        self.assertEqual(self.radius5.diameter(), 10)
        self.assertEqual(self.radius8.diameter(), 16)
