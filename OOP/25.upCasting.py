#age = int(input("Enter your age"))#conversion #type casting
#upcasting and downcasting
"""
inheritance
upcasting --> parent obj ---> convert
downcasting ---> child obj ---> convert
"""
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

if __name__ == '__main__':
    dog = Dog()
    dog.sound()

    #upcasting
    animal = Animal()
    animal = dog
    animal.sound()