'''
Author: Nick Russo
File: rectangle_test.py
Purpose: Unit tests for the Rectangle class.
'''

from unittest import TestCase
from shapes.rectangle import Rectangle

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
        self.len5wid5 = Rectangle(5, 5)

    def test_area(self):
        '''
        Since we know the length/width, we can compute the area
        and ensure the method returns the proper value.
        '''
        self.assertEqual(self.len7wid3.area(), 21)
        self.assertEqual(self.len1wid6.area(), 6)
        self.assertEqual(self.len5wid5.area(), 25)

    def test_perimeter(self):
        '''
        Since we know the length/width, we can compute the perimeter
        and ensure the method returns the proper value.
        '''
        self.assertEqual(self.len7wid3.perimeter(), 20)
        self.assertEqual(self.len1wid6.perimeter(), 14)
        self.assertEqual(self.len5wid5.perimeter(), 20)

    def test_is_square(self):
        '''
        Since we know the length/width, we can determine if this
        rectangle is a square or not.
        '''
        self.assertFalse(self.len7wid3.is_square())
        self.assertFalse(self.len1wid6.is_square())
        self.assertTrue(self.len5wid5.is_square())
