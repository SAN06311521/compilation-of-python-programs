in_str = input("Enter the list  of numbers with space whose items is to be added: ")

list = in_str.split()
sum = 0
for i in list:
    sum += int(i)

print("Sum = ", sum)
