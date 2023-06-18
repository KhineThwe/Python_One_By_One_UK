class myClass:
    def __init__(self,value1,value2,option):
        self.a = value1
        self.b = value2
        self.option = option

    def myMethod(self):
        if self.option == 1:
            result = self.a + self.b
            print(result)
        elif self.option == 2:
            result = self.a - self.b
            print(result)
        elif self.option == 3:
            result = self.a * self.b
            print(result)
        elif self.option == 4:
            result = self.a / self.b
            print(result)

if __name__ == '__main__':
    firstNo = int(input("Enter fistNumber: "))
    secondNo = int(input("Enter secondNumber: "))
    option = int(input("Enter 1 for add,2 for subtract,3 for multiply,4 for divide"))
    obj1 = myClass(firstNo,secondNo,option)
    obj1.myMethod()