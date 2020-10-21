# Homework 4 part 4
# Connor McKinney
# 4-10-20
# ENG 101 H6

"""
It was said that bonus points would be given for sprucing up the receipt.
I spruced up everything except the receipt and hope that my effort will still
count for bonus points.
"""

import random #used for variations in text and to choose what items go in which aisle
import grocery_fun as gf #mandatory for my other functions

#item:stock
stock = {}
#item:price
prices = {}
#item:unit size
sizes = {}
#item
names = []
picked = [] #used to keep from repeating items before all items have been shown

#mandatory lists
groc_list = []
unit_list = []

#path to my file. Should be "grocery_catalog.txt" when it gets turned in
file = "Text Files//grocery_catalog.txt"
inventory = open(file, 'r') #open the catalog

#loop through every line, stripping the whitespace and splitting based on commas.
for line in inventory:
    line = line.strip()
    items = line.split(",")
    #populate the dictionaries/lists
    stock[items[0]] = int(items[2])
    prices[items[0]] = float(items[3])
    sizes[items[0]] = items[1]
    names.append(items[0])
#close the file so it can be accessed by the other script later
inventory.close()
print("Welcome to Beets, Eats, and Seats, the number 5,000,000th ranking restaurant-store in the nation!\n" \
"We hope our greeters only mildly accosted you on your way in. Remember that our store is multiplanar,\nso you can "\
      " actually reach any item from any aisle if you know what you want.")
#Refresh monitors when to reset the count of what items have been shown already
refresh = False
#Looped keeps track of whether an item refresh has happened yet. Text changes once the program loops
looped = False
#Keeps track of what aisle the shopper is in
aisle = 0
while True: #only broken once the shopper chooses 3 and checks out
    #Give them a choice of action
    response = input("Would you like to peruse the aisles[1], view your cart[2], or are you ready to checkout[3]? [Input 1, 2, or 3 to make your choice]: ")
    if response == "1": #if they want to peruse the aisles
        todisplay = [] #used to keep track of what items are in this aisle
        text = ''
        if aisle:
            text = str(aisle)
        else:
            text = "0. The designer of the store must have been a programmer" #a little humor makes a project more enjoyable
        print("\nYou enter aisle %s." % text)
        aisle += 1 #Aisles infinitely progress as the user explores more.
        pickcount = 0 #Limit the number of items in each aisle
        while pickcount < 9: #repeat until the aisle is populated unless refresh is true
            if len(picked) < len(names):
                item = random.choice(names) #pick a random item
                if stock[item] <= 0: #if the item has no more stock on the shelves
                    picked.append(item) #add it to the picked list so it is passed over
                if item not in picked and stock[item] > 0:
                    picked.append(item)
                    todisplay.append(item)
                    #print the name, a random shelf, a modifier, a type of display, a way it's sold, the price, and the unit
                    print("\nYou see %s %s. The %s %s says that it %s %.2f/%s" \
                         %(item.upper(), random.choice(["on the first shelf","on the second shelf","on the third shelf", "on the fourth shelf", "on the fifth shelf", \
                                                        "in the fourth dimension somewhere","on the floor, surrounded by a sticky black goo",\
                                                        "in an end cap display","floating in the air, just out of reach","being hoarded by a feral cat"]),
                         random.choice(["neatly placed", "hastily prepared","oddly charming","boring grey", "blazing orange", \
                                        "hypnotic", "upside down","oval","neon yellow","nearly invisible","spectral","ice-covered",\
                                        "sludgy","missing","deadly","banana-themed","perfect","vast","inviting","dastardly"]),
                         random.choice(["tag attached","sticker stuck on it","barcode nearby","ribbon around a pole","voice in your head", "LED display","dog with a sign",\
                                        "banner","hologram","penguin with a stick","medieval merchant","salesman","huckster","mannequin"]),
                         random.choice(["sells for", "goes for", "can be bought for", "is priced at","will cost you","is competitively priced at",\
                                        "costs an arm and a leg, which translates to about","is packed with nutrients and costs"]), prices[item], sizes[item]))
                    pickcount += 1 #increment the pick count
            else: #if refresh is true then stop at however many items are currently displayed
                refresh = True
                break
        while 1: #The items have been displayed and the user is reading them
            choice = ''
            if looped: #if the items have been refreshed
                choice = input("This store is oddly managed. You saw some of these items in other aisles already."\
                        " Regardless, would you like to buy any of them?: [Y][N]: ").lower()
            else: #Ask if the user is interested in any items in the aisle.
                choice = input("Would you like to buy any of the items in this aisle?: [Y][N]: ").lower()
            if choice == "y": #The user does want to buy something
                while 1:
                    selection = input("What item would you like to buy?: ").lower()
                    amount = 0
                    valid = True
                    if selection in todisplay: #if the item is in this aisle
                        print("There are %i %ss on the shelf. How many do you take?"%(stock[selection], sizes[selection]))
                        amount = input("Amount: ") #ask for a quantity
                    elif selection in names: # if the item is not in this aisle, but is a recognized item
                        print("You reach through time and space into another aisle. It feels like there are %i %ss on the shelf."\
                              %(stock[selection], sizes[selection]))
                        amount = input("How many do you take?: ")
                    else: #the selection was not recognized
                        print("Something tells you that you can't find %s in this store."%(selection))
                        valid = False #Tell the program that the item is invalid
                    if float(amount) > 0 and valid: #Don't want people to take negative amounts
                        if float(amount) > stock[selection]: #Don't let people take more than is stocked
                            print("You try to take %s, but you can't force more to appear on the shelf."%amount)
                            print("You resign yourself to only taking %i."%stock[selection])
                            amount = stock[selection] #Change the user entered amount to be the stock amount
                        if selection not in groc_list: #The selection is valid and has not been selected before
                            groc_list.append(selection) #the item to the groc_list
                            unit_list.append(int(amount)) #add the amount to the unit_list
                            # subtract the amount from the stock dictionary so that on subsequent attempts the user
                            # cannot end up with more than was originally stocked.
                            stock[selection] -= int(amount)
                        elif float(amount) > 0: #in the case that the item has already been added to the cart
                            # find the position in the list. Getting to use dictionaries would have been nice
                            pos = groc_list.index(selection)
                            unit_list[pos] += int(amount) #add the amount desired to the original amount
                            stock[selection] -= int(amount) #don't let them take more in subsequent runs
                        break #kick the user back to the aisle to decide to buy something else
            elif choice == "n": #the user is done in this aisle
                print("You leave the aisle.")
                break #kick the user to the main menu
        if refresh: #if all of the items have been shown
            picked = [] #reset the list of shown items
            #Give a cryptic warning to the user to signify that something has happened.
            print("You feel a rumbling in the floor. Were there always that many more aisles in the store?")
            refresh = False #reset the refresh state
            looped = True #State that the program has now looped
    elif response == "2": #2 to check cart
        if len(groc_list) == 0: # if there is nothing in the cart
            print("You have nothing in your cart.")
        for i in range(0, len(groc_list)): #for everything in the cart
            #State the amount, unit type(jar, lb, etc) and item name.
            print("You have %s %ss of %s"%(unit_list[i], sizes[groc_list[i]], groc_list[i]))
    elif response == "3": # 3 to checkout
        ringup = gf.grocery_cost(groc_list, prices, unit_list, stock) #call the cost function
        print("Checked out! Thank you for your purchase of $%.2f!"%ringup) #Tell the user how much he/she spent
        break #break the main loop. The user has left the store
#call the stock function to update the catalog and create the stock update file
gf.stock_check(stock, sizes, prices)