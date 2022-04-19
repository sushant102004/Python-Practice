numberList = [3, 8, 12, 2, 5, 21]
max = numberList[0]
for i in numberList:
    if max < i:
        max = i
print("Greatest Number: " , max)