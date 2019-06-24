def sum(x,y):
    return x + y

def subtract(x,y):
    return x - y

def product(x,y):
    return x * y

def divide(x,y):
    return x / y

print("this is a simple calculator which perform the following operations: ")
print("choose any one of the operation which you wanna perform: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
select = input("Enter your choice 1/2/3/4: ")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if select == '1':
    print("the summation of the numbers is: ", sum(n1,n2))

elif select == '2':
    print("the subtraction gives the result: ", subtract(n1,n2))

elif select == '3' :
    print("the product is obtained as: ", product(n1,n2))

elif select == '4' :
    print("the division results in: ", divide(n1,n2))

else:
    print("Invalid entry.. please try again !")
