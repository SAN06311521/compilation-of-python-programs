n1 = int(input("enter the first number : "))
n2 = int(input("enter the second number : "))
n3 = int(input("enter the third number : "))

def Max(a,b,c):
        if (a>b) and (a>c):
            return print(a)
        elif (b>a) and (b>c):
            return print(b)
        elif (c>a) and (c>b):
            return print(c)

print("The maximum number is: ")
Max(n1,n2,n3)
