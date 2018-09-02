from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        '''
        Call the constructor from ABC, and do nothing else.
        '''
        super().__init__()

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
