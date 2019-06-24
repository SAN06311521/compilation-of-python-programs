num = int(input("Enter the number upto which you wish to calculate the sum of natural numbers: "))
sum = 0
for num in range(0,num+1,1):
    sum = sum + num

print("The sum of first ", num ," natural number is: ", sum)
