class myClass:
    def __init__(self,value1,value2):
        self.a = value1
        self.b = value2

    def myMethod(self):
        result = self.a+self.b
        print(result)

if __name__ == '__main__':
    obj1 = myClass(10,20)
    obj1.myMethod()

    obj2 = myClass(20,40)
    obj2.myMethod()