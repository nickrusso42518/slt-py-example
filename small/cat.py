from animal import Animal

class Cat(Animal):
    def __init__(self, purr_type, size):
        self.purr_type = purr_type
        super().__init__(size)

    def get_info(self):
        return f'cat is {self.size} with a {self.purr_type} purr'
