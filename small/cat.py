from animal import Animal

class Cat(Animal):
    def __init__(self, name, is_adult):
        self.is_adult = is_adult
        super().__init__(name)

    def feed(self):
        return f"{self.name} needs {5 if self.is_adult else 8} cans of food daily"

    def retract_claws(self):
        # ability unique to cats
        pass
