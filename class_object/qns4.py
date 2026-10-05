#Create a base class Shape with a method draw(). Derive classes Circle, Rectangle, and Triangle that override draw()
class Shape:
    def draw(self):
        print("Drawing a shape")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")


class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")



circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

circle.draw()
rectangle.draw()
triangle.draw()