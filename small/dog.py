from animal import Animal

class Dog(Animal):
    def __init__(self, name, weight):
        self.weight = weight
        super().__init__(name)

    def feed(self):
        return f"{self.name} needs {self.weight // 10} cups of food daily"

    def dig_hole(self):
        # ability unique to dogs
        pass
