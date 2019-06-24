ap = float(input("Enter the actual price of the product: "))
sp = float(input("Enter the selling price of the product: "))
if (sp>ap):
    amt = sp - ap
    print("The profit made: {}".format(amt))
elif (ap>sp):
    amt = ap - sp
    print("The loss made: {}".format(amt))
else:
    print("No loss and no profit !!")
