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
    divideCount = 0
    for i in range(2, element // 2):
        if element % i == 0:
            divideCount = divideCount + 1
    if divideCount == 0:
        return True
    else:
        return False

primeNumbers = [z for z in listFour if checkPrime(z)]
print(primeNumbers)