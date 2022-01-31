'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters
'''

class MyClass:
    def __init__(self):
        self.st1 = ''
    def getString(self):
        self.st1 = input('ingrese string: ')
    def prnitString(self):
        print(self.st1.upper())

obj1 = MyClass()
obj1.getString()
obj1.prnitString()