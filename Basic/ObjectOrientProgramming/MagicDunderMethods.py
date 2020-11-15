class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): #метод определяет строковое представление класса
        return f'Point x={self.x}, y={self.y}'

p = Point(3, 4)
print(p)