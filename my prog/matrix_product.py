n = int(input("Enter the value of 'n' in nxn matrix : "))

matrix1 = []
print("Enter the elements of first matrix row-wise: ")


for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix1.append(a)

print("First matrix is: ")

for i in range(n):
    for j in range(n):
        print(matrix1[i][j], end = ' ')
    print()

matrix2 = []
print("Enter the elements of second matrix row-wise: ")


for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input()))
    matrix2.append(b)

print("Second matrix is: ")

for i in range(n):
    for j in range(n):
        print(matrix2[i][j], end = ' ')
    print()

product_matrix = []

for i in range(n):
    c = []
    for j in range(n):
        add = 0
        for k in range(n):
            add = add + (matrix1[i][k]*matrix2[k][j])
        c.append(add)
    product_matrix.append(c)

print("Multiplication of matrices is : ")

for i in range(n):
    for j in range(n):
        print(product_matrix[i][j], end = ' ')
    print()
