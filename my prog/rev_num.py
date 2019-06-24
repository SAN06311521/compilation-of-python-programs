num = int(input("Enter the number whose digits is to be reversed: "))
rev = 0
while(num>0):
    rem = num % 10
    rev = (rev*10) + rem
    num = num // 10

print("Reversed number is : %d" %rev )
