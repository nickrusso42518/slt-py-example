'''
Author: Nick Russo
File: shape.py
Purpose: Definition of the abstract base class Shape
to demonstrate inheritance, polymorphism, and decorators.
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    '''
    Defines the abstract base class Shape.
    '''

    def __str__(self):
        '''
        Allows the shape to be treated like a string, returning the type.
        '''
        return type(self).__name__

    def to_dict(self):
        '''
        Convert this shape into a dictionary with name, area, and perimeter.
        '''
        return {
            'type': str(self),
            'area': self.area(),
            'perimeter': self.perimeter()
        }

    @abstractmethod
    def area(self):
        '''
        Children implement this method based on their type of shape.
        '''
        pass

    @abstractmethod
    def perimeter(self):
        '''
        Children implement this method based on their type of shape.
        '''
        pass
