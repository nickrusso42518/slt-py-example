'''
Author: Nick Russo
File: rectangle_test.py
Purpose: Unit tests for the Rectangle class.
'''

from unittest import TestCase
from rectangle import Rectangle

class RectangleTest(TestCase):
    '''
    Defines a test case for the Rectangle class.
    '''

    def setUp(self):
        '''
        Create a few test objects.
        '''
        self.len7wid3 = Rectangle(7, 3)
        self.len1wid6 = Rectangle(1, 6)

    def test_area(self):
        '''
        Since we know the length/width, we can compute the area
        and ensure the method returns the proper value.
        '''
        self.assertEqual(self.len7wid3.area(), 21)
        self.assertEqual(self.len1wid6.area(), 6)

    def test_perimeter(self):
        '''
        Since we know the length/width, we can compute the perimeter
        and ensure the method returns the proper value.
        '''
        self.assertEqual(self.len7wid3.perimeter(), 20)
        self.assertEqual(self.len1wid6.perimeter(), 14)
