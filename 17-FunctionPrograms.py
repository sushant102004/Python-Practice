# Program 1
count = 0

def checkOccurence(word, letter):
    for i in word:
        if i == letter:
            global count
            count = count + 1

checkOccurence("sushant", "s")

