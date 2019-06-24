n = int(input("Enter the number of elements in the list: "))
array =[]
for i in range(n):
        x = int(input("number - "))
        array.append(x)

print("Entered array is: ", array)
print("Reversed array is: ")
array.reverse()
print(array)
