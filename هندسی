from abc import ABC, abstractmethod

class Shape(ABC):

    def mohasebe_masahat(self):
        pass

    
    def mohasebe_mohit(self):
        pass
########################################################



class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height



    def mohasebe_masahat(self):
        return self.width * self.height

    def mohasebe_mohit(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self radius = radius
        self.pi = 3.14159



    def mohasebe_masahat(self):
        return self.pi * self.radius ** 2

    def mohasebe_mohit(self):
        return 2 * self pi * self.radius
########################################################

shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print("masahate:", shape.mohasebe_masahat())
    print("mohit", shape.mohasebe_mohit())
