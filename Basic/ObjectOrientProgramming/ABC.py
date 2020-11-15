from abc import ABC
from abc import abstractclassmethod

class Shape(ABC):

    def __init__():
        super().__init__() #нужно чтобы сделать этот класс абстрактным - через супер мы обращаемся к ABC

        @abstractmethod
        def draw(self):
            pass