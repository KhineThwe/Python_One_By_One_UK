class Student:
    def __init__(self,name,id):
        self.name = name
        self.id  = id

    def introduce(self):
        print(f'Hello,I am {self.name} with id no {self.id}')

if __name__ == '__main__':
    stu1 = Student("Khine",1)
    stu1.introduce()

    stu2 = Student("Moe Moe",2)
    stu2.introduce()
