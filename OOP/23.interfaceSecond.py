class CanFly:
    def fly(self):
        pass

class Bird(CanFly):
    def fly(self):
        print("Bird is flying")

class Airplane(CanFly):
    def fly(self):
        print("Airplane is flying")

if __name__ == '__main__':
    bird = Bird()
    bird.fly()

    airplane = Airplane()
    airplane.fly()