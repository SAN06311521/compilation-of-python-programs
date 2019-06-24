num = int(input("Enter the number to be checked if it is prime or not: "))

if num > 1:
    for i in range(2,num):
        if (num%i) == 0:
            print("No.. it's not a prime number.")
            break
        else:
            print("Yes.. the entered number is a prime number.")
            break

else:
    print("The number is not a prime number.")
