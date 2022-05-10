# Immutable

# t = (10,)
# t2 = tuple('String')
# t5 = (8, 2, 1, 3)
# li = list(t5)
# li.sort()
# t6 = tuple(li)
# print(type(t6))
# print(t6)

# list = [(0, 'a', 'A'), (1, 'b', 'B'), (2, 'c', 'C')]
# for i, j, k in list:
#     print(i, j, k)

#  Zip Function
a = [1, 2, 3, 4, 5]
b = 'xyz'
# print(list(zip(a, b)))

# Zip Program
listOne = ['black', 'orange', 'red']
listTwo = [255, 0, 100]
temp = list(zip(listOne, listTwo))
# for i in temp:
#     print(i)

# An argument which begins with * in function definition gathers all arguments into a tuple.
def createTuple(*a):
    print(a)
# createTuple(1, 2, 3, 4, 5)

def sumAll(*a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum
# print(sumAll(1, 2, 3, 4, 5))

# Inverse or Reverse Zip
args = [('India', '₹'), ('USA', '$')]
Country, Currency = zip(*args)
# print(Country)
# print(Currency)