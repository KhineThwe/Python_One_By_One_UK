class Person:
    def __init__(self,name,age):
        print(f"Hello {name}:{age},Welcome from python course!!!")

    def welcome(self):
        print("This is from Welcome method")

if __name__ == '__main__':
    person1 = Person("Khine",24)  # objဆောက်လိုက်တာ
    person1.welcome()
