class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    #getter method of name
    def get_name(self):
        return self.__name

    #setter method of name
    def set_name(self,name):
        self.__name = name

    #getter method of age
    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

if __name__ == '__main__':
    person = Person("Jame",24)
    realName = person.get_name()
    print(realName)

    person.set_name("Alice")
    realName1 = person.get_name()
    print(realName1)

    person.set_age(25)
    realAge = person.get_age()
    print(realAge)

