"""
Polymorphism --> loading , overriding

same name with different parameter ---> method overloading
"""
# def speak(language1):
#     print("language1")
# def speak(language1,language2):
#     print("language2")
#
# if __name__ == '__main__':
#     speak("language1","language2")
class Shape:
    def calculate_area(self):
        print("Welcome")

class Rectangle(Shape):
    def calculate_area(self,length,width):
        return length * width

class Circle(Shape):
    def calculate_area(self,radius):
        return 3.14 * radius * radius

if __name__ == '__main__':
    shape = Shape()
    shape.calculate_area()
    rectangle = Rectangle()
    circle = Circle()

    area_rectangle = rectangle.calculate_area(5,10)
    print("Area of rectangle: ",area_rectangle)

    area_circle = circle.calculate_area(3)
    print("Area of circle: ",area_circle)

