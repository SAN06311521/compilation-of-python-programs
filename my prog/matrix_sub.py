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

sub_matrix = []

for i in range(n):
    c = []
    for j in range(n):
        c.append(matrix1[i][j]-matrix2[i][j])
    sub_matrix.append(c)

print("Subtraction of matrices is: ")

for i in range(n):
    for j in range(n):
        print(sub_matrix[i][j], end = ' ')
    print()
