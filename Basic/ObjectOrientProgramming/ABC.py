from abc import ABC
from abc import abstractclassmethod

class Shape(ABC):

    def __init__():
        super().__init__() #нужно чтобы сделать этот класс абстрактным - через супер мы обращаемся к ABC

        @abstractmethod
        def draw(self):
            pass

        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            print('calc perimeter')

        def drag(self):
            print('basic dragging functionality')

#s = Shape() #error - нужно реализоввывать методы

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    #необходимо переопределить все абстрактные методы
    def draw(self):
        print(f'Drawing triangle with sides = {self.a}, {self.b}, {self.c}')

    def area(self):
        print('Area')

    def perimeter(self):
        print('Perimeter')

s = Triangle(10, 20, 30)
s.draw()
s.perimeter()
s.area()