'''
Author: Nick Russo
File: shape.py
Purpose: Definition of the abstract base class Shape
to demonstrate polymorphism and decorators.
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    '''
    Defines the abstract base class Shape.
    '''

    def __str__(self):
        '''
        Whenever a shape is treated like a string, this
        function returns the name of the class.
        '''
        return type(self).__name__

    @abstractmethod
    def area(self):
        '''
        Children must implement this method based on
        their type of shape.
        '''
        pass

    @abstractmethod
    def perimeter(self):
        '''
        Children must implement this method based on
        their type of shape.
        '''
        pass
