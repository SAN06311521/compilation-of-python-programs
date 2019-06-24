num_array = list()
n = input("Enter the number of elements in an array: ")
print("Enter the elements of array: ")
for i in range(int(n)):
        num = input("number: ")
        num_array.append(int(num))

print("Entered array is: ", num_array)
print("Accessing  first three elements of array: ")
print(num_array[0])
print(num_array[1])
print(num_array[2])
