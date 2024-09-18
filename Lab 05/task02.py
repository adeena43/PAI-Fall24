from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self, l, b):
        print(f"The area of triangle is {0.5*l*b}")

class Rectangle(Shape):
    def area(self, l, b):
        print(f"The area of triangle is {l*b}")  

class Square(Shape):
    def area(self, l):
        print(f"The area of triangle is {l*l}")    

sqr = Square()
tri = Triangle()
rect = Rectangle()

sqr.area(8)
tri.area(5,6)
rect.area(5,5)

