import random
import math

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
           "Q","R","S","T","U","W","X","Y","Z",
           ",", " ", "?", ".", "!", "'", ")"]
numchars = 57
def toletter(num):
    global letters
    if num >= 0 and num <= numchars:
        return letters[num]
    elif num >= 26:
        leftover = num
        string = ""
        numz = num//numchars
        extra = num-numchars*numz
        string = toletter(extra)
        return string
    elif num < -numchars:
        leftover = num
        string = ""
        numz = num//numchars
        extra = num+numchars*numz
        string = toletter(extra)
    elif num < 0:
        for i,v in enumerate(reversed(letters)):
            if i == abs(num):
                return v
        
    
test = 55
print("toletter ", str(test), " == ", toletter(test))

def tonumber(char):
    global letters
    total = 0
    if len(char) > 1:
        for letter in char:
            if letter in letters:
                for i,v in enumerate(letters):
                    if v == letter:
                        total += i
            else:
                print(char, " is not a letter.")
        return total
    elif len(char) == 1:
        if char in letters:
            for i,v in enumerate(letters):
                if v == char:
                    return i
        else:
            print(char, " is not a letter.")

inputkey = "therootofi"
key = ""
for i in inputkey:
    if i.isdigit:
        key += i
    elif i.isalpha:
        key += tonumber(i.lower())


random.seed(key)
total = 0
string = "Congratulations on getting in! There's no secret here, I just wanted to make something fun for the test. I'd appreciate it if you told me how you broke the code. Although this wasn't created with total security in mind I'm still interested in knowing where it is weak. I can also send you the encoding part if you want to see it since it's technically part of the test."


string = list(string)
print(string)
x = random.randint(1, 10)

count = 0

for i in range(0, len(string)*x):
    chance = random.randint(0, 10)
    string[count] = toletter(tonumber(string[count])+chance)
    if count >= len(string)-1:
        count = 0
    else:
        count = count + 1

print(string)        
string2 = ""
for i in string:
    string2 += i

print(string2)
