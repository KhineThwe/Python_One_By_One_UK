"""
Interface Class -- > abstract method only
"""
import zope.interface
class MyInterface(zope.interface.Interface):
    def method1(self):
        pass
    def method2(self):
        pass

@zope.interface.implementer(MyInterface)
class derivedClass:
    def method1(self):
        print("Hello from method 1")

    def method2(self):
        print("Hello from method 2")

if __name__ == '__main__':
    der = derivedClass()
    der.method1()
    der.method2()
