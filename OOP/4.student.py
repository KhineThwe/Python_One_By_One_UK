class Student:
    #special method ---> constructor --> in C# classname နဲ့တူတာမှခေါ်တာ ဒါပေမဲ့python
    def __init__(self):
        self.name = input("Enter username: ")
        self.id  = int(input("Enter id: "))

    def introduce(self):
        print(f'Hello,I am {self.name} with id no {self.id}')

if __name__ == '__main__':
    stu1 = Student()#instantiate
    #stu1 --> instance obj
    stu1.introduce()
