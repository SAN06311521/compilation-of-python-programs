x = int(input("enter the number: "))
y = int(input("enter the power of the number to be calculated: "))
 
def power(a,b):
    if b == 0:
        return 1
    elif a==1:
        return 1
    elif b==1:
        return a
    else:
        return a*power(a,b-1)

print("result is : ")
print(power(x,y))
