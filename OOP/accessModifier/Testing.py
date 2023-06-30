class Myclass:
    def __init__(self):
        self.public_var = "Public Variable"
        self._protected_var = "Protected Variable"
        self.__private_var = "Private Variable"

    def public_method(self):
        print("This is a public method.")

    def _protected_method(self):
        print("This is a protected method.")

    def __privateMethod(self):
        print("This is a private method")

if __name__ == '__main__':
    obj = Myclass()
    print(obj.public_var)
    obj.public_method()

    print(obj._protected_var)
    obj._protected_method()

    #name mangling
    print(obj._Myclass__private_var)
    obj._Myclass__privateMethod()