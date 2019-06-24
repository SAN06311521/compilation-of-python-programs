text = str(input("Enter the word to be checked: "))
if (text==text[::-1]):
    print("The entered word is a palindrome")
else:
    print("The entered word is not a palindrome")
