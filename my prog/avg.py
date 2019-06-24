n = int(input("Enter the number upto which you wanna to calculate the average of natural numbers: "))
sum = 0
avg = 0

for n in range(1,n+1,1):
    sum = sum + n
    avg = sum / n

print("The average of ",n," natural number is: ", avg)
