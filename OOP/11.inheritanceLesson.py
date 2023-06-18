class Machine:#parent class
    #reusable
    def __init__(self,id):
        self.id = id

    def start(self):
        print("Machine Started!")

    def stop(self):
        print("Machine Stopped!")

class Car(Machine):#inheritance#base class or derived class
    def __init(self,id):
        super().__init__(id)

    #Override
    def start(self):
        print("Car Started!")

    def stop(self):
        print("Car Stopped!")

    def changeGear(self):
        print("Gear Changed!")

if __name__ == '__main__':
    car = Car(2)
    car.start()
    car.stop()
    car.changeGear()

    machine = Machine(2)
    machine.start()
    machine.stop()