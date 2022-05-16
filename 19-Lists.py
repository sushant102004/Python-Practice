# List Comprehension
# list = [10, 20, 30, 40]
# for i in list:
#     print(i)
# print(list[0])
# list = [x + 10 for x in list]


# Program 1: - Display even elements using list comprehension
listOne = [1, 2, 3, 4, 5, 6]
listOne = [x for x in listOne if x % 2 == 0]

# Program 3: - Display only even elements from list
# listTwo = ["Sushant", True, 10, False, 20]
# for i in range(len(listTwo)):
#     if type(listTwo[i]) != int:
#          print(listTwo[i])

# Program 4: Create 5 element list, pass to function and calculate average
# listThree = [1, 2, 3, 4, 5]

# def calculateAverage(list):
#     temp = 0
#     for i in range(len(list)):
#         temp = temp + list[i]
#     average = temp // len(list)
#     return average
# print(calculateAverage(listThree))
