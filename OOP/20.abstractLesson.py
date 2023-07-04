#abstract
"""
abstract class ---> abstract method,normal method
abstract method ---> without body only header
"""
from abc import ABC,abstractmethod

#abstract class
class Animal(ABC):
    #annotation
    @abstractmethod
    def speak(self):#header
       pass

    def normal(self):
        print("Hi I am normal method")

"""implements"""
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

if __name__ == '__main__':
    dog = Dog()
    dog.speak()
    dog.normal()

    cat = Cat()
    cat.speak()
    cat.normal()
