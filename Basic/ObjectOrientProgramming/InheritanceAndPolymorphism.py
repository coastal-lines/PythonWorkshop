class Shape():
    
    def __init__(self):
        print('Shape created')
        
    def draw(self):
        print('Drawing a shape')
    
    def area(self):
        print('calc area')
        
    def perimeter(self):
        print('calc perimeter')

shape = Shape()

class Rectangle(Shape):
    
    def __init__(self, width, height):
        Shape.__init__(self)
        
        self.width = width
        self.height = height
        
        print('Rectangle created')
        
    def draw(self):
        print(f'Drawing rectangle with width={self.width} and height={self.height}')
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)