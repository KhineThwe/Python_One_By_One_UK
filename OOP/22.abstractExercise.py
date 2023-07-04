from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

if __name__ == '__main__':
    rectangle = Rectangle(5,3)
    result1 = rectangle.area()
    print(result1)

    circle = Circle(2)
    result2 = circle.area()
    print(result2)