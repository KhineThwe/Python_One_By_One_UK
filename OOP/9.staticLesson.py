class Calculator:
    @staticmethod
    def addNumbers(x,y):
        return x+y

if __name__ == '__main__':
    # cal = Calculator()
    # result = cal.addNumbers(10,20)
    # print(result)

    result = Calculator.addNumbers(20,20)
    print(result)