from shape import shape
from math import pi

class circle(shape):
    decimal_places = 2

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(pi * (self.radius ** 2), self.decimal_places)

    def perimeter(self):
        return round(pi * self.diameter(), self.decimal_places)

    def diameter(self):
        return self.radius * 2
