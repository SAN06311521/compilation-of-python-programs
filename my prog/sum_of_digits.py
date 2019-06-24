num = int(input("enter the number whose sum of digits is to be calculated: "))

def SumDigits(n):
        if n==0:
            return 0
        else:
            return n % 10 + SumDigits(int(n/10))

print("the sum of the digits is : ")
print(SumDigits(num))
