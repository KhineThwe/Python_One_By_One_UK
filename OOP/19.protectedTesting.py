class Parent:
    def __init__(self,age):
        self._age = age

    def getData(self):#header
        return self._age#body

class Sub(Parent):
    def __init__(self,age):
        super().__init__(age)

if __name__ == '__main__':
    sub = Sub(21)
    result = sub.getData()
    print(result)
