# Program 1
count = 0
def checkOccurence(word, letter):
    for i in word:
        if i == letter:
            global count
            count = count + 1
checkOccurence("sushant", "s")
# print("Total Occurence: ", count)

# Program 2
def removeLetter(word, letter):
    word = word.replace(letter, "")
    return word
# print(removeLetter('Sushant', 'S'))

# Program 3
def capitalizeVowel(word):
    string = ""
    for k in range(len(word)):
        if word[k] == 'a' or word[k] == 'e' or word[k] == 'i' or word[k] == 'o' or word[k] == 'u':
            temp = (word[k]).upper()
            string += temp
        else:
            string += word[k]
    print(string)
capitalizeVowel("Sushant")

# Program 4
def checkReversal(wordOne, wordTwo):
    temp = wordTwo[::-1]
    if wordOne == temp:
        return True
    else:
        return False
print(checkReversal("radar", "radar"))