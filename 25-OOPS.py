class Demo:
    pass
D1 = Demo()
# print(D1)

class Rectangle:
    len = 0
    bre = 0
R1 = Rectangle()
R2 = Rectangle()
# print(R1.len)
# print(R2.len)
R2.len = 5
R2.bre = 5
# print(R2.len)
# print(R2.bre)

class DemoOne:
    def display(self):
        print('Executed Function From A Class')

DemoOneObject = DemoOne()
# DemoOneObject.display()

from itertools import permutations
import math
from mimetypes import init
class Circle:
    def calculateArea(self, radius):
        area = math.pi * radius ** 2
        return area
circleObject = Circle()
# print(circleObject.calculateArea(4))

class Prac:
    x = 5
    def display(self, x):
        self.x = 30
        print('Local Variable X is', x)
        print('Global Variable X is', x)
pracObject = Prac()
# pracObject.display(50)

class FuncClass:
    def funcOne(self):
        print('This is function one.')
    def funcTwo(self):
        print('This is function two')
        self.funcOne()
funcClassObject = FuncClass()
# funcClassObject.funcTwo()

class InitClass:
    def __init__(self):
        name = 'Sushant'
        age = 18
        print('You are',name,'and your age is',age)

# initClassObj = InitClass()
# print(initClassObj)

class Box:
    def __init__(self, length, breadth, height):
        volume = length * breadth * height
        print(volume)

boxObject = Box(2, 3, 4)
print(boxObject)