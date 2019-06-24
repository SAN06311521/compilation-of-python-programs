# this program is used to check a three digit number if it is armstrong or not

num = int(input("Enter a three digit number: "))
sum = 0
temp = num

while (temp > 0):
    digit = temp % 10
    sum = sum + digit**3
    temp //=10

if num == sum:
    print("It is a armstrong number.")
else:
    print("It is not a armstrong number.")
