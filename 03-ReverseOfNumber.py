reverse = 0
num = int(input("Enter Any Number: "))

while num > 0:
    temp = num % 10
    reverse = reverse * 10 + temp
    num = num // 10

print("Reverse",reverse)