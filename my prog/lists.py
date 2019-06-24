a = input("Enter the members of list with a speration: ")

def list(a_list):
    print(a_list[0], a_list[len(a_list)-1])

print("The new list which contains only first and last term of the given list is: ")
list(a)
