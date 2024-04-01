from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name.strip().upper()

    @abstractmethod
    def feed(self):
        pass
