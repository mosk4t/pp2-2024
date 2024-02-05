class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print(self.length**2)
x = Square(int(input()))
y = Shape()
x.area()
y.area()