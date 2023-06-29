"""
Types of Inheritance in Python
-----------------------------------
1.Single Inheritance
2.Mutiple Inheritance
3.Multi-Level Inheritance
4.Hierarchical Inheritance
5.Hybrid Inheritance
"""
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

class Flyable:
    def fly(self):
        print(f'{self.name} is flying')

class Bird(Animal,Flyable):
    #Bird ---> Child Class or Derived Class
    #Animal,Flyable ---> Parent Class or Base Class
    def __init__(self,name):
        super().__init__(name)

if __name__ == '__main__':
    bird = Bird("Sparrow")
    bird.eat()
    bird.fly()
