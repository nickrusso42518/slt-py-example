'''
Author: Nick Russo
File: circle.py
Purpose: Defines a Circle object, inherited from the abstract class Shape.
'''

from math import pi
from shapes.shape import Shape

class Circle(Shape):
    '''
    Represents a Circle shape, and contains only a radius value
    and number of decimal places to use when computing values.
    '''
    decimal_places = 2

    def __init__(self, radius):
        '''
        Create the circle by storing the radius.
        '''
        self.radius = radius

    def area(self):
        '''
        Compute the area using the formula pi * radius^2
        '''
        return round(pi * (self.radius ** 2), self.decimal_places)

    def perimeter(self):
        '''
        Compute the perimeter (circumference) using the formula pi * diameter
        '''
        return round(pi * self.diameter(), self.decimal_places)

    def diameter(self):
        '''
        Compute the diameter using the formula radius * 2
        Computing diameter is specific to circles, not all shapes.
        '''
        return self.radius * 2
