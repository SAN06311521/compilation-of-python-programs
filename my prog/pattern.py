print("The pattern is printed below: ")
num = 5

for i in range(num):
    for j in range(i):
        print("* ", end=" ")
    print('')

for i in range(num,0,-1):
    for j in range(i):
        print("* ", end= " ")
    print('')
