input = int(input("Enter Positive Integer: "));
outputNumber = 0

def getMultiple(num):
    global outputNumber
    if num < 0:
        print("Please Enter Positive Integer")
        return
    for i in range(1, num + 1):
        if num % i == 0 and outputNumber < 5:
            outputNumber = outputNumber + 1
            print(i)

getMultiple(input)