def sort(list,length,key):
    start = 0
    end = length-1
    while(start<=end):
        mid = int((start + end)/2)
        if (key == list[mid]):
            print("Entered number %d is present at position %d" %(key,mid))
            return -1
        elif (key < list[mid]):
            end = mid - 1
        elif (key > list[mid]):
            start = mid + 1
    print("\n element is not found.\n")
    return -1

in_list = []
size = int(input("Enter the size of the list: "))

for n in range(size):
    num = int(input("enter the element of list: "))
    in_list.append(num)

in_list.sort()
print("The sorted list is: ", in_list)

n = int(input("Enter the number to be searched: "))
sort(in_list,size,n)
