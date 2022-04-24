# 1. WAP to arrange strings such that lowercase characters comes first.
# 2. WAP to count vowels in a string.
# 3. WAP to count lowercase, uppercase, numeric characters in string.
# 4. WAP a program to print len of a string without using len function.

# Program 1
print("Program 1: ")
strTwo = "SushanT"
for j in strTwo:
  if(j == j.lower()):
    print(j, end='')

for k in strTwo:
  if(k == k.upper()):
    print(k, end='')
print('\n')


# Program 2: - 
print("Program 2: ")
str = "Sushant"
vowelsCount = 0
consonentsCount = 0
strLen = len(str)

for i in str:
  if i == 'a':
    vowelsCount = vowelsCount + 1
  elif i == 'A':
    vowelsCount = vowelsCount + 1
  elif i == 'e':
    vowelsCount = vowelsCount + 1
  elif i == 'E':
    vowelsCount = vowelsCount + 1
  elif i == 'i':
    vowelsCount = vowelsCount + 1
  elif i == 'I':
    vowelsCount = vowelsCount + 1
  elif i == 'o':
    vowelsCount = vowelsCount + 1
  elif i == 'O':
    vowelsCount = vowelsCount + 1
  elif i == 'u':
    vowelsCount = vowelsCount + 1
  elif i == 'U':
    vowelsCount = vowelsCount + 1

print("Total Vowels:", vowelsCount)
consonentsCount = strLen - vowelsCount
print("Total Consonents:", consonentsCount)
print('\n')

# Program 3

print("Program 3: ")

lowerCase = 0
upperCase = 0
strThree = "SushantDhiman"

for i in strThree:
  if(i == i.lower()):
    lowerCase = lowerCase + 1
  if(i == i.upper()):
    upperCase = upperCase + 1

print("Lower Case Characters:",lowerCase)
print("Upper Case Characters:", upperCase)
print('\n')

# Program 4:
print("Program 4:")

strLength = 0
strFour = "Sushant"
for x in strFour:
  strLength = strLength + 1

print("Length of String:", strLength)