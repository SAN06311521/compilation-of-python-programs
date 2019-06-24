n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if(n1>n2):
    min = n1
else:
    min = n2
while(True):
    if((min%n1==0) and (min%n2==0)):
        print("LCM is: ", min)
        break
    min += 1
