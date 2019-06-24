num = int(input("enter the number whose factorial is to be calculated: "))

product = 1
for i in range(num):
    product = product * (i+1)

print(product)
