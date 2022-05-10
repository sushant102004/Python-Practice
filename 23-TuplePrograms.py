# WAP to store numbers present at odd index in a new tuple
T = (1, 3, 2, 4, 6, 5)
def storeOddIndex(tup):
    newList = []
    for i in range(0, len(tup), 2):
        newList.append(tup[i])
    return tuple(newList)
# print(storeOddIndex(T))

# Method 2: - Args
def storeOddIndexArgs(*args):
    newList = []
    for i in range(0, len(args), 2):
        newList.append(args[i])
    return tuple(newList)
# print(storeOddIndexArgs(1, 2, 3, 4, 5, 6))

# WAP to reverse the elements of a list.
listOne = [1, 2, 3, 4, 5, 6]
length = len(listOne)
def reverseList(list):
    newList = []
    global length
    for i in range(0, length):
        newList.append(list[-1])
        list.pop(-1)
        length = length - 1
    return newList
# print(reverseList(listOne))

# WAP to take two +ve integers where a < b and return odd elements between them.
def returnNumbers(numberOne, numberTwo):
    if numberOne > numberTwo:
        print('First number should be greater than second.')
        return

    newList = []
    for i in range(numberOne, numberTwo + 1):
        if i % 2 != 0:
            newList.append(i)
    return newList
print(returnNumbers(10, 20))