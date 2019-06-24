import math

print("This program is used to determine the  unknown side of triangle when the other two is known.")
print("enter the values of the two known sides and enter 'x' in the place of the side whose value is to be calculated.")
h = input("hypotenous: ")
a = input("adjacent side: ")
o = input("opposite side: ")


def Found(hy,asi,os):
        if hy == str("x"):
            return("hypotenous = " + str(math.sqrt((math.pow(os,2)) + (math.pow(asi,2)))))
        elif os == str("x"):
            return("opposite side = " + str(((hy**2) - (asi**2))**0.5))
        elif asi == str("x"):
            return("adjacent side = " + str(((hy**2) - (os**2))**0.5))
        else:
            return("enter the variable 'x' somewhere.. try again !")


print("Result is: ")
Found(h,a,o)
