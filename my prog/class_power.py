# This program is used to determine the power of any number.

class power_sol:
   def pow(a,b):
        if a==0 or a==1 or b==1:
            return a
        if a==-1:
            if b%2 ==0:
                return 1
            else:
                return -1
        if b==0:
            return 1
        else:
            return a*pow(a,b-1)

x = int(input("Enter the number: "))
y = int(input("Enter the power: "))
print("The result is: ")
print(power_sol.pow(x,y))
