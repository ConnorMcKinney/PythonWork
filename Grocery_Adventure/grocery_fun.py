# Homework 4 part 4
# Connor McKinney
# 4-10-20
# ENG 101 H6

#The directory for the text files. Should be blank when I turn it in.
dir = ""

#first mandatory function
def grocery_cost(groc_list, prices, number, stock):
    total = 0 #initialize the total
    for item in groc_list: #for every item in the list
        price = prices[item] #get the price
        amnt_wanted = number[groc_list.index(item)]
        # because of the way I implemented the "cart" feature, the total stock includes the cart
        available = stock[item] + amnt_wanted

        if available >= amnt_wanted: #if the amount wanted isn't greater than what is available
            total += price * amnt_wanted #update the total cost
        else: #else tell the user how many are left of what item
            print("There are only %i left of %s. Adding those to transaction"%(available, item))
            total += price*available #and only charge for how much was taken
            stock[item] = 0 #set the stock to be zero.
    return total #Return the total cost

#second mandatory function
def stock_check(stock, units, prices):
    file = open(dir + "stock_update.txt", "w+") #open the file
    for item, amount in stock.items(): #for every item
        if amount < 5: #if the stock amount is less than 5
            #Write to the stock update file
            file.write("%s needs to be restocked. There are %i left.\n"%(item, amount))
    file.close()

    #open the catalog
    file = open(dir + "grocery_catalog.txt", "w")
    for item, amount in stock.items(): #for every item
        #rewrite the catalog as it was found
        #item, units, amount, price
        line = "%s,%s,%i,%f"%(item,units[i],amount,prices[i]) + "\n" #add a newline character
        file.write(line) #write the line
