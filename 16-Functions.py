def greet():
    name = input("Enter Name: ")
    print("Hello", name)

def add(x, y):
    sum = 0
    for i in range(x, y + 1):
        sum = sum + i
    print("Sum of numbers from", x, "and", y, "is", sum)

# Positional Arguments
def display(name, age):
    print("Hello,",name,"Your age is: ", age)

# display("Sushant", 18)

# Keyword Arguments
# display(name = "Sushant", age=18)

# Positional Argument Can't Follow Keyword Argument & We Can't Duplicate An Argument By Speciying It As Both.

# Default Arguments
def func(age, name ="Mr. Unknown"):
    print("Name:", name, "Age:", age)

# Local & Global Variables
# Here p is global variable and q is local variable 
p = 10
def demo():
    q = 20

def funcTwo():
    s = "I Love Python Programming"
    print(s)
s = "This Is Python Class"
# funcTwo()
# print(s)

# Global Keyword
a = 10
def funcThree():
    global a
    a = 20
    print("Value of A:",a)
# print("Value of A:",a)
# funcThree()   

def compute(num):
    print("Number:",num)
    return num * num, num * num * num
square, cube = compute(10)
print("Square:",square)
print("Cube:",cube)