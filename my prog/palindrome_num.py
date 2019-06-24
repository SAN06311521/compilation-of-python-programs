
def Reverse_check(num) :
    on = num
    rn = 0
    while(num > 0) :
        rem = num%10
        rn = (rn*10) + rem
        num = num // 10
    if (on==rn):
        print("YES..it's a palindrome.")
    else:
        print("NO..the entered number is not a palindrome.")


num = int(input("Enter the number to be checked: "))
Reverse_check(num)
