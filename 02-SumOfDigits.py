sum = 0
num = int(input("Enter Any Number: "))

while num > 0:
    temp = num % 10
    sum += temp
    num = num // 10

print("Sum:",sum)