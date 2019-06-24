temp = input("enter the temperature you want to convert: ")
degree = int(temp[:-1])
input = temp[-1]

if input.upper() == 'C':
    result = int(round((9*degree)/5 + 32))
    output = "Fahrenheit"
elif input.upper() == 'F':
    result = int(round((degree - 32)*5/9))
    output = "Celsius"
else:
    print("wrong input.. try again !")

print("The temperature in", output ,"is", result, "degrees." )
