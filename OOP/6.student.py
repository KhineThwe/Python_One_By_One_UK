class Student:
    id = 0  # class or global variable
    name = "Global Name"  # class or global variable

    # method
    def introduce(self):
        name = "Khine"  # local variable
        id = 1  # local variable
        print(f'Hello,I am {name} with id no {id}')

    def test(self):
        print(f'{self.name}:{self.id}')


if __name__ == '__main__':
    student = Student()
    student.introduce()
    student.test()
