class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

    def wag_tail(self):
        print("Tail Wagging")

if __name__ == '__main__':
    animal = Animal()
    animal.sound()

    dog = Dog()
    dog.sound()
    dog.wag_tail()

    a = Animal()
    a.sound()

    b = Dog()
    b.sound()

    #downcasting
    dog = a
    dog.sound()

    #upcasting
    animal = b
    animal.sound()
    animal.wag_tail()