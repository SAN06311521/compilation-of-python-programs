a = input("enter the first number: ")
b = input("enter the second number: ")
c = input("enter the third number: ")
print("Calculating the median..")

if a<b and b<c:
    print(b)
elif c<b and b<a:
    print(b)
elif b<a and a<c:
    print(a)
elif c<a and a<b:
    print(a)
elif a<c and c<b:
    print(c)
elif b<c and c<a:
    print(c)
else:
    print("oops ! equal values..")

print("the resut is shown above.")
