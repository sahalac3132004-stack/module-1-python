class Shape:
    def area(self):
        print("Area of shape")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    
    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width


square = Square(6)
rectangle = Rectangle(10, 4)

print("Area of Square:", square.area())
print("Area of Rectangle:", rectangle.area())