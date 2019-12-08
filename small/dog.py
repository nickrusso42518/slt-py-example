from animal import Animal

class Dog(Animal):
    def __init__(self, bark_type, size):
        self.bark_type = bark_type
        super().__init__(size)

    def get_info(self):
        return f"dog is {self.size} with a {self.bark_type} bark"
