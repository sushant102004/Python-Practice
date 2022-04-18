sum = 0
num = int(input("Enter A Number: "))
temp = num

while temp > 0:
    lastDigit = temp % 10
    sum = sum + lastDigit ** 3
    temp = temp // 10

if num == sum:
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")