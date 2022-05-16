# Program 1: - Display Even Elemets
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def checkElement(num):
    if num % 2 == 0:
        return True
    else:
        return False
evenNumbers = [x for x in list if checkElement(x)]
# print(evenNumbers)

# Program 2: - Convert Celcius to Fahrenheit.
listTwo = [10, 50, 40, 38, 36]
def cToF(list):
    for i in range(len(list)):
        fharn = (list[i] * 1.8) + 32
        print(fharn)
# cToF(listTwo)

# Program 3 - Pick Only Integer Elements
listThree = ['sushant', 1, 52, True, 76, False]
def pickInteger(list):
    newList = []
    for i in range(len(list)):
        if type(list[i]) == int:
            newList.append(list[i])
    return newList
integersList = pickInteger(listThree)
# print(integersList)

# Program 4: - Print Prime Numbers
listFour = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def checkPrime(element):
    isPrime = True
    for i in range(2, element):
        if element % i == 0:
            isPrime = False
            return isPrime
    return isPrime
listFour = [z for z in listFour if checkPrime(listFour) == True]
print(listFour)
            

# Program 5: - Remove Negatives from list
listFive = [-1, 2, 6, -9, 5]
def removeNegative(list):
    newList = []
    for i in range(len(list)):
        if list[i] > 0:
            newList.append(list[i])
    return newList
# print(removeNegative(listFive))

# Program 6: - Check occurence of number
listSix = [1, 2, 1, 6, 1, 8]
totalOccurence = 0

def checkOccurence(list, num):
    global totalOccurence
    for i in range(len(list)):
        if list[i] == num:
            totalOccurence = totalOccurence + 1
    return totalOccurence
# print(checkOccurence(listSix, 1))

# Program 7: - Remove first and last element
listSeven = [10, 20, 30, 40]
def removeFirstLast(list):
    newList = []
    for i in range(len(list)):
        if i == 0 or i == len(list) - 1:
            continue
        else:
            newList.append(list[i])
    return newList
# print(removeFirstLast(listSeven))