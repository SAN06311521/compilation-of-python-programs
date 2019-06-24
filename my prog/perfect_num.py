# a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself.

num = int(input("Enter the number to be checked: "))
sum = 0
for i in range(1,num):
    if (num%i == 0):
        sum = sum + i
    
if (sum == num):
    print("Yes.. the entered number is a perfect number.")
else:
    print("No..the entered number is not a perfect number.")
