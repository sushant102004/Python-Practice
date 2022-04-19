# 1. WAP to arrange strings such that lowercase characters comes first.
# 2. WAP to count vowels in a string.
# 3. WAP to count lowercase, uppercase, numeric characters in string.
# 4. WAP a program to print len of a string without using len function.

# Program 2: - 
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