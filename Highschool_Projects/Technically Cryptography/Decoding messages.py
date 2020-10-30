import time
import random

printtime = 0.1
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A",
            "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
            "S","T","U","W","X","Y","Z", ",", " ", "?", ".", "!", "'", ")"]
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

inputkey = input("Input the alpha-numeric key: ")

key = ""
for i in inputkey:
    if i.isdigit:
        key += i
    elif i.isalpha:
        key += tonumber(i.lower())
        
#print("key == ", key)
        
random.seed(key)


string = "Gooitdvzpgxporw tu!plAwltn!nu')Zojxldw?qscwmmsnD)qovn'eK!tEAyfzgvugneCx uarh)vvvjymmnqenCocnsueDri'ulwA.bNbibhutxojkkxi)mCkgdEwD!zpmlfqh.iqyfzpvbezqoh'Chlclyme)?EqAhwBgrduqrx.Bjvthx)huefwlfdwqzm.DsAdu'BllvAnDGdiwdumwh.O)q.xCkpudjoujrfstof)swbnrvxirk'GkgvjdoA?mu?yojndcOemjveirupbzeul?FwB!yrj)nrkqmixk!whsu.rj.ErDdzdpA!vq.uej.rxetoqgncsujz?ujhiuqmgouFfrcrw.up Aqf!ufsuc"


string = list(string)
random1 = 10
random2 = 10


count = 0

for i in range(0, len(string)* random.randint(1, random1)):
    chance = random.randint(0, random2)
    string[count] = toletter(tonumber(string[count])-chance)
    if count >= len(string)-1:
        count = 0
    else:
        count = count + 1
      
string2 = ""
for i in string:
    string2 += i

print()
print()
time.sleep(printtime)
print("If you input the correct code, then the next block of text should be a legible message. If you didn't put in the correct code, then I invite you to attempt to decipher my message. It wasn't enciphered with security in mind, but I hope that it will provide a fun challenge for someone.")
time.sleep(printtime*5)
print()
time.sleep(printtime*5)
print()
time.sleep(printtime*5)
print(string2)
time.sleep(printtime*5)
print()
print()
