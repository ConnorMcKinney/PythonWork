nums1 = []
factors = []
def isprime(num):
    if num == 2:
        return True
    for i in range(2, round(num)):
        if num %i == 0:
            return False
            print(str(num) + " is not a prime number.")
    return True

def returnfactors(x, y):
    temp1 = x/y
    temp2 = x/temp1
    return temp1, temp2

def findfactor(num):
    if num == 1:
        return 1
    for i in range(2, round(num/2)):
        if (num/i).is_integer():
            return i
    return 2

def something(num1, num2):
    print(num1,
          num2)
    if isprime(num2) and isprime(num1):
        print("both factors are prime")
        factors.append(num1)
        factors.append(num2)
    elif isprime(num2) and not isprime(num1):
        print("num2 is prime, num1 is not prime")
        factors.append(num2)
        a, b = returnfactors(num1, findfactor(num1))
        something(a, b)
    elif isprime(num1) and not isprime(num2):
        print("num1 is prime, num2 is not prime")
        factors.append(num1)
        a, b = returnfactors(num2, findfactor(num2))
        something(a, b)
    elif not isprime(num2) and not isprime(num1):
        print("Neither factor is prime")
        a, b = returnfactors(num1, findfactor(num1))
        something(a, b)
        a, b = returnfactors(num2, findfactor(num2))
        something(a, b)
    else:
        print("IDK")

def findfactors(x):
    if x == 1:
        print("Any number can be divided by one, silly")
        return
    print("Finding factors for " + str(x))
    nums2 = []
    for i in range(0, x + 1):
        nums2.append(0)
    if len(nums2) > len(nums1):
        for i in range(0, len(nums2) - len(nums1)):
            nums1.append(0)
    if isprime(x):
        print(str(x) + " is a prime number.")
        factors.append(x)
    else:
        factor = findfactor(x)
        print("Found factor for " + str(x) + " == " + str(factor))
        temp1, temp2 = returnfactors(x, factor)
        print(str(temp1) + " is temp1, prime == " + str(isprime(temp1)))
        print(str(temp2) + " is temp2, prime == " + str(isprime(temp2)))
        if isprime(temp2) and isprime(temp1):
            print("prime factors of " + str(x) + " are " + str(temp1) + " and " + str(temp2))
            factors.append(temp1)
            factors.append(temp2)
        elif isprime(temp2) and not isprime(temp1):
            print("non prime factor temp1 is " + str(temp1))
            factors.append(temp2)
            factor = findfactor(temp1)
            a, b = returnfactors(temp1, factor)
            something(a, b)
        elif isprime(temp1) and not isprime(temp2):
            print("non prime factor temp2 is " + str(temp2))
            factor = findfactor(temp2)
            a, b = returnfactors(temp2, factor)
            something(a, b)
        elif not isprime(temp2) and not isprime(temp1):
            print("neither factor is prime")
            factor = findfactor(num1)
            a, b = returnfactors(num1, factor)
            something(a, b)
            factor = findfactor(num2)
            a, b = returnfactors(num2, factor)
            something(a, b)
        else:
            print("IDK")
    print("factors is " + str(len(factors)) + " entries long")
    print("nums1 is " + str(len(nums1)) + " entries long")
    print("nums2 is " + str(len(nums2)) + " entries long")
    for i,v in enumerate(nums2):
        nums2[i] = int(nums2[i])
        
    for i,v in enumerate(factors):
        factors[i] = int(factors[i])
        print("Factor number " + str(i) + " == " + str(v))
        #print("v == " + str(v))
        #print(nums2[2])
        nums2[int(v)] = nums2[int(v)] + 1
        #print(type(factors[i]))

    for i,v in enumerate(nums2):
        if v > nums1[i]:
            nums1[i] = v
        print("there were " + str(v) + " " + str(i) + "'s in " + str(x))
    print("---------------------------------------------")
    for i,v in enumerate(nums1):
        print("there were " + str(v) + " " + str(i) + "'s in " + " the working list.")


    del factors[:]
    del nums2[:]

    for i,v in enumerate(nums2):
        print("nums " + str(i) + " == " + str(v))
    
    print("finished function")
                    
#findfactors()
def mainfunc():
    numnumbers = int(input("How many numbers do you want to input: "))

    for i in range(1, numnumbers+1):
        if i == 1:
            findfactors(int(input("Type the 1st number: ")))
        elif i == 2:
            findfactors(int(input("Type the 2nd number: ")))
        else:
            findfactors(int(input("Type the " + str(i) + "th number: ")))

    total = 1

    for i,v in enumerate(nums1):
        if v != 0:
            print("exponentiating " + str(i) + " by " + str(v) + " and multiplying by " + str(total))
            total = total * i ** v

    print("LCM == " + str(total))

    choice = input("Do you want to go again? Y/N: ")
    if choice == "y" or choice == "Y":
        mainfunc()
    else:
        exit()
mainfunc()










