num = int(input("Enter A Number: "))
isNumberPrime = True

if num > 2:
    for i in range(2, num):
        if(num % i == 0):
            isNumberPrime = False
            break

if isNumberPrime == True:
    print("Number is Prime")
else:
    print("Number is Not Prime")