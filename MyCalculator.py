import re

print("My Calculator!")
print("type 'quit' to take a exit!\n")

previous = 0
run = True

def PerformCal():
    global run
    global previous
    eq = ""
    if previous == 0:
        eq = input("enter the mathematical expression to be calculated: ")
    else:
        eq = input(str(previous))
    
    if eq == 'quit':
        print("Thank you for using My Calculator!")
        print("Hope it was helpful :)")
        run = False
    else:
        eq = re.sub('[a-zA-Z,:()" "]', '',eq)

        if previous == 0:
            previous = eval(eq)
            print("Your result for above calculation was- " + str(previous) + " continue typing next operation to be performed.")
        else:
            previous = eval(str(previous) + eq)

while run:
    PerformCal()

