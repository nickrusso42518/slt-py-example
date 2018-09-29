from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, size):
        self.size = size.upper()

    @abstractmethod
    def get_info(self):
        pass
