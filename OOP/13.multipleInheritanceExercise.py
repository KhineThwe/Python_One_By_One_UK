"""
Vehicle Exercise
"""
class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def drive(self):
        print(f'{self.brand} is being driven.')

    def start(self):
        print(f'{self.brand} is starting')

    def stop(self):
        print(f'{self.brand} is stopping')

class FlyingVehicle:
    def fly(self):
        print(f'{self.brand} is flying')

class ModernVehicle:
    def status(self):
        print(f'{self.brand} is lastest model')

class Car(Vehicle,ModernVehicle):
    def __init__(self,brand,color):
        super().__init__(brand)
        self.color = color

    def drive(self):
        print(f'{self.brand} with {self.color} is being driven.')

class Airplane(Vehicle,FlyingVehicle,ModernVehicle):
    def __init__(self,brand):
        super().__init__(brand)

if __name__ == '__main__':
    car = Car("BMW","red")
    car.start()
    car.drive()
    car.stop()

    airplane = Airplane("Toyata")
    airplane.start()
    airplane.fly()
    airplane.stop()
    airplane.status()