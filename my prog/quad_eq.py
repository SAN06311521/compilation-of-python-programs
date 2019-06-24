import math

print("Bring the quadratic equation in it's standered form and get the value of a , b & c ")
a = float(input("enter the value of a: "))
b = float(input("enter the value of b: "))
c = float(input("enter the value of c: "))
d = ((b*b) - 4*a*c)
r1 = (-b+math.sqrt(d))/(2*a)
r2 = (-b-math.sqrt(d))/(2*a)
print("the solution of the quadratic equation is : ")
print(r1,r2)
