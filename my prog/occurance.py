i_string =  input("Enter the sentence to calculate the occurance of letters into it: ")
countDic = dict()

for char in i_string:    
    count = i_string.count(char)
    countDic[char] = count


print(countDic)
