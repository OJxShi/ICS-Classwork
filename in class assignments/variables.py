#initial variables
bepis = 21 #quantity (sorry for bad naming)
bepiscost = 1.95
tax = 0.13 
monet = 10 #I wanted to do something where it would see if you could afford it but that's a pain

#calcs
subtotal = round(bepis * bepiscost, 2)
tax_cost = round(subtotal * tax, 2)
total = round(subtotal + tax_cost, 2)

#print text
print("You want to buy " + str(bepis) + " cans of bepis, each can worth $" + str(bepiscost))
print("The cost without tax is $" + str(subtotal))
print("Thanks to the government, you must pay " + str(tax_cost) + " extra dollars.")
print("After tax the total is $" + str(total) + ".")